import pygame, random
from math import dist
from os import startfile
pygame.init()

windowDimensions = (1080, 720)
display = pygame.display.set_mode(windowDimensions)

class cursor:
    pressed = False
    def __init__(self, display):
        self.position = (0,0)
        self.display = display
        self.rect = pygame.Rect(self.position[0],self.position[1],5,5)

    def tick(self, mouse:pygame.mouse):
        self.position = mouse.get_pos()
        self.pressed = mouse.get_pressed(3)[0]
        self.rect = pygame.Rect(self.position[0]-2.5,self.position[1]-2.5,5,5)
        pygame.draw.rect(self.display, "white", self.rect)

class Button:
    def PASS(self):
        return

    def __init__(self, window, link, hoverFunction=PASS, clickFunction=PASS, ):
        self.display = window
        self.onHover = hoverFunction
        self.onClick = clickFunction
        self.link = link


class rectButton(Button):
    displayedPage = 0
    def init(self, rect, page):
        self.colour = random.choice(["red", "blue", "yellow", "purple", "green"])
        self.page = page
        if type(rect) == tuple:
                rect = pygame.Rect(rect)
        self.rect = rect
        self.position = rect.topleft

        return self
    def intersect(self, cursor:cursor):
        if self.displayedPage != self.page:
             return

        if self.rect.colliderect(cursor.rect):
            if cursor.pressed:
                self.onClick(self.link)
            else:
                self.onHover(self)
    def draw(self, page):
        self.displayedPage = page
        if page == self.page:
                pygame.draw.rect(self.display, self.colour, self.rect, 0, 15, 15, 15, 15)

def openLink(link):
     print("AGH!")
     startfile(link)




button = rectButton(display, clickFunction=openLink, link="C:/Users/Public/Desktop/Audacity.lnk")
button.init((300,100, 200, 150),0)
Cursor = cursor(display)

run = True
pygame.mouse.set_visible(False)
while run:
        display.fill("black")



        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        button.draw(0)


        button.intersect(Cursor)

        Cursor.tick(pygame.mouse)
        pygame.display.update()