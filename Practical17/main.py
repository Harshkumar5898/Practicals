# WAP to create a CSV file to store students data ( Roll number , name and marks) obtain data from user and write 5 records into the file. 

import csv

f = open("sturec.csv","w",newline="")
fw = csv.writer(f)
data = ["Rollno","Name","Marks"]
fw.writerow(data)
for i in range(5):
    data[0]= int(input("Enter student rollno :"))
    data[1] = input("Enter name :")
    data[2] = int(input("Enter marks :"))

    fw.writerow(data)

f.close()