#!/usr/bin/env python3
import pygame
import os


def init_display():
    global screen, tile, display, WINDOW_SIZE, level
    WINDOW_SIZE = (464*4, 256*2)
    screen = pygame.display.set_mode(WINDOW_SIZE, 600, 480)
    display = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]))
    tile = pygame.image.load("Sprites/Platforms/wall.png")


def tiles(map1):
    global tile
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c != " ":
                display.blit(tile, (x * 16, y * 16))


def map_to_list():
    map1 = "" + " " * 27 * 20 + "w\n"
    #map1 = ""
    map1 = map1 * 60
    map1 = map1.splitlines()
    map2 = []
    for n, line in enumerate(map1):
        map2.append(list(map1[n]))
    return map2

levelX = 0
levelY = 0
map1 = map_to_list()
pygame.init()
init_display()
loop = 1
#levelX
last_pos = x, y = pygame.mouse.get_pos()
letter = "spazio"
num_file = len(os.listdir())

map_name = f"map{num_file}.png"
textMap=[]
oldTile = (-2, -2)

ebene = 0
while loop:

    display.fill((0, 0, 0))
    tiles(map1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            #if event.key == K_s:
            if keys[pygame.K_s]:
                pygame.image.save(screen, map_name)
                #os.startfile(map_name)

        #############################################################
        #               EBENEN                                      #
        #############################################################
            if keys[pygame.K_RIGHT]:
                map1 = map_to_list()
                levelX += 116
                print("X Ebene: " + str(levelX/116))
            if keys[pygame.K_LEFT]:
                map1 = map_to_list()
                levelX -= 116
                print("X Ebene: " + str(levelX/116))
            if keys[pygame.K_UP]:
                map1 = map_to_list()
                levelY -= 32
                print("Y Ebene: " + str(levelY/32))
            if keys[pygame.K_DOWN]:
                map1 = map_to_list()
                levelY += 32
                print("Y Ebene: " + str(levelY/32))


            if keys[pygame.K_d]:
                map1 = map_to_list()
            if keys[pygame.K_t]:



                textfile = open("levels/level_1", "w")
                for element in textMap:
                    element = element[::-1]
                    #print(element)
                    element = tuple(i*10 for i in element)
                    TileSize = (10,10)
                    element += TileSize
                    platform = str(element)
                    platform = platform.replace('(','').replace(' ', '').replace(')', ',_')
                    textfile.write("240,500,220,10,_")
                    textfile.write(platform)
                textfile.close()
                print("LevelSaved")




        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            # You divide by 32 for its scaled (pygame.transform.scale)
            x, y = int(x / 16), int(y / 16)
            # x and y are col and row (the opposite)
            row, col = y, x
            map1[row][col] = (y + levelY,x + levelX)
            if oldTile != map1[row][col]:
                textMap.append(map1[row][col])
            oldTile = map1[row][col]
            print (textMap)
        elif pygame.mouse.get_pressed()[2]:

            x, y = pygame.mouse.get_pos()
            # You divide by 32 for its scaled (pygame.transform.scale)
            x, y = int(x / 16), int(y / 16)
            # x and y are col and row (the opposite)
            row, col = y, x


            print(map1[row][col])
            map1[row][col] = " "
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
pygame.quit()
