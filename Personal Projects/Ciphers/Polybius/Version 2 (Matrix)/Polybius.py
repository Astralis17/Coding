global Matrix
Matrix = [
          ["a", "b", "c", "d", "e"],
          ["f", "g", "h", "i", "k"],
          ["l", "m", "n", "o", "p"],
          ["q", "r", "s", "t", "u"],
          ["v", "w", "x", "y", "z"]
         ]
def decode(ciphertext, Capitalisation=0, CustomWords={}):
        ciphertext = list(ciphertext)
        plaintext = ""
        query = []
        if Capitalisation > 0:
                capitalise = True
        else:
                capitalise = False

        while " " in ciphertext:
                ciphertext.remove(" ")

        while len(ciphertext) > 0:
                obj = ciphertext.pop(0)
                obj += ciphertext.pop(0)

                query.append(obj)

        while len(query) > 0:
                num = query.pop(0)
                row = int(num[0]) - 1
                column = int(num[1]) - 1

                if row < 0 or column < 0:
                        plaintext += " "
                        if Capitalisation == 2:
                                capitalise = True
                else:

                        if capitalise:
                                plaintext += Matrix[row][column].upper()
                                capitalise = False
                        elif (Matrix[row][column] == "i") and (plaintext[-1] == " ") and (query[0] == "00"):
                                plaintext += Matrix[row][column].upper()
                        else:
                                plaintext += Matrix[row][column]
                if Capitalisation > 2:
                        capitalise = True
        return plaintext

def encode(plaintext, CustomWords={}):
        plaintext = [x.lower() for x in plaintext]
        ciphertext = ""
        ciphertextList = []
        print(plaintext)

        for character in plaintext:
                broken = False
                searching = True
                RowN = 0
                ColN = 0
                for row in Matrix:
                        if character in row:
                                searching = False
                        elif searching:
                                RowN += 1
                if searching:
                        broken = True
                        RowN = 0
                        if character == "j":
                                result = encode("i")
                        else:
                                result = "00 "
                else:
                        searching = True

                for collum in Matrix[RowN]:
                        if broken:
                                break
                        if character == collum:
                                searching = False
                        elif searching:
                                ColN += 1
                if not broken:
                        result = str(RowN+1) + str(ColN+1) + " "
                ciphertextList.append(result)

        for set in ciphertextList:
                print(set)
                ciphertext += set

        return ciphertext


print("Welcome to the Polybius Cipher Tool (Version 2! Now with added Matrices)")
while True:
        print("Enter 1 to select Encoding")
        print("Enter 2 to select Decoding")
        print("Enter 3 to add character to Custom Dictionary")
        while True:
                mode = int(input("Mode: "))
                if mode > 3 or mode < 0:
                        print("Please select one of the actual options")
                else:
                        break

        if mode == 1:
                print("~~~~~~~~~~~~~~~~~")
                print("ENCODING SELECTED")
                print("~~~~~~~~~~~~~~~~~")
                plaintext = input("Input your plaintext: ")
                print(encode(plaintext))
        elif mode == 2:
                print("~~~~~~~~~~~~~~~~~")
                print("DECODING SELECTED")
                print("~~~~~~~~~~~~~~~~~")
                ciphertext = input("Input your ciphertext: ")
                print("/n", "Capitalisation Mode")
                print("0: no capitalisation")
                print("1: Capitalisation for first letter only")
                print("2: Capitalisation For First Letter Of All Words")
                print("3: ALL CAPITALISATION")
                capMode = int(input("Capitalisation mode: "))
                print(decode(ciphertext, Capitalisation=capMode))

        if input("Are you done (y/n): ").lower().startswith("y"):
                break