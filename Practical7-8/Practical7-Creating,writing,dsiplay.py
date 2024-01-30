f = open("Marks.txt", "w")

n = int(input("Number of students in the class :"))
for i in range(n):
    rollno = input("Enter roll no. of student :")
    name = input("Enter student name :")
    marks = input("Enter student marks :")
    data = rollno + "," + name + "," + marks + "\n"
    f.write(data)

f.close()

f = open("Marks.txt","r")
print("RollNo   Name    Marks")
for i in f:
    data = i.split(",")
    print(data[0],"\t",data[1],"\t",data[2])
f.close()