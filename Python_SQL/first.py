import mysql.connector

def connect_db():
    db="noob_db"
    global db_connection
    db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database=db)
    return db_connection

def main(db_connection):
    cursor_db=db_connection.cursor()
    cursor_db.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    print("table created if not exists")
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [("John", "London"),("Ramesh", "India")]
    #val = ("Ram", "London")
    for i in val:
        cursor_db.execute(sql, i)
    db_connection.commit()
    return db_connection,cursor_db

def display(db_connection,cursor_db):
    query = "SELECT id, name, address FROM customers"
    cursor_db.execute(query)

    myresult = cursor_db.fetchall()
 
    for x in myresult:
        print(x)
    
    #cursor_db.execute("drop table customers;")
    db_connection.commit()
    cursor_db.close()
    db_connection.close()
 
if __name__ == "__main__":
    db_connection=connect_db()
    db_connection,cursor_db=main(db_connection)
    display(db_connection,cursor_db)