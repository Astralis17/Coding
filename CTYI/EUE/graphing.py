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



windowDim = (1440, 810)

offsetV = -75
offsetH = 100

def checkPos(p1:tuple, p2:tuple, p3:tuple, dim:int, pos:int):
    check = [p1[dim], p2[dim], p3[dim]]
    check.sort()
    return check[pos]

bottoms = [checkPos(points["a"], points["b"], points["c"], x, 0) for x in range(0,2)]
tops = [checkPos(points["a"], points["b"], points["c"], x, -1) for x in range(0,2)]

differences = [(tops[0] - bottoms[0]), (tops[1] - bottoms[1])]
if differences[0] > differences[1]:
    LengthMaxima = differences[0]
    axisMaxima = 0
else:
    LengthMaxima = differences[1]
    axisMaxima = 1


scalor = 4
print("LengthMaxima:",LengthMaxima)
10
10
300
900
1700
200

pygame.init()
display = pygame.display.set_mode(windowDim)
pygame.display.set_caption("Graph")

class point:
    def __init__(self, x, y, id):
        self.id = id  #identifier to communicate with other points
        self.x = x    #x position in relation to points
        self.y = y    #x position in relation to points

class Triangle:
    def __init__(self, P1:point, P2:point, P3:point, center:tuple=(0,0), colour:tuple=(235, 20, 20)):
        self.center = center
        P0 = center
        self.points = []
        points = [P1, P2, P3]
        for point in points:
            self.points.append((point[0] * scalor, point[1] * scalor))
        self.colour = colour
        print(self.__dict__)


    def draw(self, thickness):
        x = 0
        pointList = self.points + self.points + self.points
        for pointA in self.points:
            x += 1
            pointB = pointList[x]
            pygame.draw.line(display,
                             self.colour,
                             (pointA[0] + offsetH, pointA[1] + windowDim[1] + offsetV),
                             (pointB[0] + offsetH, pointB[1] + windowDim[1] + offsetV),
                             thickness
                            )


#p1 = (0, 5)
#p2 = (10, 0)
#p3 = (0, 0
for x in points:
      print(x)
pointsList = [(points[x][0], points[x][1]*-1) for x in points]

t = Triangle(pointsList[0], pointsList[1], pointsList[2])

display.fill((0,0,0))
t.draw(5)

run = True
while run:
    display.fill((20,150,20))

    display.fill((0,0,0), (offsetH, offsetV*-1, windowDim[0]-(offsetH*2), windowDim[1]+(offsetV*2)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


    t.draw(5)
    pygame.display.flip()