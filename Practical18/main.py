# WAP to create a CSV file “Employee.csv” by suppressing the EOL translation. And read and display the contents of the file.

import csv

f = open("Employee.csv", "w", newline="")
fw = csv.writer(f)
data = ["Code", "Name", "Salary"]
fw.writerow(data)
n = int(input("Number of employes :"))
for i in range(n):
    data[0] = int(input("Enter empcode :"))
    data[1] = input("Enter empName :")
    data[2] = int(input("Enter empSalary :"))
    fw.writerow(data)

f.close()

f = open("Employee.csv", "r")
fr = csv.reader(f)

for data in fr:
    print(data)

f.close()
