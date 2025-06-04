
Days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def gap():
    print("")

def calc():
    gap(); print("Hello, welcome to the Birthday Calculator")

    print("(When entering day please use numbers e.g Monday = 1, Tuesday = 2, etc)")
    gap(); Day = int(input("What day does your birthday occur on this year: ")) - 1   

    gap(); Age = int(input("How old are you / How old will you be after your birthday: "))

    gap(); Leapdays = int(input("How many Leap Days since you were born: "))

    a = Age + Leapdays 
    b = int(a % 7)
    
    e = Days[(Day - b) % 7]
    return e

e = calc()
gap(); print(e)