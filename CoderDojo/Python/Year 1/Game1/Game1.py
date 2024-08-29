import sys, pygame
pygame.init
background = 29, 169, 212
size = width, height = 640, 400

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        

    screen.fill(background)
    pygame.display.flip()
