hexes = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
}
hexesInverse = {}
for item in hexes.keys():
    a = hexes[item]
    hexesInverse.update({a:item})

def findLargestPower(base, num):
    power = 0
    while True:
        if num < base ** power:
            print("Number is between ", (base ** (power-1)), " and ", (base ** power))
            return power -1
        else:
            power += 1



num = input("Number: ")
numed = list(reversed(num))
baseIn = int(input("Base In: "))
baseOut = int(input("Base Out: "))

newNum = 0
powered = 0
for i in range(0, len(num)):
    x = int(hexesInverse[numed[i]])
    print(x)

    newNum += x * (baseIn ** powered)
    powered += 1

print(newNum)
num = newNum


power = findLargestPower(baseOut, num)

order = []
while power != -1:
    x = num // (baseOut ** power)
    num -= x * (baseOut ** power)
    order.append(str(x))


    power -= 1


print(order)
output = ""

for element in order:
    output += hexes[element]
print(output)