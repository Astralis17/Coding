
def keyproccessing(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQTSTUVWXYZ"
    key1 = key
    key2 = []
    i = 0
    a = 0
    while len(plaintext) > len(key):
        key += key1
    key += key1
    while len(key) > i :

        if key[i] == alphabet[a]:
            key2.append(a)
            a = 0
            i += 1
        else:
            a+=1
    return key2


#key2 = (keyproccessing("hello there", "region"))
#print("Result: ", key2)
def encoding(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQTSTUVWXYZ"
    processString = ""
    a = 0
    run = True
    for letter in plaintext:
        shift = key[a]
        i = 0
        while run:
            if letter == " ":
                processString += " "
                run = False
                a -= 1
            if letter == alphabet[i % 26]:
                processString += alphabet[(i + shift) % 26]
                run = False
            if letter == ALPHABET[i % 26]:
                processString += ALPHABET[(i + shift) % 26]
                run = False
            i += 1

        a += 1
        run = True
    return processString

def decoding(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQTSTUVWXYZ"
    processString = ""
    a = 0
    run = True
    for letter in plaintext:
        i = 0
        shift = key[a]
        while run:
            if letter == " ":
                processString += " "
                run = False
                a -= 1
            if letter == alphabet[i % 26]:
                processString += alphabet[(i - shift) % 26]
                run = False
            if letter == ALPHABET[i % 26]:
                processString += ALPHABET[(i - shift) % 26]
                run = False
            i += 1

        a += 1
        run = True
    return processString