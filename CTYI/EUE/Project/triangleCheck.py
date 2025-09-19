import pygame
import math

pygame.init()
window = pygame.display.set_mode((800,600))



trianglePoints = (
        (400, 200),
        (200, 500),
        (600, 500)
)

run = 1

def midpoint(pointA, pointB):
        return (
                (pointA[0] + pointB[0]) / 2,
                (pointA[1] + pointB[1]) / 2
        )
def triangleArea(points, altPoint =[0,0], altPointReplace =-1):
        colours = ("red", "green", "blue")
        points = list(points)
        if altPointReplace != -1:
                points[altPointReplace] = altPoint
        lines = {
                math.dist(points[0],points[1]): (0,1),
                math.dist(points[1],points[2]): (1,2),
                math.dist(points[2],points[0]): (0,2)
        }
        linelengths = [
                math.dist(points[0],points[1]),
                math.dist(points[1],points[2]),
                math.dist(points[2],points[0])
        ]
        linelengths.sort()
        hyp = lines[linelengths[-1]]
        hypMidpoint = midpoint(points[hyp[0]], points[hyp[1]])
        for point in [0,1,2]:
                if point not in hyp:
                        y = point




        b = math.dist(points[hyp[0]], points[hyp[1]])
        b /= 2
        h = math.dist(hypMidpoint, points[y])

        a = b * h

        #if altPointReplace == 2:
        #        print(hypMidpoint)
        if altPointReplace != -1:
                pygame.draw.polygon(window, colours[altPointReplace], points, 5)
                pygame.draw.circle(window, colours[altPointReplace], hypMidpoint, 5)
                pygame.draw.line(window, colours[altPointReplace], hypMidpoint, points[y])
                m = hypMidpoint

        return a

cursorPosition = (0,0)

class point:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def draw(self):
                pygame.draw.circle(window, "yellow", (self.x, self.y), 5)
points = []


timer = 0
tArea = triangleArea(trianglePoints)

while run:
        pygame.time.delay(50)
        timer += 50

        window.fill("black")
        cursorPosition = pygame.mouse.get_pos()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = 0


        a1 = triangleArea(trianglePoints, cursorPosition, 0)
        a2 = triangleArea(trianglePoints, cursorPosition, 1)
        a3 = triangleArea(trianglePoints, cursorPosition, 2)

        if timer % 500 == 0:
                print("\nSubTriangles: ",(a1+a2+a3))
                print("- r: ",(a1))
                print("- g: ",(a2))
                print("- b: ",(a3))
                print("Triangle Area: ", tArea)

        if (a1+a2+a3)/2 < tArea:
                color = "purple"
                width = 10
        else:
                color = "red"
                width = 1


        pygame.draw.polygon(window, color, trianglePoints, width)
        pygame.display.update()