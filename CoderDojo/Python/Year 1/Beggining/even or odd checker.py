print("This program ckecks number are odd or even up to ten")
n = int(input())
i = n
while i<=10 :
    print("Enter a number")
    
    if i ==0:
        print ("Invalid Number")
    else:    
        
        if n%2==0:
            print("Your number was even")
        else:
            print ("Your number was odd")

        n = int(input())    
        i == n

