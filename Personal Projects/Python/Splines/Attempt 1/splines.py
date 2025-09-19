import pygame, aTools, math
from unix import time as Time
timepoint = Time.time
pygame.init()
window = pygame.display.set_mode((1080, 720))

class point:
        grabbed = False
        def __init__(self, pos, drawing = False):
                self.x = pos[0]
                self.y = pos[1]
                self.drawing = drawing
        def __call__(self):
                return (self.x, self.y)
        def __str__(self):
                return f"({self.x}, {self.y})"

        def draw(self):
                pygame.draw.circle(window, "white", self(), 10, 2)

        def click(self, cursor):
                if cursor.pressed[0] and math.dist(self(), cursor.pos) < 10 and self.drawing:
                        self.grabbed = True
                if self.grabbed and cursor.pressed[0]:
                        self.x = cursor.x
                        self.y = cursor.y
                        pygame.draw.circle(window, "green", self(), 10, 4)
                elif not self.drawing:
                        pygame.draw.circle(window, "red", self(), 10, 4)
                else:
                        self.grabbed = False

class line:
        def __init__(self, p1:point, p2:point, colour, fill=0.5):
                self.p1 = p1
                self.p2 = p2
                self.m = point(aTools.midpoint(p1(), p2()))
                self.colour = colour
                self.fill = fill

        def lerp(self):
                baseX = self.p1.x
                baseY = self.p1.y
                distX = self.p2.x - self.p1.x
                distY = self.p2.y - self.p1.y
                self.m.x = (baseX + (distX*self.fill))
                self.m.y = (baseY + (distY*self.fill))
                return self.m

        def draw(self):
                pygame.draw.line(window, self.colour, self.p1(), self.p2(), 3)
                pygame.draw.circle(window, self.colour, self.m(), 4)

        def magnitude(self):
                return math.dist(self.p1(), self.p2())
class lineBase:
        colourCount = 0
        fill = 0
        lines = []
        mPoints = []
class bezierCurve(lineBase):
        pointed = 0
        def __init__(self, points:list[point], drawLevel = -1, offset = 0):
                self.drawLevel = drawLevel
                self.offset = offset
                self.addPoints(points)

        def addPoints(self, points=[], p=point((0,0))):
                if points != []:
                        self.points = points
                else:
                        self.points.append(p)
                self.layerCounts = len(points) - 1
                self.layers = [{"points":[], "lines":[]} for i in range(self.layerCounts)]
                self.layers[0]["points"] = self.points

        def layer(self, level=0):
                set = self.layers[level]["points"]
                for i in range(len(set)-1):
                        LINE = line(set[i], set[i+1], colours[self.colourCount], self.fill)
                        if level != self.layerCounts - 1:
                                self.layers[level+1]["points"].append(LINE.lerp())
                        self.mPoints.append(LINE.lerp())
                        self.layers[level]["lines"].append(LINE)
                        self.lines.append(LINE)
                        self.colourCount = (self.colourCount + 1) % (len(colours) - 1)
                if level != self.layerCounts - 1:
                        self.layer(level+1)

        def draw(self):
                i = 0
                for level in self.layers:
                        if i == self.drawLevel:
                                pass
                                break
                        for line in level["lines"]:
                                line.fill = self.fill
                                line.draw()
                        i += 1
        def main(self):
                self.colourCount = 0
                self.drawLevel = drawLevel
                self.fill = aTools.Math.rangeLimit(fillPercent - self.offset)
                self.layers = [{"points":[], "lines":[]} for i in range(self.layerCounts)]
                self.layers[0]["points"] = self.points
                self.lines = []
                self.mPoints = []
                self.layer()
                self.draw()

        def SMpoints(self):
                points = []
                for i in range(1000):
                        for line in self.lines:
                                line.fill = i * 0.001
                                line.lerp()
                        try:
                                points.append(self.mPoints[-1]())
                        except:
                                break
                return points

        def __str__(self):
                outStr = ""
                for p in self.points:
                        outStr += p.__str__() + ", "
                outStr += "\n"
                return outStr

class spline(lineBase):
        BezierCurves = []
        bezierCurvePointSets = []
        def __init__(self, points):
                self.addPoints(points)

        def addPoints(self, points=0, p=point((0,0))):
                if points != 0:
                        self.points = points
                        self.BezierCurves = []
                        self.bezierCurvePointSets = []
                        for i in range(0,len(self.points)-2,3):
                                self.bezierCurvePointSets.append(self.points[i:i+4])
                        x = 0
                        for set in self.bezierCurvePointSets:
                                self.BezierCurves.append(bezierCurve(set, offset=x))
                                x += 1
                        print([x.__str__() for x in self.BezierCurves])
                else:
                        self.points.append(p)
                        self.bezierCurvePointSets.append(self.points[-5:-1])
                        self.BezierCurves.append(bezierCurve(self.points[-5:-1], offset=len(self.BezierCurves)))
                        print("point added")
                        print([x.__str__() for x in self.BezierCurves])
        def main(self):
                self.fill = fillPercent
                self.mPoints = []
                for bezierCurve in self.BezierCurves:
                        bezierCurve.fill = self.fill
                        bezierCurve.main()
                        self.mPoints.append(bezierCurve.layers[-1]["lines"][0].m())
                        pygame.draw.circle(window, "white", bezierCurve.layers[-1]["lines"][0].m(), 5)

        def SMpoints(self):
                points = []
                for bezierCurve in self.BezierCurves:
                        points += bezierCurve.SMpoints()
                return points

class spline2(lineBase):
        def __init__(self):
                self.addPoints()


        def addPoints(self, p):
                pass
class Cursor:
        x = 0
        y = 0
        pos = [x,y]
        pressed = False
        def update(self):
                self.pos = list(pygame.mouse.get_pos())
                self.x = self.pos[0]
                self.y = self.pos[1]
                self.pressed = pygame.mouse.get_pressed()


colours = [aTools.randomRGB() for i in range(500)]
fillPercent = 0
drawLevel = 0

p1 = point((200, 620))
p2 = point((200, 100))
p3 = point((540, 310))
p4 = point((880, 100))
p5 = point((880, 620))
points = [p1, p2, p4, p5]
for p in points:
        p.drawing = True

SPLINE = spline(points)
SPLINE.main()
SMpoints = SPLINE.SMpoints()
CURSOR = Cursor()


frameStart = timepoint()
gameStart = frameStart
run = True
while run:
        CURSOR.update()
        frameEnd = timepoint()
        frameDifference = abs(frameEnd - frameStart)
        deltaTime = frameDifference / 0.001
        frameStart = timepoint()
        window.fill("black")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                        points.append(point(CURSOR.pos, drawing=True))
                        SPLINE.addPoints(points)

                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_KP_PLUS:
                                drawLevel += 1
                        elif event.key == pygame.K_KP_MINUS:
                                drawLevel -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                fillPercent += 0.001 * deltaTime
        elif keys[pygame.K_DOWN]:
                fillPercent -= 0.001 * deltaTime
        if CURSOR.pressed:
                SMpoints = SPLINE.SMpoints()

        if type(SPLINE) == bezierCurve:
                fillPercent = aTools.Math.rangeLimit(fillPercent, roof=1, loop=True)
        else:
                fillPercent = aTools.Math.rangeLimit(fillPercent, roof=len(SPLINE.BezierCurves), loop=True)
        drawLevel = aTools.Math.rangeLimit(drawLevel, -1, 9999999999)
        #fillPercent = (fillPercent + (0.001*deltaTime)) % 1


        SPLINE.main()
        for p in points:
                p.draw()
                p.click(CURSOR)
        try:
                pygame.draw.lines(window, "red", False, SMpoints, 5)
        except ValueError:
                pass
        #pygame.draw.circle(window, "white", SPLINE.layers[-1]["lines"][0].m(), 5)
        pygame.display.update()