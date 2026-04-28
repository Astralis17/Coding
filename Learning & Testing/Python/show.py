import pygame

import Dictionary

pygame.init()

Row1 = [Dictionary.Blank, Dictionary.Teleporter, Dictionary.Relics]
Row2 = [Dictionary.CharSelect, Dictionary.Main, Dictionary.Settings]
player = Dictionary.player

Coordinates = [Row1, Row2]

windows = {
"height" : 700,
"width" : 1000,
"border" : 100
}
window = pygame.display.set_mode((windows["width"], windows["height"]))


x = 1
y = 1
i = 0
run = True

def input(x, y, keys):
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    return x, y

def RoomChange(x, y, playerx, playery, Coordinates):
    if Coordinates[y][x]["Down"]  and playerx >= (windows["width"]/2-15)   and playerx <= (windows["width"]/2+15)  and playery >= windows["height"] -1:
        y += 1
        playery = 5

    if Coordinates[y][x]["Down"]:
        if not playerx >= (windows["width"]/2-15):
            print("Check left needed")

        if not playerx <= (windows["width"]/2+15):
            print("Check right needed")

        if not playery >= windows["height"] -1:
            print("Check move needed")



    if Coordinates[y][x]["Up"]    and playerx >= (windows["width"]/2-15)   and playerx <= (windows["width"]/2+15)  and playery <= 0:
        y -= 1
        playery = windows["height"] - 5

    if Coordinates[y][x]["Right"] and playery >= (windows["height"]/2-15)  and playery <= (windows["height"]/2+15) and playerx >= (windows["width"] - windows["border"]):
        x += 1
        playerx = 5

    if Coordinates[y][x]["Left"]  and playery >= (windows["height"]/2-15)  and playery <= (windows["height"]/2+15) and playerx >= windows["width"]:
        x -= 1
        playerx = (windows["width"] - windows["border"])

    return x, y, playerx, playery

def Border(x, y, windows):
    x = player["x"]
    y = player["y"]
    playerwidth = player["dimensions"]["width"]
    playerheight = player["dimensions"]["height"]


    if x < windows["border"]:
        x += 5
        x = windows["border"]
    if x > windows["width"] - windows["border"] - playerwidth:
        x = windows["width"] - windows["border"] - playerwidth
    if y < 0:
        y = 0
    if y > windows["height"] - playerheight:
        y = windows["height"]- playerheight
    return x, y

def CoordinateCheck(player, x, y, i):
    if i >= 40:
        print(""); print(""); print(""); print(""); print(""); print(""); print(""); print("")
        print("Player x:", player["x"])
        print("Player y:", player["y"])
        print("Coordinates:", x, y)
        i = 0
    i += 1
    return i

while run:
    pygame.time.delay(10)
    window.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    pygame.draw.rect(window, (255, 255, 255), (windows["border"], 0, (windows["width"]-(windows["border"])*2), windows["height"]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    x, y, player["x"], player["y"] = RoomChange(x, y, player["x"], player["y"], Coordinates)

    player["x"], player["y"] = input(player["x"], player["y"], keys)

    player["x"], player["y"] = Border(player["x"], player["y"], windows)

    i = CoordinateCheck(player, x, y, i)
    pygame.draw.rect(window, (92, 51, 123), (player["x"], player["y"], player["dimensions"]["width"], player["dimensions"]["height"]))



    pygame.display.update()
pygame.quit()