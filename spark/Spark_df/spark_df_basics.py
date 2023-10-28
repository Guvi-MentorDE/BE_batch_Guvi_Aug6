from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window
import os
import os
import sys


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
def spark_test():
    spark = SparkSession.builder.appName("spark_test").getOrCreate()
    sc = spark.sparkContext

    sc.setLogLevel("Error")

    #filerdd = sc.textFile("D:\\Spark\\custs.txt")
    #filerdd.take(10)
    #os.system('hadoop fs -put /home/Raj/data/dedata/custs.txt /tmp/')  #change this to your location 
    filerdd = sc.textFile("gs://dedata/custs.txt") # default =4 parttions  #change this to your location 

    rdd1 = filerdd.map(lambda l: l.split(",")).filter(lambda x: len(x) == 5)
    rdd = rdd1.map(lambda l: Row(custid=int(l[0].strip()), custfname=l[1], custlname=l[2], custage=l[3], custprofession=l[4]))
    

    schema1 = StructType([ \
        StructField("custid", IntegerType(), True), \
        StructField("custfname", StringType(), True), \
        StructField("custlname", StringType(), True), \
        StructField("custage", StringType(), True), \
        StructField("custprofession", StringType(), True), \
        ])
    
    print("converting an RDD to DataFrame")
    filedf = spark.createDataFrame(rdd, schema1)

    print("display sample of 20 records")
    filedf.show()

    print("displace the schema of the DF")
    filedf.printSchema()

    result=filedf.select("*").filter("custprofession='Pilot' and custage > 35")
    
    result.coalesce(1).write.mode('overwrite').parquet("hdfs:///result/cust_result")
    

if __name__ == '__main__':
    spark_test()