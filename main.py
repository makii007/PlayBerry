#!/usr/bin/env python3
#First Platformer

import pygame as pg                 #pygame alias pygame
import random
from settings import *
from sprites import *
from loadLevel import *
from camera import *
from Files import *



class Game:
    def __init__(self):               #startup initializes(Game Window)

        pg.init() 											#starts Pygame
        pg.mixer.init() 									#Mixer ist für die Gamesounds
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()						#Kontrolliert die Geschwindigkeit des Spiels und regelt die FPS
        self.running = True
        pg.mouse.set_visible(False)
        keys=pygame.key.get_pressed()

        self.mapId = "Tutorial"
        #JOYSTICK implementieren

        #self.joystick = pg.joystick.Joystick(0)
        #self.joystick.init()

    def new(self, mapId):                  #resets the Game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.goblinSprites = pg.sprite.Group()
        self.textSprites = pg.sprite.Group()
        self.objects = pg.sprite.Group()

        self.platformList = loadMap(mapId)
        for plat in self.platformList:
            p = Platform(*plat)                         # * --> explode into all components
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.camera = Camera(WIDTH*2,HEIGHT)

        # ADD PLAYER
        self.Player = Player (self, loadPlayerProperties(mapId), mapId)        #Um dem Player alle Gamevariablen mitzugeben
        self.all_sprites.add(self.Player)

        # ADD OBJECTS
        self.door = randomObjects(objDoor, doorProperties(mapId))
        self.objects.add(self.door)
        # ADD GOBLIN

        self.Goblins = []

        for goblin in loadGoblinProperties(mapId):

            g = Goblin(self, *goblin)
            self.Goblin = Goblin(self, *goblin)
            self.goblinSprites.add(self.Goblin)
            self.Goblins.append(self.Goblin)

        #ADD TEXT
        if mapId == "Tutorial":
            self.tutText1 = Text(tut1, 220, 0, 20, 20)
            self.tutText2 = Text(tut2, 620, 300, 20, 20)
            self.tutText3 = Text(tut3, 730, 1600, 20, 20)
            self.tutText4 = Text(tut4, 1100, 2000, 20, 20)
            self.tutText5 = Text(tut5, 1400, 1600, 20, 20)
            self.tutText6 = Text(tut6, 2300, 1600, 20, 20)
            self.tutText7 = Text(tut7, 2600, 2000, 20, 20)

            self.textSprites.add(self.tutText1)
            self.textSprites.add(self.tutText2)
            self.textSprites.add(self.tutText3)
            self.textSprites.add(self.tutText4)
            self.textSprites.add(self.tutText5)
            self.textSprites.add(self.tutText6)
            self.textSprites.add(self.tutText7)
        self.run()


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()                 #Game Loop

    def update(self):               #GameLoop - update
        #print(self.Player.pos)
        self.all_sprites.update()
        self.goblinSprites.update()
        self.platforms.update()
        self.Player.isGrounded()
        self.Player.platformCollide(self.platforms)
        for goblin in self.Goblins:
            goblin.platformCollide(self.platforms)
            if not goblin.dead:
                if(self.Player.pos.distance_to(goblin.pos)) < 100:
                    distance = self.Player.pos.distance_to(goblin.pos)
                    goblin.distance(self.Player.pos, distance)
                    if goblin.punch == True:
                        self.Player.playerHit()
                        goblin.punch = False
                else:
                    goblin.walkLeft = False
                    goblin.walkRight = False

        if self.Player.SwordAttack:
            pg.sprite.spritecollide(self.Player, self.goblinSprites, True, pg.sprite.collide_mask)
        if self.Player.dead:
            g.show_go_screen()

        if pg.sprite.spritecollide(self.Player, self.objects, False):
            if self.mapId == "Tutorial":
                self.mapId = "1"
            elif mapId == "1":
                print("end")
            g.new(self.mapId)

        self.camera.update(self.Player)

        #if  self.Player.pos.x > 3700 and self.Player.pos.y > 1800:

        if self.Player.vel.y > 100:
            g.new(self.mapId)

    def events(self):               #GameLoop - events
        for event in pg.event.get():					#Damit Inputs sofort verarbeitet werden
    		#check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            #if event.type == pg.JOYBUTTONDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                #if self.joystick.get_button(0):
                    self.Player.jump()

            #if event.type == pg.JOYBUTTONUP:
            #    if self.joystick.get_button(0):
            #        self.Player.jumpBreak()

            #if self.joystick.get_button(1):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                	self.Player.SwordAttack = True




    def draw (self):                #GameLoop - Draw
        global walkFrame
        self.screen.fill(BLACK)									#Double Buffering	--> Drawing ist sehr langsam deshalb wird während einer Szene
    														#, im Hintergrund die nächste gezeichnet(Dann wird die Szene "geflippt

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.goblinSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.textSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.objects:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pg.display.flip()

    def show_start_screen(self):
        print("startscreen")
        pass

    def show_go_screen(self):
        #Game Over screen
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new("Tutorial")
    g.show_go_screen()

pg.quit()
