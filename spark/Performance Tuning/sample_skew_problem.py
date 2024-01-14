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

data_sample = [(1,4), (2,2), (2,1), (3,5), (2,5), (2,10), (2,7), (3,4), (2,1), (2,4), (4,4)]
rdd_sample = sc.parallelize(data_sample, 3)

rdd_sample.glom().collect()

rdd_sample_grouped = rdd_sample.groupByKey()

# show groupby results
for item in rdd_sample_grouped.collect():
    print(item[0], [value for value in item[1]])
    
# show partitions:
rdd_sample_grouped.glom().collect()