#!/usr/bin/env python3
import pygame

f = open('levels/level_1')
PLATFORM_LIST_AUTO = []
levelText = f.read()
print(levelText)
#number = 0
stringNumber = ''
x=0
y=0
z=0
w=0
i = 0
for element in levelText:
    if element == "_":
        PLATFORM_LIST_AUTO.append((x,y,z,w))
        x=0
        y=0
        z=0
        w=0
        i = 0
    else:
        if element == ',':
            #print(stringNumber)
            if i == 0:
                x = int(stringNumber)
                print ("x: ")
                print(stringNumber)
            if i == 1:
                y = int(stringNumber)
                print ("y: ")
                print(stringNumber)
            if i == 2:
                z = int(stringNumber)
                print ("z: ")
                print(stringNumber)
            if i == 3:
                w = int(stringNumber)
                print ("w: ")
                print(stringNumber)
            i += 1
            stringNumber = ''
        else:
            stringNumber += element
print(PLATFORM_LIST_AUTO)
