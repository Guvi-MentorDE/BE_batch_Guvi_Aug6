import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host="localhost", database = 'noob_db',user="root", passwd="root",use_pure=True)
    query = "Select * from test1;"
    result_dataFrame = pd.read_sql(query,mydb)
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))