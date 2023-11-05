from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number
import os
from pyspark.sql.functions import explode
from pyspark import SparkConf
from pyspark.sql import SparkSession, Row


def uniq_author():
    spark = SparkSession.builder.appName("authors_json_dynamic").getOrCreate()
    sc = spark.sparkContext
    print("Finding uniq author scenario")
    schema1=StructType([StructField("authors",StringType(),True),StructField("title",StringType(),True),StructField("categories",StringType(),True),StructField("abstract",StringType(),True),StructField("comments",StringType(),True)])
    input1=spark.read.json("gs://ramshankar_gcs_bucket/arxiv-metadata-oai-snapshot.json",schema1)
    input_clr=input1.dropna(subset=["comments"])
    input_clr.count()
    input_clr_dist=input_clr.select("authors","title","categories","abstract").distinct()
    input_clr_dist.write.saveAsTable("authors.unique_authors1")
    schema2=StructType([StructField("authors",StringType(),True),StructField("title",StringType(),True),StructField("categories",StringType(),True),StructField("abstract",StringType(),True),StructField("comments",StringType(),True),StructField("versions",ArrayType(StringType()),True),StructField("authors_parsed",ArrayType(StringType()),True)])
    input2=spark.read.json("gs://ramshankar_gcs_bucket/arxiv-metadata-oai-snapshot.json",schema2)
    input_clr=input2.dropna(subset=["comments"])
    input_flatten=input_clr.select(col("authors"),col("title"),col("categories"),col("abstract"),explode(input_clr.versions).alias("versions"),col("authors_parsed"))
    input_flat_auth_par=input_flatten.select("authors","versions",explode(input_flatten.authors_parsed).alias("auth_parsed"))
    input_flat_auth_par.show(10,False)
    input_flat_auth_par.write.parquet("/result3/authors_assignment")

if __name__=='__main__':
        uniq_author()
