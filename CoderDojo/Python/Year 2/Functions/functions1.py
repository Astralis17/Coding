def square(number):
    return number * number
    

my_square = square(5)

print(my_square)



def age_check(age):
    if age >=  18:
        return True
    else:
        return False

ages = [16 , 11, 12, 19, 54, 104, 4, 17]

for person in ages:
    print(age_check)