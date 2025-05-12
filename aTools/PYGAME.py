import pygame, random
pygame.init()


windowDim = (1080,720)
window = pygame.display.set_mode(windowDim)

def PASS(self):
    return

class cursor:
    pressed = False
    def __init__(self):
        self.position = (0,0)
        self.rect = pygame.Rect(self.position[0],self.position[1],5,5)
        
    def tick(self, mouse:pygame.mouse):
        self.position = mouse.get_pos()
        self.pressed = mouse.get_pressed(3)[0]
        self.rect = pygame.Rect(self.position[0],self.position[1],5,5)

class button:
    colour = "yellow"
    window = window
    def __init__(self, rect:pygame.Rect, hoverFunction=PASS, clickFunction=PASS):
        self.position = rect.topleft
        self.rect = rect
        self.onHover = hoverFunction
        self.onClick = clickFunction
    
    def intersect(self, cursor:cursor):
        if self.rect.colliderect(cursor.rect):
            if cursor.pressed:
                self.onClick(self)
            else:
                self.onHover(self)
            
        
    def draw(self):
        pygame.draw.rect(self.window, self.colour, self.rect)

mouse = cursor()
boxes = [
    button(
    pygame.Rect(random.random()*windowDim[0],random.random()*windowDim[1], 50, 50),
    ) for x in range(4)]


run=True
while run:
    mouse.tick(pygame.mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    print(cursor.pressed)
    for box in boxes:
        box.intersect(mouse)
        box.draw()

    pygame.display.update()