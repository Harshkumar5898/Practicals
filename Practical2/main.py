def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = eval(input("Enter your list:"))
print("list recived:", list)
bubbleSort(list)
print("list after bubble sort:", list)
