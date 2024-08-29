import sys, pygame
pygame.init()
screen = pygame.display.set_mode([1366,650])
screen.fill((22,80,20))
ball = pygame.image.load("intro_ball.png")
ballrect = ball.get_rect()
def right():
    pygame.ball.move(right)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
#        if event.key == pygame.K_RIGHT :
pygame.display.flip