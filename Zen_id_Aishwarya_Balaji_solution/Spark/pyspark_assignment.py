# Step 1. upload your dataset to GCP  -> copy to your cluster -> unzip the file -> you will get a json
#    a) hadoop fs -put <file path> <hdfs path>

# Soln:
# Uploaded to GCP storage bucket as .zip and unzipped using 
# unzip 'archive (4).zip' (in linux)


#Step 2: create a spark program or use pyspark repl 
from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number
from pyspark.sql.window import WindowSpec, Window
import os

def spark_test():
    spark = SparkSession.builder.appName("Papers").getOrCreate()
    #23/10/22 05:29:39 WARN SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.
    sc = spark.sparkContext
    sc.setLogLevel("Error")

    #Step 3: load the json file into DF , infer the schema , drop malformed records [baisc data preprocessing.
    os.system('hadoop fs -put /home/dell/datasets/arxiv-metadata-oai-snapshot.json /tmp/')
    dfjson = spark.read.format("json").option("mode", "dropmalformed").option("header", "true").option("inferSchema", True).load("/tmp/arxiv-metadata-oai-snapshot.json")
    dfjson.printSchema()
    dfjson.show(10,False)

    #Step 4: if any column contains null , drop the records. 
    df_no_null = dfjson.na.drop()

    #Step 5: finally get the count of authers. 
    count_of_authors = df_no_null.select(col("authors")).count()
    print(count_of_authors)

    #Step 6: new dataframe = get the uniq authers , his titles, catagories , abstract
    new_df = df_no_null.select(col("authors"), col("title"), col("categories"), col("abstract")).distinct()

    #Step 7: save above dataframe into a hive table "authers.df_name"
    new_df.write.mode('overwrite').saveAsTable('authors.new_df')

    #Step 8: convert above arrays to columns , finally map each element to the author 
    version_df = df_no_null.select("authors", "versions.version")

    #Step 9: save the exploded information into a parquer file. in hdfs. 
    version_df.write.mode('overwrite').parquet("hdfs:///result/author_and_versions")

if __name__ == '__main__':
    spark_test()