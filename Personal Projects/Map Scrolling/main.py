import pygame

class world:
        x = 0
        y = 0
        zoom = 100

class POI:
        def __init__(self, name, x, y, boundingBox):
                self.name = name
                self.x = x
                self.y = y
                self.boundingBox = (boundingBox[0], boundingBox[1])

        def draw(self, surface, offset):
                x1 = self.boundingBox[0][0] + offset[0] + self.x
                y1 = self.boundingBox[0][1] + offset[1] + self.x
                x2 = self.boundingBox[0][0] - self.boundingBox[1][0]
                y2 = self.boundingBox[0][1] - self.boundingBox[1][0]
                pygame.draw.rect(surface, (30,30,200), (x1,y1,x2,y2))
world = world()


obj = POI("Test", 100, 100, ((-50, -50),(50, 50)))

pygame.init()

window = pygame.display.set_mode((960, 520))


run = True
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False



        obj.draw(window, (world.x, world.y))
        pygame.display.update()
pygame.quit()