import mysql.connector
db = mysql.connector.connect(host="localhost",user="root", passwd="harsh@5898",database="school")
cursor = db.cursor()

cursor.execute("create table kvstudents(roll_no int primary key, name varchar(20),fees float(7,2))")

print("Table created successfully")