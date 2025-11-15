import random



monthNum = random.randint(1, 12)

D31 = [1, 3, 5, 7, 8, 10, 12]
D30 = [4, 6, 9, 11]

months = ["null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def new_func(D31, D30, months):
    monthNum = random.randint(1, 12)
    print(f"\n{monthNum}")
    if monthNum in D31:
            print(f"{months[monthNum]} has 31 days")
    elif monthNum in D30:
            print(f"{months[monthNum]} has 30 days")
    else:
            print(f"{months[monthNum]} has 28 days")


for x in range(0, 50):
        new_func(D31, D30, months)