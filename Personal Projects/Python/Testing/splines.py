import pygame, aTools, math
pygame.init()
window = pygame.display.set_mode((1080, 720))

class point:
        def __init__(self, pos):
                self.x = pos[0]
                self.y = pos[1]
        def __call__(self):
                return (self.x, self.y)

class splineLine:
        def __init__(self, p1:point, p2:point, colour):
                self.p1 = p1
                self.p2 = p2
                self.m = point(aTools.midpoint(p1(), p2()))
                self.colour = colour
                self.fill = 0.5

        def findM(self):
                baseX = self.p1.x
                baseY = self.p1.y
                distX = self.p2.x - self.p1.x
                distY = self.p2.y - self.p1.y
                self.m.x = (baseX + (distX*self.fill))
                self.m.y = (baseY + (distY*self.fill))

        def draw(self):
                pygame.draw.line(window, self.colour, self.p1(), self.p2(), 3)
                pygame.draw.circle(window, self.colour, self.m(), 5)

class spline:
        def __init__(self, points):
                pass
p1 = (200, 620)
p2 = (200, 260)
p3 = (880, 460)
p4 = (880, 100)
spline1 = splineLine(point(p1), point(p2), "green")
spline2 = splineLine(point(p2), point(p3), "red")
spline3 = splineLine(point(p3), point(p4), "blue")
splines = [spline1, spline2, spline3, 0, 0, 0]
points = []
fillPercent = 0
splines[3] = splineLine(spline1.m, spline2.m, "yellow")
splines[4] = splineLine(spline2.m, spline3.m, "orange")
splines[5] = splineLine(splines[3].m, splines[4].m, "pink")
for i in range(1000):
        for spline in splines:
                spline.fill = i * 0.001
                spline.findM()
        points.append(splines[5].m())
run = True
while run:
        splines[3] = splineLine(spline1.m, spline2.m, "yellow")
        splines[4] = splineLine(spline2.m, spline3.m, "orange")
        splines[5] = splineLine(splines[3].m, splines[4].m, "pink")
        window.fill("black")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                points = []
                                for i in range(1000):
                                        for spline in splines:
                                                spline.fill = i * 0.001
                                                spline.findM()
                                        points.append(splines[5].m())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                fillPercent += 0.001
        if keys[pygame.K_DOWN]:
                fillPercent -= 0.001

        #fillPercent = aTools.rangeLimit(fillPercent)

        for spline in splines:
                spline.fill = fillPercent
                spline.findM()
        splines[5].draw()





        pygame.draw.lines(window, "red", False, points, 5)
        pygame.display.update()