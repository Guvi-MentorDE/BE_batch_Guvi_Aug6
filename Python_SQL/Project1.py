import mysql.connector
import csv 

db="noob_db"
global db_connection
db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database=db)
cursor_db=db_connection.cursor()
cursor_db.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql ='''DROP TABLE IF EXISTS `test1`; CREATE TABLE IF NOT EXISTS test1 (policyID int, statecode varchar(255), county varchar(255))'''
cursor_db.execute(sql)
cursor_db.close()


with open('D:/Guvi/dataset/sample2.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database=db)
    cursor_db=db_connection.cursor()
    for row in reader:
        print(row)  
        a,b,c=row['policyID'],row['statecode'],row['country']
        #print(a,b,c)
        sql = "INSERT INTO test1(policyID ,statecode,county) VALUES (%s,%s,%s)"
        #cursor_db.execute(sql, [(row['policyID'], row['statecode'], row['country'])])
        cursor_db.execute(sql, [a,b,c])
        
    db_connection.commit()
    #cursor_db.close()
    #db_connection.close()
        
         #print(row['policyID'], row['statecode'], row['county'])
#cursor_db.close()
#db_connection.close()

query = "SELECT * FROM test1"
cursor_db.execute(query)

myresult = cursor_db.fetchall()
 
for x in myresult:
    print(x)
    
#cursor_db.execute("drop table customers;")
db_connection.commit()
cursor_db.close()
db_connection.close()