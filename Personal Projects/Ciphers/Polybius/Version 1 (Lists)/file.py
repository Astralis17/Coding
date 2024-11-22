import functions

run = True
plaintext = ""
ciphertext = ""

print("Welcome to the Polybius Cipher Tool")
print("Enter 1 to select Encoding")
print("Enter 2 to select Decoding")
while run:
    mode = int(input("Mode: "))
    if mode !=1:
        if mode != 2:
            print("ERROR")
        else:
            run = False
    else:
        run = False
if mode == 1:
    print("~~~~~~~~~~~~~~~~~")
    print("ENCODING SELECTED")
    print("~~~~~~~~~~~~~~~~~")
    plaintext = input("Input your plaintext: ")
    print(functions.encode(plaintext))
else:
    print("~~~~~~~~~~~~~~~~~")
    print("DECODING SELECTED")
    print("~~~~~~~~~~~~~~~~~")
    ciphertext = input("Input your ciphertext: ")
    print(functions.decode(ciphertext))


