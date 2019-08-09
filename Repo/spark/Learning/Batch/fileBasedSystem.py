from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# spark session is used to build entry point to spark sql
spark = SparkSession.builder.appName('abc').getOrCreate()
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
# #write file into azure data lake as parquet format
# df.write\
#     .format("parquet")\
#     .mode("overwrite")\
#     .save("adl://biglakepoctest.azuredatalakestore.net/RawZone/survey-data/")

#read parquet file and write into json

dfParJson = spark.read\
    .format("parquet")\
    .option("mode", "failfast")\
    .load("adl://biglakepoctest.azuredatalakestore.net/RawZone/survey-data/")

dfParJson.write\
    .format("json")\
    .mode("overwrite")\
    .save("adl://biglakepoctest.azuredatalakestore.net/RawZone/json-data/")