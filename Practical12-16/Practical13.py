# WAP to append students records to binary file “Stu.dat” by getting data from user as long as user want.

import pickle

f = open("Stu.dat", "ab")

n = int(input("Number of student data you want to enter :"))
data = dict()

for i in range(n):
    print("Enter student", i + 1, "information")
    data["Rollno"] = int(input("Enter roll no. :"))
    data["Name"] = input("Enter name :")
    data["Marks"] = float(input("Enter marks :"))
    pickle.dump(data, f)
    print()

f.close()