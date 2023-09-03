import mysql.connector
import csv 

def connect_db(db):
    db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database=db)
    cursor_db=db_connection.cursor()
    return cursor_db,db_connection

def execute_ddl(cursor_db):
    print(execute_ddl)
    cursor_db.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    sql ='''CREATE TABLE IF NOT EXISTS policy (policyID int, statecode varchar(255), country varchar(255))'''
    cursor_db.execute(sql)
    cursor_db.close()

def csv_read(cursor_db,db_connection):
    print(csv_read)
    
    with open('D:/Guvi/dataset/sample2.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database=db)
        cursor_db=db_connection.cursor()
        for row in reader:
            print(row)  
            a,b,c=row['policyID'],row['statecode'],row['country']
            #print(a,b,c)
            sql = "INSERT INTO policy(policyID ,statecode,country) VALUES (%s,%s,%s)"
            cursor_db.execute(sql, [a,b,c])
        
        
        db_connection.commit()

def select_result(cursor_db,db_connection):
    query = "SELECT * FROM policy"
    cursor_db.execute(query)
    myresult = cursor_db.fetchall()
    for x in myresult:
        print(x)
    close_connection(cursor_db,db_connection)
        

def close_connection(cursor_db,db_connection):
    db_connection.commit()
    cursor_db.close()
    db_connection.close()


if __name__ == "__main__":
    db='noob_db'
    cursor_db,db_connection=connect_db(db)
    execute_ddl(cursor_db)
    cursor_db,db_connection=connect_db(db)
    csv_read(cursor_db,db_connection)
    select_result(cursor_db,db_connection)