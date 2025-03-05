i = int(input("Number:"))
x = 0
i += i/((i ** 2)**0.5)
while i != x:
    print(int(x))
    x += i/((i ** 2)**0.5)
