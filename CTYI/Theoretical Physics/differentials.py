from math import sin,cos
import numpy
num = 0.5

def deriving(function, offset=-1, level=1):
        level -= 1
        if offset == -1:
                offset = 1.0000000000000002e-08
        def deriv(x, offset=offset, order = 1) -> float:
                for i in range(order):
                        a = function(x+offset) - function(x)
                        a /= offset
                return a
        #func = function
        #while level > 0:
        #        func = deriv(func, offset, level)
        #        level -= 1

        return deriv

def diff(x, y):
        return abs(x-y)


fprime = deriving(sin)
cosprime = deriving(cos)
F = [sin]
G = [deriving(F[0])]

for i in range(1,5):
        F.append(deriving(F[i-1]))
        G.append(deriving(G[i-1]))
        print(diff(F[i-1](num), G[i](num)))

print(G)
print(F)
'''
sin -> cos
cos -> -sin
-sin -> -cos
-cos -> sin
'''
g = G[0]
h = F[0]

print(h(num))

offset = 0.1
a = fprime(num, offset)
b = fprime(num, offset/10)
'''while b > a:
        offset = offset/10
        a = fprime(num, offset)
        b = fprime(num, offset/10)
out = a

print(f"\nOffset: {offset}")
print(f"Output: {out}")
'''
print(f"Cos: {g(num)}")
print(f"Difference: {diff(g(num), (h)(num))}")

'''
print(fprime(num, 0.00000001))
zeros = 0
while offset < 0.1:
        offset = offset * 10
        zeros += 1
print(zeros)
'''