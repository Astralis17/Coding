import random

Variable1 = 50
list2 = ["hi",Variable1]
repeatnum = 10
num1 = 1
list2ran = 0
while repeatnum>0 :

    list1 = [list2[list2ran],Variable1]
    print (list1[num1])
    list2 = ["hi",Variable1]
    repeatnum -= 1
    Variable1 =random.randint(1,100)
    num1 = random.randint(0,1)
    list2ran = random.randint(0,1)
