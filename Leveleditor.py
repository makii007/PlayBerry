#!/usr/bin/env python3
import pygame
import os
from settings import *

def init_display():
    global screen,tile , display, WINDOW_SIZE, level
    WINDOW_SIZE = (464*4, 256*2)
    screen = pygame.display.set_mode(WINDOW_SIZE, 600, 480)
    display = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]))
    tile = pygame.image.load("Sprites/Platforms/grass_small.png")


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

#Ebenen
levelX = 0
levelY = 0

map1 = map_to_list()
pygame.init()
init_display()

loop = 1
last_pos = x, y = pygame.mouse.get_pos()
#letter = "spazio"
#num_file = len(os.listdir())

#map_name = f"map{num_file}.png"
textMap=[]
oldTile = (-2, -2)

#Größe der Oberflächen
TileSize = (10,10)
#Oberflächen (Tuple mit einem Wert)
terrain = (2,)
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
                print("Y Ebene:wall " + str(levelY/32))


        #############################################################
        #               VERSCHIEDENE_OBERFLÄCHEN                    #
        #############################################################

            if keys[pygame.K_1]:
                tile = pygame.image.load("Sprites/Platforms/wall.png")
                terrain = (1,)
                print("Ground = wall")

            if keys[pygame.K_2]:
                tile = pygame.image.load("Sprites/Platforms/grass_small.png")
                print("Ground = grass_small")
                terrain = (2,)

            if keys[pygame.K_3]:
                tile = pygame.image.load("Sprites/Platforms/stone_small.png")
                print("Ground = stone_small")
                terrain = (3,)
            #if keys[pygame.K_2]:
            #    tile = pygame.image.load("Sprites/Platforms/Platform_grass_medium.png")
            #    TileSize = (20,10)

                            ##############
                            ##DELETE MAP##
            #########################################################

            if keys[pygame.K_d]:
                map1 = map_to_list()


        #############################################################
        #               MAP_SPEICHERUNG                             #
        #############################################################
            if keys[pygame.K_t]:
                textfile = open("levels/level_1", "w")
                for element in textMap:
                    #print(element)
                    element = element[::-1]

                    #print(element)
                    element = tuple(i*10 for i in element)
                    #add Tilesize + terrain to each element
                    element += TileSize
                    platform = str(element)
                    print(platform)
                    platform = platform.replace('(','').replace(' ', '').replace(')', ',_')
                    #textfile.write("240,500,220,10,_")
                    textfile.write(platform)
                textfile.close()
                print("LevelSaved")


        #############################################################
        #               MAUS-EVENTS                                 #
        #############################################################

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            x, y = int(x / 16), int(y / 16)

            row, col = y, x
            map1[row][col] = (y + levelY,x + levelX)

            map1[row][col] = map1[row][col] + terrain


            if oldTile != map1[row][col]:
                textMap.append(map1[row][col])
            oldTile = map1[row][col]
            #print (textMap)

        elif pygame.mouse.get_pressed()[2]:

            x, y = pygame.mouse.get_pos()
            x, y = int(x / 16), int(y / 16)
            row, col = y, x

            print(map1[row][col])
            map1[row][col] = " "
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
pygame.quit()
