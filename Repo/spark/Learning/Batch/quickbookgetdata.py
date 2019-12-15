import math
import sys

import json
from pandas.io.json import json_normalize
import pandas as pd

from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects import *
from pyspark.sql import functions as F
from pyspark.sql.types import *
from datetime import datetime
from pyspark.dbutils import DBUtils


from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark.sparkContext)

CLIENT_ID = "ABGA9WMqhlrmpP39UxG5Q3H2227bLiXsIWVTeoq0UnQVW2B8fw"
CLIENT_SECRET = "risgBjg1RqjqK8AVDHnYmbwnY46vG0K45v6kG3FH"
REDIRECT_URI = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
ENVIRONMENT = 'sandbox'
REFRESH_TOKEN = "AB115848891146ZaHw6LwvFP0afcRg4iNHB3BkAlFY7h4tvRuO"
COMPANY_ID = "4620816365025351930"
destpath = "/mnt/bdapcode/QuickBookTokens"
market = "QBSA"

BUSINESS_OBJECTS = [
        Account, Attachable  
        
    ]
         
# BUSINESS_OBJECTS = [
#         Account, Attachable, Bill, BillPayment,
#        Class, CreditMemo, Customer,
#         Department, Deposit, Employee, Estimate, Invoice,
#         Item, JournalEntry, Payment, PaymentMethod,
#         Purchase, PurchaseOrder, RefundReceipt,
#         SalesReceipt, TaxAgency, TaxCode, Term,
#         TimeActivity, Transfer, Vendor, VendorCredit
  
        
#     ]

def xstr(s):
    if s is None:
        return ''
    return str(s)
  
def fileExists(path : str):
  try:
    dbutils.fs.ls(path)
    res = True
  except:
    res = False
  return res    
  
#create file if not exists

def create_token_file(market : str, destpath : str):
  
    data_schema = [StructField('Market', StringType(), True), StructField('Old_Refresh_token', StringType(), True),StructField('Current_Refresh_token', StringType(), True)\
                   ,StructField('ModifiedDate', TimestampType(), True)]
    final_struc = StructType(fields=data_schema)
    df = spark.createDataFrame([{"Market": market, "Old_Refresh_token": "", "Current_Refresh_token": "", "ModifiedDate" : datetime.now()},
                                 ],schema = final_struc)
     
  
    if not fileExists(destpath):
      
        df.write.format("csv").mode("Overwrite").options(header="true",sep="\t").save(destpath)
    else: 
        _df = read_file(destpath)
        _df = _df[_df['Market'] == market]
        if _df.count() == 0:
          print("append Market : ", market)
          df.write.format("csv").mode("append").options(header="true",sep="\t").save(destpath)

def read_file(destpath : str):
    df= spark.read \
      .option("wholeFile", True) \
      .option("multiline",True) \
      .option("header", True) \
      .csv(destpath,sep='\t',header='true' ,quote='"',encoding='utf-8')  
    return df    

def get_recent_token(market : str, destpath : str):
    create_token_file(market, destpath)
    df = read_file(destpath)
    tokenlist = df.filter(df.Market == market).select("Current_Refresh_token").collect()
    Current_Refresh_token = tokenlist[0][0]
    Current_Refresh_token = xstr(Current_Refresh_token)
    return Current_Refresh_token,df


# # #get refresh token

def update_refresh_token(df, Current_Refresh_token : str, New_refresh_token : str, destpath : str):
    
    if Current_Refresh_token != New_refresh_token:
        print("Tokens are different")
        print(Current_Refresh_token)
        df = df.withColumn("Old_Refresh_token", F.when(F.col("Market")== market, Current_Refresh_token).otherwise(df.Old_Refresh_token))
        df = df.withColumn("Current_Refresh_token", F.when(F.col("Market")== market, New_refresh_token).otherwise(df.Current_Refresh_token))
        df = df.withColumn("ModifiedDate", F.when(F.col("Market")== market, datetime.now()).otherwise(df.ModifiedDate))
        df.write.format("csv").mode("Overwrite").options(header="true",sep="\t").save(destpath)


 


# ##################################

auth_client = AuthClient(
        client_id= CLIENT_ID,
        client_secret=CLIENT_SECRET,
        environment= ENVIRONMENT,
        redirect_uri= REDIRECT_URI,
    )

try:
    auth_client.refresh(refresh_token=REFRESH_TOKEN)
    current_token,df = get_recent_token(market, destpath)
except:
    current_token,df = get_recent_token(market, destpath)
    REFRESH_TOKEN = current_token
    auth_client.refresh(refresh_token=REFRESH_TOKEN)
finally:
  New_token = auth_client.refresh_token
  update_refresh_token(df,current_token,New_token,destpath) 
  
    
ACCESS_TOKEN = auth_client.access_token,
print(ACCESS_TOKEN)
client = QuickBooks(
        auth_client=auth_client,
        refresh_token= REFRESH_TOKEN ,
        access_token=ACCESS_TOKEN,
        company_id=COMPANY_ID
    )    


def set_download_path(market : str, datasoruce : str, entity : str, zone : str):
  path = "/mnt/bdap/" + zone +"/SupportedTrack/" + market + "/" + datasoruce + "/" + entity + "/"
  return path

def querycutomized(cls, select, qb=None):
    """
    :param select: QBO SQL query select statement
    :param qb:
    :return: Returns list
    """
    if not qb:
        qb = QuickBooks()
    json_data = qb.query(select)
    return json_data   

def getentitydata(obj, entity : str, qb = None, offset : int = 1, limit : int = 100):
    objdata = querycutomized(obj,"select * from " + entity + "  STARTPOSITION " + str(offset) + " MAXRESULTS "+ str(limit), qb = qb)
    objdata = objdata["QueryResponse"][entity]
    df = json_normalize(objdata)
    return df

def getentitycount(obj, entity : str, qb = None):
    
    objcount = obj.count( qb = qb)
    return objcount  

def getentitydatafull(obj, destpath : str, entity : str, qb = None):
    offset = 1
    limit = 100
    obj = obj()
    counter = getentitycount(obj, entity, qb)
    if counter > 0:
        iter = math.ceil(counter / 100)
    else:
        iter = 0
    
    if iter > 0:
        dbutils.fs.rm(destpath,True)
        
        for i in range(int(iter)):
            data = getentitydata(obj, entity, qb, offset,limit)
            spark_df = spark.createDataFrame(data.astype(str))
#             spark_df = spark.createDataFrame(data)
            spark_df.write.format("csv").mode("append").options(header="true",sep="\u0001").save(destpath)
            offset= offset + 100 
      
  

######################################

def readLandingFile(srcpath: str):
  
  df= spark.read\
  .option("wholeFile", True)\
  .option("multiline",True)\
  .option("header", True)\
  .csv(srcpath,sep='\u0001',header='true' ,quote='"',encoding='utf-8')
  return df

def writingTempFiles(srcpath: str,tblname: str):
  
  df=readLandingFile(srcpath)
#   df =df.to_string()
  df= df.registerTempTable(tblname)
  return df

def convertFileLandingToRawZone(df: pd.DataFrame,destpath: str):
  
  # read file and convert into parquet
  df.write.format("parquet").mode("overwrite").options(header="true",sep="\t").save(destpath)
  

def fileExists(path : str):
  try:
    dbutils.fs.ls(path)
    res = True
  except:
    res = False
  return res  
       
  
# Entity 

def LandingToRaw(market : str, entity: str, path: str):
  
  if fileExists(path):
    writingTempFiles(path , entity)
    df= spark.sql("SELECT * \
    from " + entity )
    destpath= path.replace("LandingZone","RawZone")
    convertFileLandingToRawZone(df,destpath)

  

def savingFileAsTable(market : str, entity: str, path : str):
  entity = market + '.' + entity
  spark.sql("DROP TABLE IF EXISTS " + entity)
  spark.sql("CREATE TABLE  " + entity +  \
  " USING parquet \
  LOCATION '"+ path +"'")
  spark.sql("REFRESH TABLE " + entity)
      
# working code
#################################################################################################################


# Getting file form QB into Landing Zone
for ob in BUSINESS_OBJECTS:
    name = repr(ob.__name__).strip("\'")
    try:

        getentitydatafull(ob, set_download_path(
                                                          'Proagrica', 
                                                          'QBSA', 
                                                           name, 
                                                          'LandingZone'
                                                           ), 
                                name, 
                               qb = client
                              )
    except NameError:
        "Object not exit " +name

# Moving file from Landing Zone into RawZone

for ob in BUSINESS_OBJECTS:
  name = repr(ob.__name__).strip("\'")
  path = set_download_path(
                                                        'Proagrica', 
                                                        'QBSA', 
                                                         name, 
                                                        'LandingZone'
                                                         )
  print(path)
  LandingToRaw('Proagrica',name,path)
  despath = set_download_path(
                                                        'Proagrica', 
                                                        'QBSA', 
                                                         name, 
                                                        'RawZone'
                                                         )
  if fileExists(path):
    savingFileAsTable('Proagrica', 'QBSA' + '_' + name, despath)
  print(despath)
  

# def main():
#     ls = ['Account']
#     def str_to_class(str):
#       return getattr(sys.modules[__name__], str)
    
#     for ob in ls:
#        getentitydatafull(str_to_class(ob), set_download_path(
#                                                     'Proagrica', 
#                                                     'QBSA', 
#                                                      'Account', 
#                                                     'LandingZone'
#                                                      ), 
#                           'Account', 
#                          qb = client
#                         )
    

# if __name__ == "__main__":
#     main()