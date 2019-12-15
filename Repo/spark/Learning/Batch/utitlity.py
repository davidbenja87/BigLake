# # from environment import Environments
# import environment

# # print(Environments.SANDBOX)
# print(environment.SANDBOX)
# # User access token - dapi038f703e35a19eb6f34d49297fde01d9
# # cluster id - 1212-155528-fast77
# # organisation id - 1040887839144818
# # port - 15001
# # url https://westeurope.azuredatabricks.net/

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.sql("SELECT * FROM Accuity.unity_account")
df.show()
