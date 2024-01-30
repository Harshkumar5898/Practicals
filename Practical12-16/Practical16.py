# 16. 	WAP to update the records of the file “Stu.dat” so that those who have scored more than 81.0 , get additional bonus marks of 1. And display the records of file which modified.

import pickle

f = open("stu.dat", "+rb")
f.seek(0)
try:
    while True:
        pos = f.tell()
        data = pickle.load(f)
        if data["Marks"] > 81:
            f.seek(pos)
            data["Marks"] += 1
            pickle.dump(data, f)

except EOFError:
    f.close()

f = open("stu.dat", "rb")

try:
    while True:
        data = pickle.load(f)
        print(data)

except EOFError:
    f.close()
