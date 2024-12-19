inputText = ""

file = open("Personal Projects/AdventOfCode/Day3/input.txt", "r")
output = open("Personal Projects/AdventOfCode/Day3/output.txt", "w")
lines = file.readlines()
for line in lines:
    inputText += line[:-1]

i = 0
characterPos = 0
run = True
multiplying = True

while run:
    first5 = inputText[characterPos:characterPos+5]
    if first5[:-1] == "mul(" and multiplying == True:
        characterPos += 5
        processString = first5
        done = False
        while not done:
            character = inputText[characterPos]
            if character.isdigit():
                characterPos += 1
                processString += character
            elif character == ",":
                characterPos += 1
                processString += character
            elif character == ")":
                done = True
                characterPos += 1
                processString += character
            else:
                done = True
                processString = "mul(0,0)"

        output.write(processString+"\n")
        print(processString)
        processString = processString[4:-1]

        digits = processString.split(",")
        if len(digits) < 2:
            digits.append("0")
        digits = [int(num) for num in digits]

        i += digits[0] * digits[1]

    elif first5[:2] == "do":
        print(first5)
        if first5 == "don't":
            multiplying = False
            characterPos += 5
        else:
            multiplying = True
            characterPos += 2

    else:
        characterPos += 1
    if characterPos > len(inputText):
        run = False
        break
print(i)