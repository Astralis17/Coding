import pygame
pygame.init()

screen = pygame.display.set_mode([1366,768])

#Run until user asks to quit
running = True
while running:

    ##Did user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #background color
    screen.fill((22,80,20))

    #Draw solid blue circle
    pygame.draw.circle(screen, (0,0,255), (250,250), 100)
    pygame.draw.rect(screen, (0,2,2), pygame.Rect(30, 60, 70, 60))
    #Flip the display
    
    pygame.display.flip()

pygame.quit()