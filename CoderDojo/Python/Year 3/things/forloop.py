sentence = "hi, your a person (i think)"

vowels = ["a", "e", "o", "i", "u"]
i = 0
for letter in sentence:
    if letter in vowels:
        i += 1
print(i)

letter = sentence[0]
charValue = 0
