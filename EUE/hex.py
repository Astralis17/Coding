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


def function(hexes, num, baseOut, power):
    order = []
    while power != -1:
        x = num // (baseOut ** power)
        num -= x * (baseOut ** power)
        order.append(str(x))


        power -= 1


    output = ""

    for element in order:
        output += hexes[element]
    print(output)
    return output


def new_func(hexes, hexesInverse, findLargestPower, function, num =input("Number: "),baseIn = int(input("Base In: ")),baseOut = input("Base Out: ")):
    numed = list(reversed(num))

    newNum = 0
    powered = 0
    for i in range(0, len(num)):
        x = int(hexesInverse[numed[i]])

        newNum += x * (baseIn ** powered)
        powered += 1

    print(newNum)
    num = newNum

    if len(baseOut) > 3:
        baseOuts = baseOut.split(" ")
        for baseOut in baseOuts:
            baseOut = int(baseOut)
            power = findLargestPower(baseOut, num)
            function(hexes, num, baseOut, power)
            ans = ""

    else:
        baseOut = int(baseOut)
        power = findLargestPower(baseOut, num)
        ans = function(hexes, num, baseOut, power)
    return ans

nums = input("Numbers: ")
nums = nums.split(".")
print(nums)
outputs = []
for num in nums:
    ans = new_func(hexes, hexesInverse, findLargestPower, function, num =num, baseIn=10, baseOut="2")
    outputs.append(ans)

tempAnses = []
for ans in outputs:
    tempAns = ans
    while len(tempAns) < 8:
        tempAns = "0" + tempAns
    tempAnses.append(tempAns)

outputString = ""
for tempAns in tempAnses:
    outputString += tempAns + "."
print(outputString)