def encode(plaintext):
    LETTERS= "abcdefghijklmnopqrstuvwxyz "
    MORSE= [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ","--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ","-.-- ","--.. "," "]
    i = 0
    a = 0
    check = True
    morse = []
    ciphertext =""
    for a in plaintext:
        while check:
            if a == LETTERS[i]:
                morse.append(MORSE[i])
                check= False
            else:
                i+=1
        i=0

        check=True

    a = 0
    while i < len(morse):
        while a < len(morse[i]):
            if morse[i][a] == ".":
                ciphertext += "10"
            elif morse[i][a] == "-":
                ciphertext += "1110"
            elif morse[i][a] == " ":
                ciphertext += "00"

            a+=1
        a=0
        i+=1
    while ciphertext[-1] == "0":
        ciphertext = ciphertext[:-1]
    return ciphertext


def decode(ciphertext):
    LETTERS= "abcdefghijklmnopqrstuvwxyz "
    MORSE= [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ","--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ","-.-- ","--.. ","/ "]
    i = 0
    plaintext = ""
    while ciphertext[-1] == "0":
        ciphertext = ciphertext[:-1]
    ciphertext += "0a"
    processing = ciphertext
    list = []

    try:
        while processing[-1] == "a":
            string = ""
            checking = True
            while checking:
                if processing[0] + processing[1] == "10":
                    i = 2
                    string += "."

                if processing[0] + processing[1] == "11":
                    i = 4
                    string += "-"

                if processing[0] == "a":
                    list.append(string)

                if processing[0] + processing[1] == "00":
                    if processing[2] + processing[3] == "00":
                        list.append(string +" ")
                        string = "/ "
                        i = 4
                    else:
                        i = 2
                        string += " "
                    checking = False
                    list.append(string)

                while i != 0:
                    processing = processing[1:]
                    i -= 1
                if processing[0] == "a":
                    list.append(string + " ")
                    processing = "b"

        list.append(string)
    except:
        i = 0
    for thing in list:
        while thing != MORSE[i]:
            i += 1
        plaintext += LETTERS[i]
        i = 0

    return plaintext


print(encode("hello world"))















    