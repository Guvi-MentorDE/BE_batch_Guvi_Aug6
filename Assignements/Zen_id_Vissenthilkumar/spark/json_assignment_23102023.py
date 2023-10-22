from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window

def spark_json_implementation():
    spark = SparkSession.Builder().appName(name='Test').getOrCreate()
    # Create a sample DataFrame
    df = spark.read.option('mode','DROPMALFORMED').json("gs://mystorage_demo/arxiv-metadata-oai-snapshot.json")
    
    print('Autors counts :',df.select("authors").count())
    df.repartition(20)
    df_null_dropped = df.na.drop()
    df.repartition(20)
    new_data = df_null_dropped.select(col("authors"),col("title"),col("categories"),col("abstract")).distinct()
    new_data.show(10)
    new_data.write.mode('overwrite').saveAsTable("sparkdemo.arxiv_snapshot")
    new_data.createOrReplaceTempView("temp_table")
    spark.sql(""" select * from temp_table""").show(30,False)


if __name__ == '__main__':
  spark_json_implementation()