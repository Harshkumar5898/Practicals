# WAP to display contents of file “Stu.dat” on the Screen.

import pickle

f = open("stu.dat", "rb")

print("Rollno \t Name \t Marks")
try:
    while True:
        data = pickle.load(f)
        print(data["Rollno"], "\t", data["Name"], "\t", data["Marks"])

except EOFError:
    f.close()

# Rollno   Name    Marks
# 1        harsh   95.0
# 2        vinit   97.0
# 3        mitul   98.0
# 4        saif    99.0