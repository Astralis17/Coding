import math
print("This is such bullshit but here goes nothing")

print("Enter co-ordinates of A")
xA = float(input("x: "))
yA = float(input("y: "))

print("Enter co-ordinates of B")
xB = float(input("x: "))
yB = float(input("y: "))
print("Enter co-ordinates of C")
xC = float(input("x: "))
yC = float(input("y: "))

def aCos(a,b,c):
    abc = ((-1*a*a)+(b*b)+(c*c))
    x = math.acos(abc / (2 * b * c))
    x = math.degrees(x)
    return x

print("\n")
a = math.dist((xB, yB), (xC, yC))
b = math.dist((xA, yA), (xC, yC))
c = math.dist((xB, yB), (xA, yA))

print("a:", a)
print("b:", b)
print("c:", c)



A = aCos(a, c, b)
B = aCos(b, a, c)
C = aCos(c, a, b)

print("Angle A:", A)
print("Angle B:", B)
print("Angle C:", C)
