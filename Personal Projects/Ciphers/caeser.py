alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQTSTUVWXYZ"


print("Hello, welcome to the Caeser cipher encoder/decoder")
print("Enter 1 for encoding, enter 2 for decoding")
mode = int(input())

if mode == 1:
    print("~~~~~~~~~~~~~~~~~")
    print("ENCODING SELECTED")
    print("~~~~~~~~~~~~~~~~~")
elif mode == 2:
    print("~~~~~~~~~~~~~~~~~")
    print("DECODING SELECTED")
    print("~~~~~~~~~~~~~~~~~")
else:
    print("~~~~~~~~~~~~~~~~~")
    print("ENCODING SELECTED")
    print("~~~~~~~~~~~~~~~~~")
    mode = 1    
if mode == 1:
    string = input("Plaintext: ")
    shift = int(input("How much to shift by: "))

if mode == 2:
    string = input("Ciphertext: ")
    shift = int(input("How much to shift back by: "))


processString = ""
i = 26
run = True
if mode == 1:
    for thing in string:
        while run:
            if thing == " ":
                processString += " "
                run = False
            if thing == alphabet[i % 26]:
                processString += alphabet[(i + shift) % 26]
                run = False
            if thing == ALPHABET[i % 26]:
                processString += ALPHABET[(i + shift) % 26]
                run = False
            i += 1
            
        i = 0
        run = True
    print(processString)

if mode == 2:
    for thing in string:
        while run:
            if thing == " ":
                processString += " "
                run = False
            if thing == alphabet[i % 26]:
                processString += alphabet[(i - shift) % 26]
                run = False
            if thing == ALPHABET[i % 26]:
                processString += ALPHABET[(i - shift) % 26]
                run = False
            i += 1
            
        i = 26
        run = True
    print(processString)