import classes as c

point1 = c.obj1(0, 0, [0,0], [0,10], 0)
point2 = c.obj1(0, 0, [0,0], [20,5], 1)

print(point1.impulse(impulsePos=point2.position))