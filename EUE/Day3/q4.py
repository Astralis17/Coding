word = input("Word: ").lower()          #ice
longer  =input("Longer Word: ").lower() #office

if not word in longer:
    print(word + " cannot be found in " + longer)
else:
    x  = 0
    while x+len(word) <= len(longer):
        if longer[x:x+len(word)] == word:
            print("Word Found at position", x)
            break
        else:
            x += 1
