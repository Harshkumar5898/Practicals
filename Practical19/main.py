# WAP to illustrate linear searching in an array. i
def linearSearch():
    for i in range(0,len(array)):
        if x == array[i]:
            return i
    return False

array = [1,2,3,4,5,6,7,8,9]

x = int(input("Enter search element :"))

found = linearSearch()

if not found:
    print("Element not found")
else :
    print("Element found at index :",found)