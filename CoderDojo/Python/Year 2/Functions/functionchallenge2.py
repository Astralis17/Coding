
signinput = input("Sign:")
def add():
    input1 = int(input("Number1:"))
    input2 = int(input("Number2:"))
    return input1 + input2

def minus():
    input1 = int(input("Number1:"))
    input2 = int(input("Number2:"))
    return input1 - input2

def multiply():
    input1 = int(input("Number1:"))
    input2 = int(input("Number2:"))
    return input1 * input2

def divide():
    input1 = int(input("Number1:"))
    input2 = int(input("Number2:"))
    return input1 / input2

if signinput == "+":
    squareoutput = add()
elif signinput == "-":
    print(minus())
elif signinput == "*":
    print(multiply())
elif signinput == "/":
    print(divide())
print