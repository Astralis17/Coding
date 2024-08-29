


my_string = input()
letters = ""
output_numbers = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

for thing in my_string:
    if thing in alphabet:
        letters.append(thing)
    elif thing in numbers:
        output_numbers.append(thing)