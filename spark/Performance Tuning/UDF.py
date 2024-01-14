from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import os
import os
import sys


spark = SparkSession.builder.appName("spark_test").getOrCreate()
sc = spark.sparkContext

columns = ["serial_no","topic"]
data = [("1", "hadoop"),("2", "aws"),("3", "hive"),("4", "spark")]

df = spark.createDataFrame(data=data,schema=columns)

df.show(truncate=False)

def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr 

# Converting function to UDF 
convertUDF = udf(lambda z: convertCase(z),StringType())



df.select(col("serial_no"), \
    convertUDF(col("topic")).alias("topic") ) \
   .show(truncate=False)