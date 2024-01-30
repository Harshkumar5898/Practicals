# WAP to implement Stack Operations.( push() , pop() and display() ).

stack = []

while True:
    print("chose(1/2/3/4):\n\
          1) push item\n\
          2) pop item\n\
          3) display item\n\
          4) Exit")
    x = int(input())
    if x == 1:
        item = input("Enter item :")
        stack.append(item)
        print("item added!")
    elif x == 2:
        print("Item poped :",stack.pop())
    elif x ==3 :
        if stack:
            print("[")
            print(stack[-1],"<-- Top")
            for i in range(len(stack)-2,-1,-1):
                print(stack[i])
            print("]")
        else:
            print("Stack is empty")
    else:
        print("Exiting...")
        break
    print()