import pygame, random
# import aTools
from math import sin, cos, radians, floor
pygame.init()
pygame.font.init()

display = pygame.display.set_mode((800,600))
# monoFont = aTools.Pygame.font(20)
monoFont = pygame.font.SysFont("mono", 20, 0)
def midpoint(p1,p2):
        mx = (p1[0] + p2[0]) /2
        my = (p1[1] + p2[1]) /2
        return (mx, my)

class SceneObject:
        displayObj = display
        def tick(self):
                self.draw()

class Slider(SceneObject):
        fillValue = 0.5
        filledRange = 0
        filling:bool = False
        def __init__(self,position:tuple[int,int], dimensions:tuple[int,int], range:tuple[int,int]):
                self.position = position
                self.dimensions = dimensions
                self.range = range
                self.maxValue = abs(self.range[0] - self.range[1])
                self.rect = pygame.Rect(self.position[0], self.position[1], self.dimensions[0], self.dimensions[1])


        def onClick(self):
                print("clicked")


        def tick(self):
                
                self.draw()
                if self.rect.colliderect(cursor.boundingBox):
                        self.filling = True
                if self.filling and cursor.clicked["l"]:
                        cursorMovedX = cursor.position[0] - self.position[0]
                        self.fillValue = cursorMovedX/self.dimensions[0]
                        self.fillValue = 1 if self.fillValue>1 else 0 if self.fillValue <0 else self.fillValue
                        self.filledRange = (self.fillValue*self.maxValue) -self.maxValue/2
                        self.filledRange = floor(self.filledRange*100)/100

        def draw(self):
                self.textObject = monoFont.render(str(self.filledRange), True, "white")
                pygame.draw.rect(self.displayObj, (50,50,50), self.rect)
                scaledRect = self.rect.scale_by(self.fillValue,1).move((self.dimensions[0]*self.fillValue - self.dimensions[0])/2 ,0)
                pygame.draw.rect(self.displayObj, (120,150,250), scaledRect)
                self.displayObj.blit(self.textObject, self.rect)
                
class Cursor(SceneObject):
        def __init__(self):
                self.position = (0,0)
                self.boundingBox = pygame.Rect(self.position[0],self.position[1],10,10)
                self.clicked = {
                        "l":0,
                        "m":0,
                        "r":0,
                }
        
        def tick(self):
                self.position = pygame.mouse.get_pos()
                self.boundingBox = pygame.Rect(self.position[0],self.position[1],10,10)
                self.clicked["l"], self.clicked["m"], self.clicked["r"] = pygame.mouse.get_pressed()
                # self.draw()

        def draw(self):
                pygame.draw.rect(self.displayObj, "white", self.boundingBox)

class SolarPanel(SceneObject):
        photons = 0
        photonsPerSecond = 0
        photonRecord = [0 for i in range(100)]
        fillValue = 0
        def __init__(self, linkedSlider):
                self.linkedSlider = linkedSlider
                self.topline = ((325, 500),(475, 500))
                self.fulcrum = (midpoint(*self.topline)[0], 510)
                self.points = (self.topline[0], (self.topline[0][0], self.topline[0][1]+20), (self.topline[1][0], self.topline[1][1]+20), self.topline[1])
                self.textboxPosition = (5, 570)
                self.textBoxDimensions = (200, 25)
                self.textboxRect = pygame.Rect(*self.textboxPosition, *self.textBoxDimensions)

        def tick(self):
                self.fillValue = self.photonsPerSecond/20
                self.rotate()
                if ticks % 1000 == 0:
                        self.photonRecord.append(self.photons)
                        self.photons = 0
                        self.photonsPerSecond = sum(self.photonRecord[-24:])/25
                self.draw()
                

        def rotate(self):
                self.adjustedPoints = []
                angle = radians(self.linkedSlider.filledRange)
                for point in self.points:
                        x = point[0]-self.fulcrum[0]
                        y = point[1]-self.fulcrum[1]
                        X = x*cos(angle) - y*sin(angle) + self.fulcrum[0]
                        Y = y*cos(angle) + x*sin(angle) + self.fulcrum[1]

                        self.adjustedPoints.append((X, Y))
                self.adjustedTopline = (self.adjustedPoints[0], self.adjustedPoints[-1])

        def draw(self):
                self.textObject = monoFont.render(f"{self.photonsPerSecond}/s", True, "white")
                pygame.draw.polygon(self.displayObj, "white", self.adjustedPoints)
                pygame.draw.line(self.displayObj, "blue", *self.adjustedTopline, 5)

                pygame.draw.rect(self.displayObj, (50,50,50), self.textboxRect)
                scaledRect = self.textboxRect.scale_by(self.fillValue,1).move((self.textBoxDimensions[0]*self.fillValue - self.textBoxDimensions[0])/2 ,0)
                pygame.draw.rect(self.displayObj, (180,190,50), scaledRect)
                self.displayObj.blit(self.textObject, self.textboxRect)             


class Photon(SceneObject):
        speed = 3
        dead = False
        colour = "yellow"
        def __init__(self, unitVector, position):
                self.velVector = [dim * self.speed for dim in unitVector]
                self.position = list(position)
                self.rect = pygame.Rect(position[0], position[1]-9,2,10)

        def tick(self):
                for index, dimension in enumerate(self.velVector):
                        self.position[index] += dimension
                self.rect = pygame.Rect(self.position[0], self.position[1]-9,2,10)
                
                if self.position[1] > 600:
                        self.dead = True
                elif abs(self.position[0]-400) < 100:
                        self.colisionCheck()

                self.draw()

        def colisionCheck(self):
                if self.rect.clipline(*panel.adjustedTopline):
                        self.dead = True
                        self.colour = "red"
                        panel.photons += 1
        def draw(self):
                if renderPhotons:
                        pygame.draw.circle(self.displayObj, self.colour, self.position, 2)


class Star(SceneObject):
        photons = []
        angle = 0.8
        def __init__(self, position:tuple[int,int]=None, size=100):
                self.size = size
                if position:
                        self.position = position
                else:
                        self.position = (self.displayObj.get_width()/2, int(50-size))

        def tick(self):
                self.draw()
                self.emitPhoton()
                toRemove = []
                for index, photon in enumerate(self.photons):
                        photon.tick()
                        if photon.dead:
                                toRemove.append(photon)
                toRemove.reverse()
                for index in toRemove:
                        self.photons.remove(index)
                

        def draw(self):
                pygame.draw.circle(self.displayObj, "yellow", self.position, self.size)

        def emitPhoton(self):
                direction = [
                        random.random()*self.angle,
                        1
                ]
                direction = [i/max(direction) for i in direction]
                direction[0] *= random.choice([1,-1])
                
                self.photons.append(Photon(direction, self.position))



cursor = Cursor()
slider = Slider((595,570), (200,25), (-90,90))
panel = SolarPanel(slider)
sun = Star()
clickables = [] #list of objects that are clickable
tickables = [panel, sun, slider, cursor, ]
clock = pygame.time.Clock()



sim = True
ticks = 0
tickTime = 10
renderPhotons = True
while sim:
        clock.tick()
        pygame.time.delay(tickTime-clock.get_time())
        ticks = (ticks+tickTime)%1000

        display.fill((20,20,20))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sim = False
                elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_0]:
                                slider.filledRange = 0
                        elif keys[pygame.K_1]:
                                slider.filledRange = 15
                        elif keys[pygame.K_2]:
                                slider.filledRange = 30
                        elif keys[pygame.K_3]:
                                slider.filledRange = 45
                        elif keys[pygame.K_4]:
                                slider.filledRange = 60
                        elif keys[pygame.K_5]:
                                slider.filledRange = 75
                        elif keys[pygame.K_MINUS]:
                                if slider.filledRange > 90:
                                        slider.filledRange *= -1
                                else:
                                        slider.filledRange *= -1
        
                

        for object in tickables:
                object.tick()
        pygame.display.flip()