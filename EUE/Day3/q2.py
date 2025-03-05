x = int(input())
x = int(x * (x/((x ** 2)**0.5)))+1
i = 0
while i != x:
    output = ""
    if i % 3 == 0:
        output += "fizz"
    if i % 5 == 0:
        output += "buzz"
    if not (i % 3 == 0) and not (i % 5 == 0):
        output = str(i)

    print(output)
    i += 1