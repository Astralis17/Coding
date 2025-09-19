import math
print("Welcome to the quadratic equation solver")

a = int(input("x^2 Coefficient : "))
b       = int(input("x Coefficient   : "))
c = int(input("Standard int    : "))
right   = int(input("It should be zero but enter the \nRight side of = : "))

c -= right


root = ((b*b)-4*a*c)
print(root)
rooted = math.sqrt(root)

Positive = (-1*b + rooted)/(2*a)
Negative = (-1*b - rooted)/(2*a)


print("Positive result:", Positive)
print("Negative result:", Negative)