# WAP to search records for roll numbers as 12 or 14. If found then display the records. 

import pickle

f = open("stu.dat","rb")
search = [12,14]
found = False
try:
    while True:
        data = pickle.load(f)
        if data["Rollno"] in search:
            print(data)
            found = True

except EOFError:
    if not found:
        print("Data not found!")

    f.close()