from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    df = spark.read\
    .format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .option("mode", "failfast")\
    .option("nullValue", "NA")\
    .option("path", "adl://datalakepocplaygroundrba.azuredatalakestore.net/Landing%20Zone/Supported%20Track/Accuity/dbo.BWDRE_Account.txt")\
    .load()

    df.show()
    

 
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