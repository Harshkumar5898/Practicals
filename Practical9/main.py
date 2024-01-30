f = open("Answer.txt", "r")

vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vcount = 0
ccount = 0
data = f.read()
for i in data:
    if i.isalpha():
        if i in vowel:
            vcount+=1
        else:
            ccount+=1

print("Number of vowels :",vcount)
print("Number of consonants :",ccount)