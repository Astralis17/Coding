def fizzbuzz(n):
    i = 0
    while i < n:
        i = i + 1
        if i != 0:
            if i % 3 and i % 5:
                print("fizzbuzz")
            elif i % 3:
                print("fizz")
            elif i % 5:
                print("buzz")
            else:
                print(i)

fizzbuzz(int(input()))