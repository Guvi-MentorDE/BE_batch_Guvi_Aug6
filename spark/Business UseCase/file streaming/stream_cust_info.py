from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window


def stream():
    spark = SparkSession.builder.appName("spark_test").getOrCreate()
    sc = spark.sparkContext

    spark = SparkSession \
    .builder \
    .appName("user-logs-analysis-streaming") \
    .getOrCreate()
    
    schema1 = StructType([ \
        StructField("custid", IntegerType(), True), \
        StructField("custfname", StringType(), True), \
        StructField("custlname", StringType(), True), \
        StructField("custage", StringType(), True), \
        StructField("custprofession", StringType(), True), \
        ])
    
    df = spark \
      .readStream \
      .format("csv") \
      .option("header", "true") \
      .option("inferSchema", True) \
      .option("maxFilesPerTrigger", 1) \
      .option("checkpointLocation", "/checkpoint") \
      .schema(schema1) \
      .load("/stream/")
      
    
    df2=df.groupBy("custprofession").agg(avg("custage").alias("avg_age"), count("custid").alias("customer_count"))
    
    stream_data=df2 \
    .writeStream \
    .format("console") \
    .outputMode("complete") \
    .trigger(processingTime="10 seconds") \
    .start()
    
    
    stream_data.awaitTermination()





if __name__ == '__main__':
    stream()