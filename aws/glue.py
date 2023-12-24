from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

spark = SparkSession.builder.appName("spark_test").getOrCreate()
sc = spark.sparkContext
df = spark.read.json("s3://porjectdata/zipcodes.json")

df.printSchema()
df.show(10,False)
df2=df.select(col("City"),col("Country"),col("EstimatedPopulation")).where(col("EstimatedPopulation").isNotNull())
#df2.createOrReplaceTempTable(df2_temp_table)
#df2.write.mode('overwrite').saveAsTable("population_by_area")

df2.write.mode('append').csv("s3://result1612/")