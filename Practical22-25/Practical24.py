import mysql.connector
db = mysql.connector.connect(host="localhost",user="root", passwd="harsh@5898",database="school")
cursor = db.cursor()

roll = int(input("Enter student roll no which to be deleted : "))
qry = "delete from kvstudents where roll_no = %s"
value = (roll,)
cursor.execute(qry,value)
db.commit()

print("Student data deleted.")