import pygame, random
from math import dist
pygame.init()
class cursor:
    pressed = False
    def __init__(self):
        self.position = (0,0)
        self.rect = pygame.Rect(self.position[0],self.position[1],5,5)
        
    def tick(self, mouse:pygame.mouse):
        self.position = mouse.get_pos()
        self.pressed = mouse.get_pressed(3)[0]
        self.rect = pygame.Rect(self.position[0],self.position[1],5,5)


class Button:
    def PASS(self):
        return
    def __init__(self, window, hoverFunction=PASS, clickFunction=PASS):
        self.colour = random.choice(["red", "blue", "yellow", "purple", "green"])
        self.display = window
        self.onHover = hoverFunction
        self.onClick = clickFunction

class rectButton(Button):
    def init(self, rect:pygame.Rect):
        self.position = rect.topleft
        self.rect = rect
        return self
    def intersect(self, cursor:cursor):
        if self.rect.colliderect(cursor.rect):
            if cursor.pressed:
                self.onClick(self)
            else:
                self.onHover(self)
    def draw(self):
        pygame.draw.rect(self.display, self.colour, self.rect)

class circleButton(Button):
    def init(self, position, radius):
        self.position = position
        self.radius = radius
        return self
    def intersect(self, cursor:cursor):
        if dist(cursor.rect.topleft, self.position) <=self.radius:
            if cursor.pressed:
                self.onClick(self)
            else:
                self.onHover(self)
    def draw(self):
        pygame.draw.circle(self.display, self.colour, self.position, self.radius)