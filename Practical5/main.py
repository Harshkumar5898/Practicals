def encrypt(string, key):
    return key.join(string)

def decrypt(string, key):
    list = string.split(key)
    return "".join(list)

string = input("Enter the string :")
key = input("Enter the key :")

encString = encrypt(string, key)
decString = decrypt(encString, key)

print("Encrypted string :", encString)
print("Decrpted string :",decString)