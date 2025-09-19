from splines import *



p1 = point((200, 620))
p2 = point((200, 100))
p3 = point((540, 310))
p4 = point((880, 100))
p5 = point((880, 620))
points = [p1, p2, p3, p4, p5]

lineBase = spline(points)

for set in lineBase.bezierCurvePointSets:
        out = []
        for p in set:
                out.append(p())
        print(out)