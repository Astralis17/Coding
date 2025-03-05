i = 0
x = input("First Number: ")

while True:
    i += 1
    answer = ""
    if i % 3 == 0:
        answer += "fizz"
    if i % 5 == 0:
        answer += "buzz"
    if not (i % 3 == 0) and not (i % 5 == 0):
        answer = str(i)

    if x == answer:
        print("Correct")
        x = input("Next Number: ")
    else:
        print("FAILED")
        break