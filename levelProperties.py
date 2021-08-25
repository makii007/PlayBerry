#!/usr/bin/env python3
import pygame as pg
vec = pg.math.Vector2                               #2D Vector

def loadPlayerProperties(mapId):
    if mapId == "Tutorial":
        PlayerStartPosition = vec(230, 230)

    elif mapId == "1":
        PlayerStartPosition = vec(20, 575)
    return PlayerStartPosition

def loadGoblinProperties(mapId):
    if mapId == "Tutorial":
        goblinList = [(2685,1860),(3156,1860)]

    elif mapId == "1":
        goblinList = [(345, 580), (828, 340), (1088, 540),(2400, 580), (2946, 380), (5110, 560),(5185, 560), (5272, 560), (5411, 560),(5476, 560), (5560, 560), (5687, 560)]
    return goblinList

def doorProperties(mapId):
    if mapId == "Tutorial":
        position = vec(3640, 1840)
    elif mapId == "1":
        position = vec(0,0)
    return position
