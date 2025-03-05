run = True
while run:
    print("\n\n\nIs it Odd or is it Even, step right up step right up and let's see")
    x = int(input("Input: "))

    if x % 2 == 0:
        print("\nYour number was Even")
    else:
        print("Your number was Odd")

    repeat = input("Wanna try again (y/n)\n")
    if not repeat.startswith("y"):
        run = False
    else:
        run = True
