from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window
import os
import os
import sys

def top_artist():
    spark = SparkSession.builder.appName("authors_json_dynamic").getOrCreate()
    sc = spark.sparkContext
    input_spotify=spark.read.option("header","true").option("inferSchema","true").csv("gs://ramshankar_gcs_bucket/spotify-2023.csv")
    input_year=input_spotify.withColumn("year",lit("spotify 2023"))

    input_col_rename=input_year.withColumnRenamed("artist(s)_name","artist_name").withColumnRenamed("danceability_%","danceability").withColumnRenamed("valence_%","valence").withColumnRenamed("energy_%","energy").withColumnRenamed("acousticness_%","acousticness").withColumnRenamed("instrumentalness_%","instrumentalness").withColumnRenamed("liveness_%","liveness").withColumnRenamed("speechiness_%","speechiness")

    author_track_count=input_col_rename.groupBy("artist_name").count()
    author_track_count.write.format("parquet").saveAsTable("authors.track_count1")

    WindowSpec = Window.partitionBy("released_year").orderBy(col("streams").desc())

    top_artist = input_col_rename.withColumn("rownum", row_number().over(WindowSpec)).filter(col("rownum") == 1)
    top_artist.write.format("parquet").saveAsTable("authors.top_artist1")

if __name__=='__main__':
        top_artist()
  
