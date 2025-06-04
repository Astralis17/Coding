import pygame
pygame.init()
window = pygame.display.set_mode((960, 520))



class POI:
        def __init__(self, name, x, y, boundingBox):
                self.name = name
                self.x = x
                self.y = y
                self.boundingBox = (boundingBox[0], boundingBox[1])



        def draw(self, surface, offset):
                self.x1 = self.boundingBox[0][0] + offset[0] + self.x
                self.y1 = self.boundingBox[0][1] + offset[1] + self.x
                self.x2 = self.boundingBox[0][0] - self.boundingBox[1][0]
                self.y2 = self.boundingBox[0][1] - self.boundingBox[1][0]
                pygame.draw.rect(surface, (30,30,200), (self.x1,self.y1,self.x2,self.y2))
class world:
        x = 100
        y = 100
        zoom = 100
        POIs = []

        def __init__(self, display):
                self.display = display

        def addPOI(self, poi:POI):
                self.POIs.append(poi)


        def tick(self):
                self.position = [self.x, self.y]
                for POI in self.POIs:
                        POI.draw(self.display, self.position)




obj = POI("Test", 100, 100, ((50, 50),(-50, -50)))
gameWorld = world(window)
gameWorld.addPOI(obj)



run = True
while run:
        window.fill("red")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False


        gameWorld.tick()
        pygame.display.flip()
pygame.quit()