#!/usr/bin/env python3
import pygame as pg
vec = pg.math.Vector2                               #2D Vector

def loadPlayerProperties(mapId):
    if mapId == "Tutorial":
        PlayerStartPosition = vec(230, 10)

    elif mapId == "1":
        PlayerStartPosition = vec(10, 10)
    return PlayerStartPosition

def loadGoblinProperties(mapId):
    if mapId == "Tutorial":
        goblinList = [(3400, 1820)]

    elif mapId == "1":
        #goblinList = [(250, 10), (270, 10), (310, 10)]
        goblinList = [(250,10)]
    return goblinList
