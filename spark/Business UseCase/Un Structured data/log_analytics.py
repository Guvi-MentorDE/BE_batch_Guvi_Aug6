from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number
from pyspark.sql.window import WindowSpec, Window
import os
from pyspark import StorageLevel
import re


def collect_words(line):
    return re.compile('\w+').findall(line.lower())


def get_repo(line):
    return re.compile(' \w+ ').findall(line.lower())


def log_analytics():
    spark = SparkSession.builder.appName("log analytics for unstructured data").getOrCreate()
    sc = spark.sparkContext

    sc.setLogLevel("Error")
    #os.system("hadoop fs -put /home/Raj/data/ghtorrent-logs.txt /tmp/")
    rdd = sc.textFile('gs://delog/ghtorrent-logs.txt')
    rdd = rdd.repartition(8)
    print(rdd.getNumPartitions())

    rdd.persist(StorageLevel.MEMORY_AND_DISK)
    #rdd.takeSample(False, 20)

    print(collect_words('we are TESTING GHTorrent! ?, OK!'))

    # get lines containing "transaction" and "repo"
    print("use case: print all the lines containing transaction , repo keywords")

    rdd_Transactions = rdd.filter(lambda line: "transaction" in collect_words(line)) 
    rdd_Repo = rdd.filter(lambda line: "repo" in collect_words(line))

    rdd_intersect = rdd_Transactions.intersection(rdd_Repo)
    rdd_intersect.count()

    rdd_intersect.collect()

    print(" finding the most commently used repo from the logs ")
    rdd2 = rdd.filter(lambda line: " repo " in get_repo(line))
    rdd3 = rdd2.map(lambda line: line.lower().split('repo')[1].split(' ')[1])
    rdd4 = rdd3.map(lambda repo: (repo, 1)).reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], ascending=False)
    rdd4.first()


if __name__ == '__main__':
    log_analytics()