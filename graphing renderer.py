import pygame


pygame.init()

displayDimensions = (1440, 810)
display = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption("Graph")

class point:
    def __init__(self, x, y, id):
        self.id = id  #identifier to communicate with other points
        self.x = x    #x position in relation to points
        self.y = y    #x position in relation to points

class Triangle:
    def __init__(self, P1:point, P2:point, P3:point, center:tuple, colour:tuple):
        self.center = center
        P0 = center
        self.points = [P0, P1, P2, P3]
    def draw(self):
        x = 0
        pointList = self.points + self.points + self.points
        print(pointList)
        for pointA in self.points:
            x += 1
            pointB = pointList[x]
            print([pointA, pointB])
            pygame.draw.line(display, self.colour, (pointA + (100,100)), (pointB + (100,100)), thickness)



p1 = (5, 10)
p2 = (10, 5)
p3 = (7, 2)


drawTriangle([p1, p2, p3], (255, 20, 20), 5)


while True:



    pygame.display.flip()