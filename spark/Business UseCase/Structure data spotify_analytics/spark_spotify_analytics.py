from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number
from pyspark.sql.window import WindowSpec, Window
import os

def spark_test():
    spark = SparkSession.builder.appName("spotify").getOrCreate()
    sc = spark.sparkContext

    sc.setLogLevel("Error")

    print("Dataframe reader:")

    #dfcsv1 = spark.read.format("csv").option("mode", "dropmalformed").option("header", "true").option("inferSchema", True).load("D:\\Guvi\\CSV\\spotify-2023.csv")
    os.system('hadoop fs -put /home/Raj/data/spotify-2023.csv /tmp/')
    dfcsv1 = spark.read.format("csv").option("mode", "dropmalformed").option("header", "true").option("inferSchema", True).load("/tmp/spotify-2023.csv")

    dfcsv1.printSchema()

    dfcsv1.show(10,False)

    print(dfcsv1.rdd.getNumPartitions())

    dfcsv2 = dfcsv1.repartition(10)
    

    print("select specific rows.")
    dfcsv2.select(col("artist(s)_name"), col("track_name")).show()

    print("adding a constant column:")
    
    #dfcsv2 = dfcsv2.withColumn(new column , logic)

    dfcsv2 = dfcsv2.withColumn("source",lit("spotify 2023"))

    dfcsv2.printSchema()
    dfcsv2.show(10,False)

    print("renaming existing columns")

    dfcsv3 = dfcsv2.withColumnRenamed("danceability_%","danceability") \
    .withColumnRenamed("valence_%","valence")\
    .withColumnRenamed("energy_%","energy")\
    .withColumnRenamed("acousticness_%","acousticness") \
    .withColumnRenamed("instrumentalness_%", "instrumentalness") \
    .withColumnRenamed("liveness_%", "liveness") \
    .withColumnRenamed("speechiness_%", "peechiness") \
    .withColumnRenamed("artist(s)_name", "artist_name")

    dfcsv3.show()

    print("no of songs by each artist")

    df_top_artist=dfcsv3.groupBy("artist_name").count()
    df_top_artist.show(20,False)

    print("top tracks of each year")
    
    #select t.*
    #from 
    #(select release_year, track_name , row_number() over(partition by release_year order by steams desc) as rnum from table1)t 
    #where t.rnum=1;
     
    
    WindowSpec = Window.partitionBy("released_year").orderBy(col("streams").desc())

    top_streams_df = dfcsv3.withColumn("rnum", row_number().over(WindowSpec))\
        .select(col("released_year"),col("track_name"),col("artist_name"),col("streams")).where(col("rnum") == 1)

    top_streams_df.show(20,False)

    print("dataframe writer")
    top_streams_df.write.mode('overwrite').parquet("hdfs:///result/top_streams_df")
    #top_streams_df.write.option("header", True).mode('overwrite') \
    #    .csv("D:\\Guvi\\CSV\\Result\\top_streams_df")

    

if __name__ == '__main__':
    spark_test()