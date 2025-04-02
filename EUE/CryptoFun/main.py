
f = open("EUE/CryptoFun/ciphertext1.txt", "r")
textblock = f.readlines()

alph = "abcdefghijklmnopqrstuvwxyz"
excludedChars = ["!", " ", "\n", "’", "”", ".", ","]

text = ""
for line in textblock:
    line = line.strip("\n")
    text += line.lower()


letters = {}

for character in text:
    if character in letters.keys():
        letters[character] += 1
    else:
        letters.update({character: 1})
letters.pop(" ")
x = 0
for key in letters.keys():
    if letters[key] > x:
        x = letters[key]
        mostCommon = key

x = alph.index(mostCommon)
y = alph.index("e")
z = (x-y)%26
print(z)

processString = ""
run = True
for character in textblock:
    i = 0
    while run:
        if character in excludedChars:
            processString += character
            run = False
        elif character == alph[i % 26]:
            processString += alph[(i + z) % 26]
            run = False

        i += 1
    print(alph[i % 26])
    run = True
print(processString)