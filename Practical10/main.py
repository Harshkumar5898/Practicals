f = open("poem.txt", "r")

str = " "
size = 0
while str:
    str = f.readline()
    size = size + len(str.strip())
print("size", size)

f.close()
