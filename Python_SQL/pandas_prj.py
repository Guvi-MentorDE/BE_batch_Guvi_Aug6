import mysql.connector as connection
import pandas as pd
#python -m pip install sqlalchemy
try:
    mydb = connection.connect(host="localhost", database = 'pysql',user="root", passwd="root",use_pure=True)
    query = "Select * from orders;"
    result_dataFrame = pd.read_sql(query,mydb)
    df1=result_dataFrame.query("country == 'USA'")
    print(df1)
    #df2=result_dataFrame.query("country == 'US'",inplace=True)
    df3=result_dataFrame.apply(lambda row: row[result_dataFrame['country'].isin(['USA','UK'])])
    print(df3)
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))