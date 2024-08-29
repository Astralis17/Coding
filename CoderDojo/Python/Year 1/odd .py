i = 1000
while i >= 0:
    n = int(input())
    if n >= 1:
        if n <= 10:

            if n%2==0:
                print("Your number was even")
            else:
                print ("Your number was odd")
        else:
            print ("Invalid Number")
    else:
        print ("Invalid Number")