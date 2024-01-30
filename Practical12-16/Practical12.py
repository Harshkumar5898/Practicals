# 12.	WAP to get students data ( roll number , names  and marks) from user and write onto a binary file “Stu.dat” as long as user want.

import pickle

f = open("Stu.dat", "wb")

n = int(input("Number of student in class :"))
data = dict()

for i in range(n):
    print("Enter student", i + 1, "information")
    data["Rollno"] = int(input("Enter roll no. :"))
    data["Name"] = input("Enter name :")
    data["Marks"] = float(input("Enter marks :"))
    print()

    pickle.dump(data, f)

f.close()

f = open("stu.dat", "rb")

print("Rollno \t Name \t Marks")
try:
    while True:
        data = pickle.load(f)
        print(data["Rollno"], "\t", data["Name"], "\t", data["Marks"])

except EOFError:
    f.close()
