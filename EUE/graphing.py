import math, pygame


def point(name:str):
        x = float(input(name.capitalize() + "x: "))
        y = float(input(name.capitalize() + "y: "))
        Pos = (x, y)
        return Pos
def findLength(points:dict, OppPoint:str):
        keyList = points.keys()
        otherPoints = []
        for key in keyList:
                if key == OppPoint:
                        pass
                else:
                        otherPoints.append(points[key])
        length = math.dist(otherPoints[0], otherPoints[1])
        return {OppPoint:length}

def cosineRule(lengthList:dict,PointName:str):
        keyList = points.keys()
        otherLengths = []
        for key in keyList:
                if key == PointName:
                        pass
                else:
                        otherLengths.append(lengthList[key])
        a = lengthList[PointName]
        b = otherLengths[0]
        c = otherLengths[1]

        abc = b**2 + c**2 - a**2
        radians = math.acos(abc/(2*b*c))

        degrees = math.degrees(radians)
        return degrees
names = ["a", "b", "c"]

points = {}
for name in names:
        Pos = point(name)
        points.update({name:Pos})

lengths = {}
for name in names:
        length = findLength(points, name)
        lengths.update(length)

print("Lengths:",lengths)
angles = {}
for name in names:
        angle = cosineRule(lengths, name)
        angles.update({name:angle})
print("Points : ", points)
print("Lengths: ", lengths)
print("Angles : ", angles)

pygame.init()


windowDim = (1440, 810)
display = pygame.display.set_mode(windowDim)

