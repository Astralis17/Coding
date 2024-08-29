def read(path):
    with open(path, 'r') as file:
        data = file.readlines()

    list = eval(data[0].strip())
    string = data[1].strip()

    return list, string

def write(path, list, string):
    with open(path, 'w') as file:
        file.write(str(list) + '\n')
        file.write(string)

list, string = read("Testing\\test.txt")

print(list)
print(string)

list.append(string)
string += " and a potato"

write("Testing\\test.txt", list, string)