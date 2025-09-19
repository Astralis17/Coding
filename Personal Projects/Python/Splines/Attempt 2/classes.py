import pygame, aTools, random



class point:
        def __init__(self, pos, colour="White"):
                self.x = pos[0]
                self.y = pos[1]
                self.colour = pygame.Color(colour)
        def __call__(self):
                return [self.x, self.y]
        def draw(self, display):
                pygame.draw.circle(display, self.colour, (self.x, self.y), 5)

class line:
        def __init__(self, p1,p2, thickness=3):
                self.p1:point = p1
                self.p2:point = p2
                self.colour = aTools.randomRGB()
                self.thickness = thickness

        def draw(self, display):
                pygame.draw.line(display, self.colour, self.p1(), self.p2(), self.thickness)


class BezierCurve:
        def __init__(self, points:list[point], display):
                self.basePoints = points
                self.display = display
                self.t = 0
                self.colour = "Red"
                self.SMPointsNeeded = True

                random.seed(aTools.seedGen(seedInput=""))
                self.seed = aTools.seedGen(seedInput="")


                lineCount = len(self.basePoints) -1
                self.baseLines: list[line] = [line(self.basePoints[i], self.basePoints[i+1]) for i in range(lineCount)]

                self.subPoints: list[point] = []
                self.subLines: list[line] = []
                self.SMpoints:list[point] = []

        def findSubPoints(self, t:float=None):
                if t is None:t = self.t

                random.seed(self.seed)
                self.subPoints = [point(aTools.lerp(i.p1(), i.p2(), t), i.colour) for i in self.baseLines]

                lineCount = len(self.subPoints) -1
                self.subLines =  [line(self.subPoints[i], self.subPoints[i+1], 2) for i in range(lineCount)]

                for i in self.subLines:
                        self.subPoints.append(point(aTools.lerp(i.p1(), i.p2(), t), i.colour))

                self.subLines.append(line(self.subPoints[-2], self.subPoints[-1]))
                self.subPoints.append(point(aTools.lerp(self.subLines[-1].p1(), self.subLines[-1].p2(), t), self.subLines[-1].colour))

        def drawPoints(self):
                self.points = self.basePoints + self.subPoints
                for p in self.points:
                        p.draw(self.display)
        def drawLines(self):
                self.lines = self.baseLines + self.subLines

                for line in self.lines:
                        line.draw(self.display)

        def draw(self):
                self.findSubPoints()
                self.drawLines()
                self.drawPoints()
                self.SmoothLinePoints()

        def SmoothLinePoints(self):
                if self.SMPointsNeeded:
                        self.SMPointsNeeded = False
                        self.SMpoints:list[point] = []
                        for t in aTools.Math.fRange(0, 1, 0.001):
                                self.findSubPoints(t)
                                self.SMpoints.append(self.subPoints[-1])
                else:
                        pygame.draw.lines(self.display, self.colour, False, [p() for p in self.SMpoints])

