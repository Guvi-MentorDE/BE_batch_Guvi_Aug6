from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
import os
from pyspark.sql.functions import col, lit, udf, min, max, concat, column


def cust_details():
    spark = SparkSession.builder.appName("cust_details").getOrCreate()
    sc = spark.sparkContext

    sc.setLogLevel("Error")  # unc   /ALL/Error/WARN/INFO
    os.system('hadoop fs -put /home/dell/datasets/cust*.txt /tmp/')  #change this to your location  
    rdd = sc.textFile('/tmp/' + 'cust*.txt') 

    lines = rdd.collect()

    print("""print all the elements or unto certain limit from the RDD""")
    lines = rdd.collect()
    lines_count = rdd.count()
    print("no of lines from the source :", lines_count)
    count = 0
    for l in lines:
        if count <= 10:
            print(l)
        else:
            break
        count = count + 1

    print(""" accessing specific index from RDD""")
    temp_rdd = rdd.map(lambda x: x.split(',')).map(lambda l: Row(l[0], l[1]))
    print(temp_rdd.take(10))

    print(""" Data Preprocessing acticity : cleaning of bad records """)
    filtered_rdd = rdd.map(lambda x: x.split(',')).filter(lambda x: len(x) == 5)
    filtered_rdd_count = filtered_rdd.count()
    print("filtered lines count:", filtered_rdd_count)

    print(""" Data Preprocessing acticity : get the list of bad records """)
    filtered_error_lines = rdd.map(lambda x: x.split(',')).filter(lambda x: len(x) < 5)
    filtered_error_count = filtered_error_lines.count()
    print("filtered lines count:", filtered_error_count)


    print("get unique professions")
    unique_professions= filtered_rdd.map(lambda x:x[4]).distinct().count()
    print("unique_professions=", unique_professions)

    print(" count by profesion")
    count_by_profession = filtered_rdd.map( lambda  x: (x[4],x[1])).countByKey()
    print("count by employee profession=",count_by_profession)


    print("verify the parititions count=")
    print(filtered_rdd.getNumPartitions())
    total_cust_new = filtered_rdd.repartition(20)
    print(total_cust_new.getNumPartitions())

    print("save")

    
    #os.system('hadoop fs -rm -r /result/errored_cust_records.txt')
    os.system('hadoop fs -rm -r /result')
    os.system('hadoop fs -mkdir /result')
    filtered_error_lines.saveAsTextFile("hdfs:///result/errored_cust_records") 
    total_cust_new.saveAsTextFile("hdfs:///result/total_cust_new") 
    filtered_error_lines.saveAsTextFile("hdfs:///result/filtered_error_lines") 


if __name__ == '__main__':
    cust_details()