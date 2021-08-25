#!/usr/bin/env python3
# Hier organisieren wir unsere sprites
import pygame as pg
from settings import *

from levelProperties import *
from Files import *
#from main import *
vec = pg.math.Vector2                               #2D Vector

class Player(pg.sprite.Sprite):
    def __init__(self, game, pos, mapId):
        self.game = game
        self.playerWidth = 20
        self.playerHeight = 32

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.playerWidth,self.playerHeight))
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        global startingPosition

        self.pos = pos
        startingPosition = loadPlayerProperties(mapId)

        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumps = 1
        self.lifes = 3
        self.dead = False

        self.grounded = False

        #Variablen für Animationen
        self.hit = False
        self.walking = False
        self.jumping = False
        self.currentFrame = 0
        self.lastUpdate = 0

        self.SwordAttack = False
        self.SwordHit = False
        self.FrameFromZero = 0

        self.awake = True

        self.idlingLeft = False
        self.idlingRight = False

        self.walking = False
        self.walkLeft = False
        self.walkRight = False

        #JOYSTICK implementieren

        #self.joystick = pg.joystick.Joystick(0)
        #self.joystick.init()

    def jump(self):
        # Jump wird nur ausgeführt wenn sich etwas unter dem Spieler befindet
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = JUMPHIGHT
            self.jumps = 1
        elif not hits and self.jumps > 0:
            self.vel.y = JUMPHIGHT
            self.jumps -=1

    def jumpBreak(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
                self.jumping = False

    def isGrounded(self):

        self.hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if self.hits:
            self.grounded = True
        else:
            self.grounded = False
        return self.grounded

    def playerHit(self):
        print (self.lifes)
        if not self.dead:
            self.lifes -= 1
            if self.lifes > 0:
                self.hit = True
            else:
                self.dead = True


    def update(self):
        #if self.joystick.get_button(9):
        #    pg.quit()
        keys=pygame.key.get_pressed()
        self.acc = vec(0, PLAYER_GRAV)
        #if self.joystick.get_button(13) and not self.SwordAttack:
        if keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and not self.SwordAttack:
            self.walkLeft = True
            self.walkRight = False
            self.idlingLeft = True
            self.idlingRight = False
            self.acc.x = -PLAYER_ACC

        #if self.joystick.get_button(14) and not self.SwordAttack:
        if keys[pg.K_RIGHT] and not keys[pg.K_LEFT] and not self.SwordAttack:
            self.idlingRight = True
            self.idlingLeft = False
            self.walkRight = True
            self.walkLeft = False
            self.acc.x = PLAYER_ACC
        #elif not self.joystick.get_button(13) and not self.joystick.get_button(14):
        elif not keys[pg.K_RIGHT] and not keys[pg.K_LEFT]:
            self.walkLeft = False
            self.walkRight = False

        self.animate()

        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        #Player loopt den screen
    #    if self.pos.x > WIDTH:
    #        self.pos.x = 0
    #    if self.pos.x < 0:
    #        self.pos.x = WIDTH
        #self.rect.center = self.pos                    #Um Kollisionen mit Platformen einfacher zu machen (Position ist nun unten in der Mitte und nicht Center)
        self.rect.midbottom = self.pos

    def platformCollide(self, platforms):
        self.hits = pg.sprite.spritecollide(self, platforms, False)
        if self.hits:                                        #Checkt ob Player Platform berührt
            if self.rect.bottom < self.hits[0].rect.bottom: #self.Player.vel.y > 0 and
                self.pos.y = self.hits[0].rect.top# - self.Player.rect.height/2
                self.vel.y = 0
                self.jumping = False

            if self.vel.y < 0:
                self.top = self.hits[0].rect.bottom
                self.vel.y = 0

            for hit in self.hits:
                if hit.rect.left and self.pos.y > hit.rect.y:
                    self.vel.x = -2
                elif hit.rect.right and self.pos.y > hit.rect.y:
                    self.vel.x = +2

    def animate(self):
        now = pygame.time.get_ticks()                   #Zeit seit Spielstart

    ########Awake################

        if self.awake:
            self.walkRight = False
            self.walkLeft = False
            if now - self.lastUpdate > 100:
                self.lastUpdate = now
                self.FrameFromZero = (self.FrameFromZero + 1) % len(PlayerAwake)
                self.image = PlayerAwake[self.FrameFromZero]

                if self.FrameFromZero == len(PlayerAwake)-1:
                    self.awake = False
                    self.idlingRight = True
                    self.lifes = 3

        ###### WALKING #######

        if ((self.walkRight or self.walkLeft) and self.grounded)and not self.SwordAttack:
            if now - self.lastUpdate > 50:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(PlayerWalkRight)

                if self.walkRight:
                    self.image = PlayerWalkRight[self.currentFrame]
                if self.walkLeft:
                    self.image = pygame.transform.flip(PlayerWalkRight[self.currentFrame], True, False)             # Flip Horizontal = True; Flip Vertical = False

        ####### JUMPING ###########

        if self.jumping and self.vel.y < 0:
            if now - self.lastUpdate > 50:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(RightUpJump)
                if self.jumping and self.vel.y < 0:
                    if self.vel.x < 0:
                        self.image = pygame.transform.flip(RightUpJump[self.currentFrame], True, False)
                    else:
                        self.image = RightUpJump[self.currentFrame]


        ####### FALLING #########
        if self.vel.y > 0:
            if now - self.lastUpdate > 50:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(RightUpJump)
                if self.vel.x < 0:
                    self.image = pygame.transform.flip(RightDownJump[self.currentFrame], True, False)
                else:
                    self.image = RightDownJump[self.currentFrame]

    ########Hitting################

        if self.hit:
            self.walkRight = False
            self.walkLeft = False
            if now - self.lastUpdate > 30:
                self.lastUpdate = now
                self.FrameFromZero = (self.FrameFromZero + 1) % len(PlayerHit)
                self.image = PlayerHit[self.FrameFromZero]

                if self.FrameFromZero == len(PlayerHit)-1:
                    FrameFromZero = 0
                    self.hit = False

        ######## Sword Attack #########

        if (self.SwordAttack or (self.SwordAttack and self.walking))and self.grounded:
            if now - self.lastUpdate > 100:
                self.lastUpdate = now
                self.FrameFromZero = (self.FrameFromZero + 1) % len(SwordAttack)
                if self.idlingRight:
                    self.image = SwordAttack[self.FrameFromZero]
                if self.idlingLeft:
                    self.image = pygame.transform.flip(SwordAttack[self.FrameFromZero], True, False)

                if self.FrameFromZero == len(SwordAttack)-1:
                    self.SwordAttack = False
                    self.walkRight = False
            self.mask = pg.mask.from_surface(self.image)
            #elif self.jumping and self.vel.y > 0:


        ########Dying################

        if self.dead:
            self.walkRight = False
            self.walkLeft = False
            if now - self.lastUpdate > 100:
                self.lastUpdate = now
                self.FrameFromZero = (self.FrameFromZero + 1) % len(PlayerDying)
                self.image = PlayerDying[self.FrameFromZero]

                if self.FrameFromZero == len(PlayerDying)-1:
                    print(startingPosition)
                    self.pos = startingPosition
                    FrameFromZero = 0
                    self.awake = True
                    self.dead = False
                    self.lifes = 3


        ###########IDLING##################

        if not self.walking and not self.jumping:
            if now - self.lastUpdate > 200:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(PlayerIdlingLeft)
                if self.idlingLeft:
                    self.image = PlayerIdlingLeft[self.currentFrame]
                if self.idlingRight:
                    self.image = PlayerIdlingRight[self.currentFrame]



class Goblin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.goblinWidth = 20
        self.goblinHeight = 32

        self.lifes = 1
        self.dead = False

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.goblinWidth,self.goblinHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.FrameFromZero = 0
        self.currentFrame = 0
        self.lastUpdate = 0

        self.punch = False
        self.attack = False
        self.walkRight = False
        self.walkLeft = False
        self.jumping = False

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.animate()

        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def platformCollide(self, platforms):
        hits = pg.sprite.spritecollide(self, platforms, False)
        if hits:                                        #Checkt ob Player Platform berührt
            if self.rect.bottom < hits[0].rect.bottom: #self.Player.vel.y > 0 and
                self.pos.y = hits[0].rect.top# - self.Player.rect.height/2
                self.vel.y = 0
                self.jumping = False
                if self.vel.y < 0:
                    self.top = hits[0].rect.bottom
                    self.vel.y = 0

                for hit in hits:
                    if hit.rect.left and self.pos.y > hit.rect.y:
                        self.vel.x = -2
                    elif hit.rect.right and self.pos.y > hit.rect.y:
                        self.vel.x = +2

#    def hit(self):
#        self.lifes -= 1


    def distance(self, targetPos, distance):
        if distance < 20:
            self.attack = True
        if targetPos.x > self.pos.x:
            self.walkRight = True
            self.walkLeft = False
        else:
            self.walkLeft = True
            self.walkRight = False


    def animate(self):
        now = pygame.time.get_ticks()                   #Zeit seit Spielstart

########Dying################

        if self.lifes < 0 and not self.dead:
            self.walkRight = False
            self.walkLeft = False
            if now - self.lastUpdate > 100:
                self.lastUpdate = now
                self.FrameFromZero = (self.FrameFromZero + 1) % len(GoblinDying)
                self.image = GoblinDying[self.FrameFromZero]

                if self.FrameFromZero == len(GoblinDying)-1:
                    self.dead = True
                    self.game.all_sprites.remove(self)
                    self.game.goblinSprites.remove(self)

        if not self.dead:
####### IDLING #############


            if not self.walkRight or not self.walkLeft:
                if now - self.lastUpdate > 200:
                    self.lastUpdate = now
                    self.currentFrame = (self.currentFrame + 1) % len(GoblinIdling)
                    self.image = pygame.transform.flip(GoblinIdling[self.currentFrame], True, False)

            self.mask = pg.mask.from_surface(self.image)


    ##########Walking################
            if (self.walkRight or self.walkLeft) and not self.attack:
                if now - self.lastUpdate > 50:
                    self.lastUpdate = now
                    self.currentFrame = (self.currentFrame + 1) % len(GoblinRunning)

                    if self.walkRight:
                        self.vel.x = 3
                        self.image = GoblinRunning[self.currentFrame]
                    if self.walkLeft:
                        self.vel.x = -3
                        self.image = pygame.transform.flip(GoblinRunning[self.currentFrame], True, False)             # Flip Horizontal = True; Flip Vertical = False

###############ATTACKING###################

            if self.attack:
                if now - self.lastUpdate > 150:
                    self.lastUpdate = now
                    self.FrameFromZero = (self.FrameFromZero + 1) % len(GoblinAttack)
                    if self.walkRight:
                        self.image = GoblinAttack[self.FrameFromZero]
                    if self.walkLeft:
                        self.image = pygame.transform.flip(GoblinAttack[self.FrameFromZero], True, False)
                    if self.FrameFromZero == 2:
                        self.punch = True
                    else:
                        self.punch = False
                    if self.FrameFromZero == len(GoblinAttack)-1:
                        self.attack = False

class Platform(pg.sprite.Sprite):
    def __init__(self, img, x, y, w, h,):

        if img == 10:
            pic = pg.image.load("Sprites/Platforms/wall.png")
            self.image = pg.transform.scale(pic, (w, h))
            #self.image = pg.image.load("Sprites/Platforms/wall.png")
            #self.image.transform.scale(w,h)
        if img == 20:
            pic = pg.image.load("Sprites/Platforms/grass_small.png")
            self.image = pg.transform.scale(pic, (w, h))
            #self.image = pg.image.load("Sprites/Platforms/grass_small.png")
        if img == 30:
            pic = pg.image.load("Sprites/Platforms/stone_small.png")
            self.image = pg.transform.scale(pic, (w, h))
            #self.image = pg.image.load("Sprites/Platforms/stone_small.png")
        #else:
        #    print(img)
        #    self.image = pg.Surface((w, h))
        #    self.image.fill(GREEN)
        #print(img)
        pg.sprite.Sprite.__init__(self)


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.originalX = self.rect.x
        self.originalY = self.rect.y

class Text(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.center = vec(x, y)

class randomObjects(pg.sprite.Sprite):
    def __init__(self, pic,location):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((48,48))
        self.image = pic
        self.rect = self.image.get_rect()
        #self.rect.center = vec(3640, 1840)
        self.rect.center = location
