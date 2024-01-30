def myFun(myList):
    print("\tInside myFun()")
    print("\tlist received in function :", myList)
    myList[0]= 100
    print("\tlist after changes :", myList)

list = eval(input("Enter a list :"))
print("list received :",list)
myFun(list)
print("list after function :",list)