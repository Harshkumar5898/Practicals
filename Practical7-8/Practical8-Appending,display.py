# f = open("Marks.txt","a")

# for i in range(2):
#     rollno = input("Enter roll no. of student :")
#     name = input("Enter student name :")
#     marks = input("Enter student marks :")
#     data = rollno + "," + name + "," + marks + "\n"
#     f.write(data)

# f.close()

f = open("Marks.txt","r")
print("RollNo   Name    Marks")
for i in f:
    data = i.split(",")
    print(data[0],"\t",data[1],"\t",data[2])
f.close()