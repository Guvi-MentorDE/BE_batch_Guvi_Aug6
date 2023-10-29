import os
from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window


def spark_test():
    spark = SparkSession.builder.appName("spark_test").getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("Error")
    os.system('hadoop fs -put /supdata/arxiv-metadata-oai-snapshot.json /tmp/')
    df = spark.read.format("json").option("mode", "dropmalformed").option("header", "true").option("inferSchema", True).load("/tmp/arxiv-metadata-oai-snapshot.json")
    df.printSchema()
    df.show(10,False)
    df3=df.repartition(30)
    print(df.rdd.getNumPartitions())
    df3.groupBy("authors").count().show()
    windowSpec  = Window.partitionBy("authors").orderBy("categories")
    df2=df3.select(col("authors"),col("title"),col("categories"),col("abstract")).withColumn("row_number",row_number().over(windowSpec))
    df2.show()
    df2.write.mode('overwrite').saveAsTable("authors.df2")
    df2.write.mode('overwrite').parquet("hdfs:///result/book_details")
    
    
    if __name__ == '__main__':
        spark_test()



    # schema=StructType().add("versions",ArrayType(StructType()\
    #                    .add("version",StringType(),True)\
    #                    .add("created",StringType(),True)))
    # df = spark.read.json(path="gs://supdata/arxiv-metadata-oai-snapshot.json", schema=schema, multiLine=True)

    # df1 = spark.read.json(path="gs://supdata/arxiv-metadata-oai-snapshot.json", multiLine=True)