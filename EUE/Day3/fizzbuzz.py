def fizzbuzz(num):
    output = ""
    if num % 3 == 0:
        output += "fizz"
    if num % 5 == 0:
        output += "buzz"
    if not (num % 3 == 0) and not (num % 5 == 0):
        output = str(num)
    return output