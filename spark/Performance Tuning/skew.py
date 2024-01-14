
from pyspark import SparkConf
from pyspark.sql import SparkSession, Row
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, udf, min, max, concat, column, row_number, avg, count
from pyspark.sql.window import WindowSpec, Window
import os
import os
import sys
import numpy as np
import random

spark = SparkSession.builder.appName("spark_test").getOrCreate()
sc = spark.sparkContext

#### before applying salting : skew problem 
key_1 = ['a'] * 10
key_2 = ['b'] * 6000000
key_3 = ['c'] * 800
key_4 = ['d'] * 10000
keys = key_1 + key_2 + key_3 + key_4
random.shuffle(keys)


values_1 = list(np.random.randint(low = 1, high = 100, size = len(key_1)))
values_2 = list(np.random.randint(low = 1, high = 100, size = len(key_2)))
values_3 = list(np.random.randint(low = 1, high = 100, size = len(key_3)))
values_4 = list(np.random.randint(low = 1, high = 100, size = len(key_4)))
values = values_1 + values_2 + values_3 + values_4


pair_skew = list(zip(keys,values))
rdd = sc.parallelize(pair_skew, 8)
rdd.glom().collect()

grouped_rdd = rdd.groupByKey().cache()

grouped_rdd.map(lambda pair:(pair[0], [(i+10) for i in pair[1]])).count()


rdd_sort = rdd.sortByKey(ascending=False, numPartitions=4)
rdd_sort.count()


def salting(val):
    tmp = val + "_" + str(random.randint(0,5))
    return tmp


rdd_salting = rdd.map(lambda x: (salting(x[0]), x[1]))


# actual code
grouped_rdd = rdd_salting.groupByKey().cache()
# run a simple data transformation (using map()) on the skewed data
grouped_rdd.map(lambda pair:(pair[0], [(i+10) for i in pair[1]])).count()