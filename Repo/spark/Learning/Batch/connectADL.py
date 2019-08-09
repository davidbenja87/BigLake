
import findspark
findspark.init()

import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
spark = SparkSession \
    .builder \
    .appName("MyApp") \
    .config("spark.driver.host", "localhost") \
    .getOrCreate()


 spark.conf.set("spark.executor.memory", '8g')
 spark.conf.set('spark.executor.cores', '3')
 spark.conf.set('spark.cores.max', '3')
 spark.conf.set("spark.driver.memory",'8g')    