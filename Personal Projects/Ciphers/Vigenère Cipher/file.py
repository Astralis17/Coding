import functions


plaintext = ""
ciphertext = ""
key = ""

print("Welcome to the Vigenère Cipher Tool")
run = True
print("Enter 1 to select Encoding")
print("Enter 2 to select Decoding")
while run:
    mode = int(input("Mode: "))
    if mode !=1:   
        if mode != 2: 
            print("ERROR")
        else:
            run = False
            print("~~~~~~~~~~~~~~~~~")
            print("DECODING SELECTED")
            print("~~~~~~~~~~~~~~~~~")
    else:
        run = False
        print("~~~~~~~~~~~~~~~~~")
        print("ENCODING SELECTED")
        print("~~~~~~~~~~~~~~~~~")
if mode == 1:
    plaintext = input("Input your plaintext: ")
    key = input("Key: ")
    print(functions.encoding(plaintext, functions.keyproccessing(ciphertext, key)))
else:
    ciphertext = input("Input your ciphertext: ")
    key = input("Key: ")
    print(functions.decoding(ciphertext, functions.keyproccessing(ciphertext, key)))


