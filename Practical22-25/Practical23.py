import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="harsh@5898", database="school"
)
cursor = db.cursor()

for i in range(5):
    roll = int(input("Enter roll no : "))
    name = input("Enter name of the student : ")
    fees = float(input("Enter fees of the student : "))
    qry = "insert into kvstudents values(%s,%s,%s)"
    values = (roll, name, fees)
    cursor.execute(qry, values)

db.commit()


print("\nstudents data\n")
cursor.execute("select * from kvstudents")
data = cursor.fetchall()
for i in data:
    print(i)