from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
#from pyspark.sql.types import StructType
import os
from pyspark.sql.functions import col, lit, udf, min, max, concat, column


def cust_details(files):
    spark = SparkSession.builder.appName("cust_details1").getOrCreate()
    sc = spark.sparkContext

    sc.setLogLevel("Error")  # unc   /ALL/Error/WARN/INFO
    emp_RDD = sc.emptyRDD()
    columns = StructType([])

    emp_RDD1 = sc.emptyRDD()
    columns1 = StructType([])
    #df_union=spark.createDataFrame(data = emp_RDD,schema=columns)
    #df_union_err=spark.createDataFrame(data = emp_RDD1,schema=columns1)
    print("Looping starts")
    for i in range(len(files)):
        os.system("hadoop fs -put /home/ramshankarcse/spark_datasets/"+files[i]+" /tmp/")  #change this to your location 
    rdd = sc.textFile("/tmp/*.txt") # default =4 parttions  #change this to your location 

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

    #df_union=df_union.union(filtered_rdd)
    #df_union_err=df_union_err.union(filtered_error_lines)

    print("save")

    
    #os.system('hadoop fs -rm -r /result/errored_cust_records.txt') 
    os.system('hadoop fs -rm -r /result1')
    os.system('hadoop fs -mkdir /result1')
    filtered_error_lines.saveAsTextFile("hdfs:///result/errored_cust_records") 
    filtered_rdd.saveAsTextFile("hdfs:///result/total_cust_new") 
    #filtered_error_lines.saveAsTextFile("hdfs:///result/filtered_error_lines") 


if __name__ == '__main__':
    '''print("Enter the number of files:")
    num_files=input()
    file_list=[]
    for i in num_files:
        print("Enter the file name:")
        file_name=input()
        file_list.append(file_name)'''
    file_list=['custs.txt','custs2.txt','custs3.txt']
    cust_details(file_list)
