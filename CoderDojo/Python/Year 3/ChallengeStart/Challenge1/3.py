hobbies  = []
i = 0
I = 0
hinput = ""
print("Tell me about yourself")
name = input("What is your name: ")
age = input("How old are you: ")
hobbiescount = int(input("How many hobbies do you have: "))
I = hobbiescount

while I != 0:
    if i != hobbiescount:
        hobbies.append(input("Hobbie" + str(i + 1) + ": "))
        i += 1
        I -=1
    else:
        break

print("Your name is", name, ",you are ", age,"years old", "and your hobbies are", hobbies)