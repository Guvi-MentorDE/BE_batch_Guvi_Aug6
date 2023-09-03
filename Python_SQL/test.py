import mysql.connector
db="noob_db"
db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database=db)
cursor_db=db_connection.cursor()
cursor_db.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
print("table created if not exists")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    #val = [("John", "London"),("Ramesh", "India")]
val = ("Ram", "London")
cursor_db.execute(sql, val)
db_connection.commit()
cursor_db.close()
db_connection.close()
