def interest(p,r=10,t=2):
    return (p*r*t)/100

p = int(input("Enter principal amount :"))
r = int(input("Enter rate :"))
t = int(input("Enter time(year) :"))

print("Interest with defalut values =",interest(p))
print("Interest with given values =",interest(p,r,t))