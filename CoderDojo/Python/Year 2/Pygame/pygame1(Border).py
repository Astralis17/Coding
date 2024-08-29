import pygame
pygame.init()
window = pygame.display.set_mode((800, 500))

squarex = 350
squarey = 200
squarewidth = 100
squareheight = 100
speed = 0.5

run = True
while run:
    pygame.time.delay(1)
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        squarey = squarey - speed
    if keys[pygame.K_DOWN]:
        squarey = squarey + speed
    if keys[pygame.K_RIGHT]:
        squarex = squarex + speed
    if keys[pygame.K_LEFT]:
        squarex = squarex - speed
    if squarex >= 701:
        squarex = 700
    if squarex <= -1:
        squarex = 0
    if squarey >= 401:
        squarey = 400
    if squarey <= -1:
        squarey = 0


    pygame.draw.rect(window,(0, 100, 100), (squarex, squarey, squarewidth, squareheight ))
    pygame.draw.rect(window,(0, 0, 0), (squarex + 20, squarey + 30, 10, 10  ))
    pygame.draw.rect(window,(0, 0, 0), (squarex + 70, squarey + 30, 10, 10 ))
    pygame.display.update()
pygame.quit()