import findspark
findspark.init()

import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
spark = SparkSession.builder.getOrCreate()

df = spark.sql('''select 'spark' as hello ''')
df.show()

# read a csv files from local
dflocal = spark.read.options(header="true",
inferSchema = "true",
nullValue = "NA",
timestampFormat = "yyyy-MM-dd'T'HH::mm::ss",
mode="failfast"
).csv("C:\\Users\\Ben\\Documents\\spark-Data\\mental-health-in-tech-survey\\survey.csv")

#select few columns

dflocal = dflocal.select("Gender","treatment")

#transform few columns
dflocalG = dflocal.select(dflocal["Gender"],
    f.when(dflocal["treatment"] == "Yes",1).otherwise(0).alias("All-Yes"),
    f.when(dflocal["treatment"] == "No",1).otherwise(0).alias("All-No")
)

print(dflocalG.dtypes)
# dflocalG.groupBy(dflocalG["Gender"]).agg(sum("All-Yes"),sum("All-No"))
# df.groupBy("gender").
# dflocal.
# 
# ()