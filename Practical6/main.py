import random

print("Loading dice simulation :-", end="\n\n")
ans = "y"
print("* Throwing dice")
while ans == "y":
    dice = random.randint(1, 6)
    print("You get:", dice, end="\n\n")
    ans = input("Do you want to throw the dice(y/n):")
