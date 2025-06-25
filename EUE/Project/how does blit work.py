import pygame, aTools
G = 0
W = 1




tilesize = 32
mapwidth = 4
mapheight = 4

pygame.init()

image = pygame.image.load(aTools.localPath("Nomekop/Assets/Tiles/Water1.png"))
image2 = pygame.image.load(aTools.localPath("Nomekop/Assets/Tiles/Grass0 - 0.png"))
image = pygame.transform.scale(image, (64,64))
display = pygame.display.set_mode((832, 416),pygame.SRCALPHA)

tS = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.polygon(tS, pygame.Color(225, 125, 20, 127), (
        (0, tS.get_height()/2),
        (tS.get_width(), 0),
        (tS.get_width(), tS.get_height())
        ))

run = True
while run:
        display.blit(image, (50, 50))
        display.blit(image2, (10, 50))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        display.blit(tS, (10, 10))
        pygame.display.update()