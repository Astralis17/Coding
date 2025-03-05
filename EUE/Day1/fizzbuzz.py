print("Welcome to fizzbuzz, \n \nEnter 1 for specific mode\nEnter 2 for range mode")

mode = int(input("Mode: "))

def check(input):
    output = ""
    if (input % 3) == 0:
        output += "fizz"
    if (input % 5) == 0:
        output += "buzz"
    if not (input % 3 == 0) and not (input % 5 == 0):
        output += str(input)

    return output


if mode == 1:
    input = int(input("Input Number: "))
    print(check(input))

else:
    start = int(input("What is the start of the range: "))
    end   = int(input("What is the end of the range: ")) + 1

    while start != end:
        print(check(start))
        start += 1
