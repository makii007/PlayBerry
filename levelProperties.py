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
        goblinList = [(3400, 1820),(3500,1820)]

    elif mapId == "1":
        #goblinList = [(250, 10), (255, 10), (260, 10),(265, 10), (270, 10), (275, 10),(280, 10), (285, 10), (290, 10),(295, 10), (300, 10), (305, 10),(310, 10), (315, 10), (320, 10)]
        goblinList = [(250,10)]
    return goblinList
