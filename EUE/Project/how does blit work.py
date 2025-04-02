import pygame
G = 0
W = 1




tilesize = 32
mapwidth = 4
mapheight = 4

pygame.init()

image = pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Water1.png")
image2 = pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 0.png")
image = pygame.transform.scale(image, (64,64))
display = pygame.display.set_mode((832, 416))


run = True
while run:
        display.blit(image, (10, 200))
        display.blit(image2, (10, 200))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()