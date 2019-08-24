from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()
#read azure data lake gen 1
    df = spark.read\
    .format("csv")\
    .option("header", "true")\
    .option("sep", "|")\
    .option("inferSchema", "true")\
    .option("mode", "failfast")\
    .option("nullValue", "NA")\
    .option("path", "adl://datalakepocplaygroundrba.azuredatalakestore.net/Landing Zone/Supported Track/Accuity/minecraftstory.txt")\
    .load()

#read azure data lake gen 2
    df = spark.read\
        .format("csv")\
        .option("header", "true")\
        .option("inferSchema", "true")\
        .option("mode", "failfast")\
        .option("nullValue", "NA")\
        .option("path", "abfs://bdap@biglakestorageaccount.dfs.core.windows.net/example/data/fruits.txt")\
        .load()
    
    df.show()    
    
  

    # df.write\
    # .format("parquet")\
    # .mode("overwrite")\
    # .save("adl://datalakepocplaygroundrba.azuredatalakestore.net/Raw Zone/Supported Track/Accuity/parquet-data/")


    
    # dfParquet = spark.read\
    # .format("parquet")\
    # .option("header", "true")\
    # .option("inferSchema", "true")\
    # .option("mode", "failfast")\
    # .option("nullValue", "NA")\
    # .load( "adl://datalakepocplaygroundrba.azuredatalakestore.net/Raw Zone/Supported Track/Accuity/parquet-data/")

    # df.write\
    # .format("csv")\
    # .mode("overwrite")\
    # .saveAsTable("mysparkdb.account")

#create database
    spark.sql('Create database test')
    # print(spark.catalog.listDatabases.show(False))


    # df.show()
    

 
#
# # read file from Azure data lake store
# df = spark.read\
#     .format("csv")\
#     .option("header", "true")\
#     .option("inferSchema", "true")\
#     .option("mode", "failfast")\
#     .option("nullValue", "NA")\
#     .option("path", "adl://biglakepoctest.azuredatalakestore.net/LandingZone/survey.csv")\
#     .load()
#
# counters = lines.flatMap(lambda x: x.split(' ')) \
#              .map(lambda x: (x, 1)) \
#              .reduceByKey(add)

# coll = counters.collect()
# sortedCollection = sorted(coll, key = lambda r: r[1], reverse = True)

# for i in range(0, 5):
#      print(sortedCollection[i])