mylist = ["My Name Is ","eee",168,197,55,True,False]

mylist[1] = "Garry"
total = 0
for thing in mylist:
    if type(thing) == str:
        print(thing)
    elif type(thing) == int:
        total += thing

print("Total", total)
