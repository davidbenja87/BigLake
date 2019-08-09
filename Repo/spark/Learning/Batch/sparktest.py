
import sys,os
os.environ["SPARK_HOME"] = r'C:\Spark\sparkinstallation\spark-2.1.0-bin-without-hadoop'
os.environ['PYSPARK_PYTHON'] = r'C:\Users\sugumarb\AppData\Local\Programs\Python\Python35'
os.environ['PYSPARK_DRIVER_PYTHON'] = r'ipython'
os.environ['JAVA_HOME'] = r'C:\Spark\jdk-11.0.1'
os.environ['HADOOP_HOME'] = r'C:\Spark\sparkinstallation\hadoop-3.0.0-alpha2'
os.environ['HADOOP_CLASSPATH'] = r'C:\Spark\sparkinstallation\hadoop-3.0.0-alpha2\share\hadoop\tools\lib\*'
os.environ['JAVA_HOME'] = r'C:\Spark\jdk-11.0.1'
sys.path.append('C:\Spark\sparkinstallation\spark-2.1.0-bin-without-hadoop\python')
sys.path.append('C:\Spark\sparkinstallation\spark-2.1.0-bin-without-hadoop\python\lib\py4j-0.10.4-src.zip')


from pyspark import SparkContext
sc = SparkContext("local", "Simple App")

rdd = sc.textFile(r"C:\D\Biglake\minecraftstory.txt")
rdd.collect()