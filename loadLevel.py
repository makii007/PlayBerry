#!/usr/bin/env python3
import pygame


def loadMap(mapId):
    if mapId == "Tutorial":
        f = open('levels/level_tutorial')
    elif mapId == "1":
        f = open('levels/level_1')
    PLATFORM_LIST = []
    levelText = f.read()
    print(levelText)
    stringNumber = ''
    x=0
    y=0
    z=0
    w=0
    img = 0
    i = 0
    for element in levelText:
        if element == "_":
            PLATFORM_LIST.append((img,x*2,y*2,z*2,w*2))
            x=0
            y=0
            z=0
            w=0
            i=0
        else:
            if element == ',':
                #print(stringNumber)
                if i == 0:
                    img = int(stringNumber)
                    #print ("x: ")
                    #print(stringNumber)
                if i == 1:
                    x = int(stringNumber)
                    #print ("y: ")
                    #print(stringNumber)
                if i == 2:
                    y = int(stringNumber)
                    #print ("z: ")
                    #print(stringNumber)
                if i == 3:
                    z = int(stringNumber)
                    #print ("w: ")
                    #print(stringNumber)
                if i == 4:
                    w = int(stringNumber)
                    #print(stringNumber)
                i += 1
                stringNumber = ''
            else:
                stringNumber += element
    return PLATFORM_LIST
    #print(PLATFORM_LIST)
