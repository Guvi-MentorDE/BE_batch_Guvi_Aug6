from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import*
from pyspark.sql.functions import col,lit,udf,min,max,concat,column,row_number,avg,count
from pyspark.sql.window import WindowSpec,Window
from pyspark.sql.functions import count
import os


spark = SparkSession.builder.appName("Json_test").getOrCreate()

sc =spark.sparkContext
sc.setLogLevel("Error")
df = spark.read.json("gs://jsonfileda/arxiv-metadata-oai-snapshot.json")
df.printSchema()

df.show(10,False)


dfj=spark.read.format("json").option("mode","dropmalformed").option("header","true").option("inferSchema",True)
print("Dataframe reader:")

dfj=spark.read.format("json").option("mode","dropmalformed").option("header","true").option("inferSchema",True)
 
os.system('hadoop fs -put /home/Shashidhar/data/arxiv-metadata-oai-snapshot.json /tmp/')

dfj=spark.read.format("json").option("mode","dropmalformed").option("header","true").option("inferSchema",True).load("/tmp/arxiv-metadata-oai-snapshot.json")
dfj.printSchema()

print(dfj.rdd.getNumPartitions())
dfj.dropna().show(truncate=False)
dfj.count()
 
dfj.select(count(dfj.authors)).show()

dfj.select(count("authors")).show()
dfj.groupBy("authors").count().show()

WindowSpec = Window.partitionBy("authors").orderBy(col("catagories").desc())
new_df = dfj.select(col("authors"),col("titles"),col("catagories"),col("abstract")).withColumn("row_number",row_number().over(windowspec))

