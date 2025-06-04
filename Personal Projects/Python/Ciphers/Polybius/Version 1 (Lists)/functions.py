

def encode(plaintext):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    plaintext = plaintext.lower()
    poly = ["11 ","12 ","13 ","14 ","15 ","21 ","22 ","23 ","24 ","25 ","31 ","32 ","33 ","34 ","35 ","41 ","42 ","43 ","44 ","45 ","51 ","52 ","53 ","54 ","55 "]
    ciphertext = ""
    for thing in plaintext:
        x = 0
        run = True
        if thing == " ":
            run = False
        while run:
            if thing == alphabet[x]:
                ciphertext += poly[x]
                run = False

            elif x ==26:
                run = False
            x+=1
    return ciphertext


def decode(ctext):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    poly = ["11","12","11","14","15","21","22","23","24","25","31","32","33","34","35","41","42","43","44","45","51","52","53","54","55"]
    ptext = ""
    x = 0
    i = 0
    run = True
    str1 = ""
    for thing in ctext:
        if thing != " ":
            str1 += thing
    ctext = str1
    if (len(ctext)%2) == 1:
        ctext = ctext[:-1]
        print(ctext)
    while run:
        str2 = ctext[x] + ctext[x + 1]
        check = True
        i = 0
        x =+ 2

        while check:
            if str2 == poly[i]:
                ptext += alphabet[i]
                check = False

            if str2 == "00":
                ptext += " "
                check = False

            elif i ==26:
                check = False
            i += 1

        if len(ptext) == (len(ctext)/2):
            run = False
    return ptext
