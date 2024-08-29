
Days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def gap():
    print("")


def calc():


    gap(); print("Hello, welcome to the Birthday Calculator")
    

    print("(When entering day please use numbers e.g Monday = 1, Tuesday = 2, etc)")
    gap(); Day = int(input("What day does your birthday occur on this year: "))    


    gap(); Date = int(input("What is the date your birthday occurs on: "))    


    gap(); print("(When entering the month please use numbers e.g January = 1, February = 2, etc)")
    Month = int(input("What month does your birthday occur in: "))
    
    if Month >= 13:
        print("!!Error!!")
        return


    gap(); Age = int(input("How old are you / How old will you be after your birthday: "))


    gap(); Leapdays = int(input("How many Leap Days since you were born: "))



    if Month == 1:
        a = 0
    elif Month == 2:
        a = 31
    elif Month == 3:
        a = 59
    elif Month == 4:
        a = 90
    elif Month == 5:
        a = 120
    elif Month == 6:
        a = 151
    elif Month == 7:
        a = 181
    elif Month == 8:
        a = 212
    elif Month == 9:
        a = 242
    elif Month == 10:
        a = 273
    elif Month == 11:
        a = 303
    elif Month == 12:
        a = 334
    

    b = (a + Date)
    gap(); print("Days since start of year: ")
    print(b)

    c = ((Age + Leapdays) % 7) 
    gap(); print(c)
    d = int(c % 7)
    
    e = Days[(Day + d) % 7]
    return e

e = calc()
gap(); print(e)