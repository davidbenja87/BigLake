import findspark
findspark.init()

import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
spark = SparkSession.builder.getOrCreate()

# # Read csv and write into parquet format
# df = spark.read  \
#  .format("csv") \
#  .option("header","true")\
#  .option("nullValue","NA")\
#  .load(r"C:\Users\Ben\Documents\spark-Data\mental-health-in-tech-survey\survey.csv")

# #write Data frame to parquet
# df.write  \
# .format("parquet") \
# .mode("overwrite") \
# .save(r"C:\Users\Ben\Documents\spark-Data\mental-health-in-tech-survey\parquet-data")

# df.write.parquet("temp.parquet")  
# parquetFile = spark.read.parquet("temp.parquet")
# .format("parquet") \
# .mode("overwrite") \
# .save(r"C:\Users\Ben\Documents\spark-Data\mental-health-in-tech-survey\parquet-data")

#read parquet and write into json

df = spark.read\
    .format("parquet")\
    .load("C:\\Users\\Ben\\Documents\\spark-Data\\mental-health-in-tech-survey\\parquet-data")
 
df.show()          
