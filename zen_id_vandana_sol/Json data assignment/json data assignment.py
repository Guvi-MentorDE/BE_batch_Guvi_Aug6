df = spark.read.json("gs://sparkstreaming/arxiv-metadata-oai-snapshot.json")
>>> df.printSchema()
root
 |-- abstract: string (nullable = true)
 |-- authors: string (nullable = true)
 |-- authors_parsed: array (nullable = true)
 |    |-- element: array (containsNull = true)
 |    |    |-- element: string (containsNull = true)
 |-- categories: string (nullable = true)
 |-- comments: string (nullable = true)
 |-- doi: string (nullable = true)
 |-- id: string (nullable = true)
 |-- journal-ref: string (nullable = true)
 |-- license: string (nullable = true)
 |-- report-no: string (nullable = true)
 |-- submitter: string (nullable = true)
 |-- title: string (nullable = true)
 |-- update_date: string (nullable = true)
 |-- versions: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- created: string (nullable = true)
 |    |    |-- version: string (nullable = true)

>>> print(df.rdd.getNumPartitions())
25
>>> Schema = StructType([
...     StructField('authors', StringType(), True),
...     StructField('categories', StringType(), True),
...     StructField('license', StringType(), True),
...     StructField('comments', StringType(), True),
...     StructField('abstract', StringType(), True),
...     StructField('versions', ArrayType(StringType()), True),
... ])
>>> df1 = spark.read.json("gs://sparkstreaming/arxiv-metadata-oai-snapshot.json", schema=Schema)
>>> df1.filter(df1.comments.isNull()).show()
+--------------------+--------------------+-------+--------+--------------------+--------------------+
|             authors|          categories|license|comments|            abstract|            versions|
+--------------------+--------------------+-------+--------+--------------------+--------------------+
|Wael Abu-Shammala...|     math.CA math.FA|   null|    null|  In this paper w...|[{"version":"v1",...|
|Paul Harvey, Brun...|            astro-ph|   null|    null|  We discuss the ...|[{"version":"v1",...|
|         Dohoon Choi|             math.NT|   null|    null|  Recently, Bruin...|[{"version":"v1",...|
|Dohoon Choi and Y...|             math.NT|   null|    null|  Serre obtained ...|[{"version":"v1",...|
|Zhan Shu, Xiao-Li...|              hep-ph|   null|    null|  In $\XQM$, a qu...|[{"version":"v1",...|
|Wael Abu-Shammala...|     math.CA math.FA|   null|    null|  In this paper w...|[{"version":"v1",...|
|     Frank J. Tipler|      physics.pop-ph|   null|    null|  I shall present...|[{"version":"v1",...|
|Rastislav \v{S}r\...|               cs.DS|   null|    null|  In this paper, ...|[{"version":"v1",...|
|   Somnath Choudhury|              hep-ph|   null|    null|  Neutrinoless do...|[{"version":"v1",...|
|Lawrence H. Friedman|   cond-mat.mtrl-sci|   null|    null|  Epitaxial self-...|[{"version":"v1",...|
|J. Y. Abuhlail, S...|             math.RA|   null|    null|  This paper is a...|[{"version":"v1",...|
|Duong Minh Duc an...|             math.DG|   null|    null|  Our main result...|[{"version":"v1",...|
|       Lester Ingber|cs.CE cond-mat.st...|   null|    null|  Real Options fo...|[{"version":"v1",...|
|Daniele Fausti, T...|cond-mat.str-el c...|   null|    null|  The sequence of...|[{"version":"v1",...|
|H. Takenaka and D...|   cond-mat.mtrl-sci|   null|    null|  We investigate ...|[{"version":"v1",...|
|W. Kuch, F. Offi,...|   cond-mat.mtrl-sci|   null|    null|  We present an x...|[{"version":"v1",...|
|G. Dereli and B. ...|   cond-mat.mtrl-sci|   null|    null|  This paper exam...|[{"version":"v1",...|
|   Martin Schumacher|      hep-ph nucl-ex|   null|    null|  The electromagn...|[{"version":"v1",...|
|Andrew Dancer, Mc...|             math.DG|   null|    null|  We extend our p...|[{"version":"v1",...|
|Daniela K\"uhn an...|             math.CO|   null|    null|  The minimum sem...|[{"version":"v1",...|
+--------------------+--------------------+-------+--------+--------------------+--------------------+
only showing top 20 rows

>>> print("dropping the records containing null values")
dropping the records containing null values
>>> df2 = df1.dropna(subset=["comments"])
>>> print("replace null values with unknown keyword")
replace null values with unknown keyword
>>> df3 = df2.fillna(value="unknown", subset=["license"])
>>> df3.show()
+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
|             authors|          categories|             license|            comments|            abstract|            versions|
+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
|C. Bal\'azs, E. L...|              hep-ph|             unknown|37 pages, 15 figu...|  A fully differe...|[{"version":"v1",...|
|Ileana Streinu an...|       math.CO cs.CG|http://arxiv.org/...|To appear in Grap...|  We describe a n...|[{"version":"v1",...|
|         Hongjun Pan|      physics.gen-ph|             unknown| 23 pages, 3 figures|  The evolution o...|[{"version":"v1",...|
|        David Callan|             math.CO|             unknown|            11 pages|  We show that a ...|[{"version":"v1",...|
|Y. H. Pong and C....|   cond-mat.mes-hall|             unknown|6 pages, 4 figure...|  We study the tw...|[{"version":"v1",...|
|Alejandro Corichi...|               gr-qc|             unknown|16 pages, no figu...|  A rather non-st...|[{"version":"v1",...|
|     Damian C. Swift|   cond-mat.mtrl-sci|http://arxiv.org/...|   Minor corrections|  A general formu...|[{"version":"v1",...|
|  Sergei Ovchinnikov|             math.CO|             unknown|36 pages, 17 figures|  Partial cubes a...|[{"version":"v1",...|
|Clifton Cunningha...|     math.NT math.AG|http://arxiv.org/...|14 pages; title c...|  In this paper w...|[{"version":"v1",...|
|        Koichi Fujii|     math.CA math.AT|             unknown|  18 pages, 1 figure|  In this article...|[{"version":"v1",...|
|     Christian Stahn|              hep-th|             unknown|22 pages; signs a...|  The pure spinor...|[{"version":"v1",...|
|Chao-Hsi Chang, T...|              hep-ph|             unknown|17 pages, 3 figur...|  In this work, w...|[{"version":"v1",...|
|Nceba Mhlahlo, Da...|            astro-ph|             unknown|10 pages, 11 figu...|  Results from sp...|[{"version":"v1",...|
|  Andreas Gustavsson|              hep-th|             unknown|20 pages, v2: an ...|  We give a presc...|[{"version":"v1",...|
|         Norio Konno|     math.PR math.AG|             unknown|6 pages, Journal-...|  In this note we...|[{"version":"v1",...|
|The BABAR Collabo...|              hep-ex|             unknown|21 pages, 13 post...|  The shape of th...|[{"version":"v1",...|
|Vanessa Casagrand...|nlin.PS physics.c...|             unknown|  5 pages, 4 figures|  Spatiotemporal ...|[{"version":"v1",...|
|Simon J.A. Malham...|             math.NA|             unknown| 20 pages, 4 figures|  We present Lie ...|[{"version":"v1",...|
|M. A. Loukitcheva...|            astro-ph|             unknown|4 pages, 2 figure...|  The very nature...|[{"version":"v1",...|
|A.A. Serga, M. Ko...|             nlin.PS|             unknown|First appeared in...|  The formation o...|[{"version":"v1",...|
+--------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
only showing top 20 rows

df3.select(col("versions")).show(1, False)
+-----------------------------------------------------------------------------------------------------------------------+
|versions                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------+
|[{"version":"v1","created":"Mon, 2 Apr 2007 19:18:42 GMT"}, {"version":"v2","created":"Tue, 24 Jul 2007 20:10:27 GMT"}]|
+-----------------------------------------------------------------------------------------------------------------------+
only showing top 1 row

>>> print("flatten a json df")
flatten a json df
>>> flatten_df = df3.select(df3.authors, explode(df3.versions))
>>> flatten_df.show(truncate=False)
+-------------------------------------------------------+----------------------------------------------------------+
|authors                                                |col                                                       |
+-------------------------------------------------------+----------------------------------------------------------+
|C. Bal\'azs, E. L. Berger, P. M. Nadolsky, C.-P. Yuan  |{"version":"v1","created":"Mon, 2 Apr 2007 19:18:42 GMT"} |
|C. Bal\'azs, E. L. Berger, P. M. Nadolsky, C.-P. Yuan  |{"version":"v2","created":"Tue, 24 Jul 2007 20:10:27 GMT"}|
|Ileana Streinu and Louis Theran                        |{"version":"v1","created":"Sat, 31 Mar 2007 02:26:18 GMT"}|
|Ileana Streinu and Louis Theran                        |{"version":"v2","created":"Sat, 13 Dec 2008 17:26:00 GMT"}|
|Hongjun Pan                                            |{"version":"v1","created":"Sun, 1 Apr 2007 20:46:54 GMT"} |
|Hongjun Pan                                            |{"version":"v2","created":"Sat, 8 Dec 2007 23:47:24 GMT"} |
|Hongjun Pan                                            |{"version":"v3","created":"Sun, 13 Jan 2008 00:36:28 GMT"}|
|David Callan                                           |{"version":"v1","created":"Sat, 31 Mar 2007 03:16:14 GMT"}|
|Y. H. Pong and C. K. Law                               |{"version":"v1","created":"Sat, 31 Mar 2007 04:24:59 GMT"}|
|Alejandro Corichi, Tatjana Vukasinac and Jose A. Zapata|{"version":"v1","created":"Sat, 31 Mar 2007 04:27:22 GMT"}|
|Alejandro Corichi, Tatjana Vukasinac and Jose A. Zapata|{"version":"v2","created":"Wed, 22 Aug 2007 22:42:11 GMT"}|
|Damian C. Swift                                        |{"version":"v1","created":"Sat, 31 Mar 2007 04:47:20 GMT"}|
|Damian C. Swift                                        |{"version":"v2","created":"Thu, 10 Apr 2008 08:42:28 GMT"}|
|Damian C. Swift                                        |{"version":"v3","created":"Tue, 1 Jul 2008 18:54:28 GMT"} |
|Sergei Ovchinnikov                                     |{"version":"v1","created":"Sat, 31 Mar 2007 05:10:16 GMT"}|
|Clifton Cunningham and Lassina Dembele                 |{"version":"v1","created":"Sat, 31 Mar 2007 05:32:49 GMT"}|
|Clifton Cunningham and Lassina Dembele                 |{"version":"v2","created":"Tue, 19 Aug 2008 04:46:47 GMT"}|
|Clifton Cunningham and Lassina Dembele                 |{"version":"v3","created":"Wed, 20 Aug 2008 13:15:09 GMT"}|
|Koichi Fujii                                           |{"version":"v1","created":"Sun, 1 Apr 2007 12:04:13 GMT"} |
|Christian Stahn                                        |{"version":"v1","created":"Mon, 2 Apr 2007 18:10:09 GMT"} |
+-------------------------------------------------------+----------------------------------------------------------+
only showing top 20 rows

flatten_df.write.mode('overwrite').parquet("hdfs:///result/flatten_author_versions")
>>> df3.createOrReplaceTempView("Archive")

>>> sql_query = """ SELECT distinct authors FROM Archive
...                 WHERE categories LIKE 'math%'
...                 """

>>> authers_list=spark.sql(sql_query)
>>> print(spark.sql(sql_query).count())
192065
>>> authers_list.write.mode('overwrite').parquet("hdfs:///result/authers_list")

