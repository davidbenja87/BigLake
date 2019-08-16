from __future__ import print_function
 import sys
 from operator import add
 from pyspark.sql import SparkSession
 if __name__ == "__main__":
     spark = SparkSession\
         .builder\
         .appName("PythonWordCount")\
         .getOrCreate()

     lines = spark.read.text('adl://datalakepocplaygroundrba.azuredatalakestore.net/Landing%20Zone/Supported%20Track/Accuity/dbo.BWDRE_Account.txt')
     lines.collect()
     spark.stop()