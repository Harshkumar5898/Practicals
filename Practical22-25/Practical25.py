import mysql.connector
db = mysql.connector.connect(host="localhost",user="root", passwd="harsh@5898",database="school")
cursor = db.cursor()

roll = int(input("Enter roll no to be updated : "))
fees = float(input("Enter new fees : "))
qry = "update kvstudents set fees = %s where roll = %s"
values = (fees, roll)
cursor.execute(qry, values)
db.commit()

print("Student fees has been updated.")