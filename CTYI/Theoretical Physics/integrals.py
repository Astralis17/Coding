import aTools

a = 3
b = -2

func = aTools.Math.number("5x^4")
integral = func.integrate()

tot = integral(a) - integral(b)
print(tot)