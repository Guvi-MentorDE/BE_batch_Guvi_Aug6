from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName('SparkByExamples.com') \
        .master("local[5]").getOrCreate()

# Create PySpark DataFrame
Data = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=Data, schema = schema)
df.show()

df.write.mode("overwrite").csv("/result/partition.csv")


# repartition by multiple column
df2 = df.repartition(2,"state")
print(df2.rdd.getNumPartitions())

df2.write.mode("overwrite").csv("/result/partition.csv")


# repartition() by number 
df3 = df.repartition(numPartitions=3)
print(df3.rdd.getNumPartitions())
df3.write.mode("overwrite").csv("/result/partition.csv")

#last option
df.write.mode("overwrite").partitionBy("state").csv("/result/partition.csv")