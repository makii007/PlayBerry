#!/usr/bin/env python3
import pygame

#########################
#        PLAYER         #
#########################

width = 32
height = 32

#Running:

img0 = pygame.image.load("Sprites/Player/RightRunning/RightRunning0.png")
img1 = pygame.image.load("Sprites/Player/RightRunning/RightRunning1.png")
img2 = pygame.image.load("Sprites/Player/RightRunning/RightRunning2.png")
img3 = pygame.image.load("Sprites/Player/RightRunning/RightRunning3.png")
img4 = pygame.image.load("Sprites/Player/RightRunning/RightRunning4.png")
img5 = pygame.image.load("Sprites/Player/RightRunning/RightRunning5.png")

OriginalSize = [img0,img1,img2,img3,img4,img5]
PlayerWalkRight = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    PlayerWalkRight.append(element)

#Idling Right

img0 = pygame.image.load("Sprites/Player/Idle/idle0.bmp")
img1 = pygame.image.load("Sprites/Player/Idle/idle1.bmp")
img2 = pygame.image.load("Sprites/Player/Idle/idle2.bmp")
img3 = pygame.image.load("Sprites/Player/Idle/idle3.bmp")

OriginalSize = [img0,img1,img2,img3]
PlayerIdlingRight = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    PlayerIdlingRight.append(element)

# Idling Left

img0 = pygame.image.load("Sprites/Player/Idle/idle0.bmp")
img1 = pygame.image.load("Sprites/Player/Idle/idle1.bmp")
img2 = pygame.image.load("Sprites/Player/Idle/idle2.bmp")
img3 = pygame.image.load("Sprites/Player/Idle/idle3.bmp")

OriginalSize = [img0,img1,img2,img3]
PlayerIdlingLeft = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    element = pygame.transform.flip(element, True, False)
    PlayerIdlingLeft.append(element)

#JUMPING######

#up

img0 = pygame.image.load("Sprites/Player/RightJumpUp/RightJumpUp0.png")
img1 = pygame.image.load("Sprites/Player/RightJumpUp/RightJumpUp1.png")
img2 = pygame.image.load("Sprites/Player/RightJumpUp/RightJumpUp2.png")

OriginalSize = [img0,img1,img2]
RightUpJump = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    RightUpJump.append(element)

#down

img0 = pygame.image.load("Sprites/Player/RightJumpDown/RightJumpDown0.png")
img1 = pygame.image.load("Sprites/Player/RightJumpDown/RightJumpDown1.png")
img2 = pygame.image.load("Sprites/Player/RightJumpDown/RightJumpDown2.png")

OriginalSize = [img0, img1, img2]
RightDownJump = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    RightDownJump.append(element)

#landing

img0 = pygame.image.load("Sprites/Player/Landing/BeforeLanding0.png")
img1 = pygame.image.load("Sprites/Player/Landing/BeforeLanding1.png")

OriginalSize = [img0, img1]
PlayerLanding = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    PlayerLanding.append(element)



#SwordAttack

img0 = pygame.image.load("Sprites/Player/SwordAttack/frame_0.png")
img1 = pygame.image.load("Sprites/Player/SwordAttack/frame_1.png")
img2 = pygame.image.load("Sprites/Player/SwordAttack/frame_2.png")
img3 = pygame.image.load("Sprites/Player/SwordAttack/frame_3.png")

OriginalSize = [img0,img1,img2,img3]
SwordAttack = []

for element in OriginalSize:
    element = pygame.transform.scale(element, (64, height))
    SwordAttack.append(element)


#Dying:

img0 = pygame.image.load("Sprites/Player/Dying/frame_0.png")
img1 = pygame.image.load("Sprites/Player/Dying/frame_1.png")
img2 = pygame.image.load("Sprites/Player/Dying/frame_2.png")
img3 = pygame.image.load("Sprites/Player/Dying/frame_3.png")
img4 = pygame.image.load("Sprites/Player/Dying/frame_4.png")
img5 = pygame.image.load("Sprites/Player/Dying/frame_5.png")
img6 = pygame.image.load("Sprites/Player/Dying/frame_6.png")
img7 = pygame.image.load("Sprites/Player/Dying/frame_7.png")

OriginalSize = [img0,img1,img2,img3,img4,img5,img6,img7]
PlayerDying = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    PlayerDying.append(element)

#Awake:

img0 = pygame.image.load("Sprites/Player/Awake/frame_0.png")
img1 = pygame.image.load("Sprites/Player/Awake/frame_1.png")
img2 = pygame.image.load("Sprites/Player/Awake/frame_2.png")
img3 = pygame.image.load("Sprites/Player/Awake/frame_3.png")
img4 = pygame.image.load("Sprites/Player/Awake/frame_4.png")
img5 = pygame.image.load("Sprites/Player/Awake/frame_5.png")
img6 = pygame.image.load("Sprites/Player/Awake/frame_6.png")
img7 = pygame.image.load("Sprites/Player/Awake/frame_7.png")

OriginalSize = [img0,img1,img2,img3,img4,img5,img6,img7]
PlayerAwake = []
for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    PlayerAwake.append(element)

#Hit

img0 = pygame.image.load("Sprites/Player/Hit/frame_0.png")
img1 = pygame.image.load("Sprites/Player/Hit/frame_1.png")
img2 = pygame.image.load("Sprites/Player/Hit/frame_2.png")

OriginalSize = [img0,img1,img2]
PlayerHit = []

for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    PlayerHit.append(element)











###################

######ENEMY########

###################

        ###########GOBLIN#

#Idling right


img0 = pygame.image.load("Sprites/Enemy/Goblin/Idle/frame_0.png")
img1 = pygame.image.load("Sprites/Enemy/Goblin/Idle/frame_1.png")
img2 = pygame.image.load("Sprites/Enemy/Goblin/Idle/frame_2.png")
img3 = pygame.image.load("Sprites/Enemy/Goblin/Idle/frame_3.png")

OriginalSize = [img0,img1,img2,img3]
GoblinIdling = []

for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    GoblinIdling.append(element)

#Running

img0 = pygame.image.load("Sprites/Enemy/Goblin/Running/frame_0_delay-0.1s.png")
img1 = pygame.image.load("Sprites/Enemy/Goblin/Running/frame_1_delay-0.1s.png")
img2 = pygame.image.load("Sprites/Enemy/Goblin/Running/frame_2_delay-0.1s.png")
img3 = pygame.image.load("Sprites/Enemy/Goblin/Running/frame_3_delay-0.1s.png")
img4 = pygame.image.load("Sprites/Enemy/Goblin/Running/frame_4_delay-0.1s.png")
img5 = pygame.image.load("Sprites/Enemy/Goblin/Running/frame_5_delay-0.1s.png")

OriginalSize = [img0,img1,img2,img3,img4,img5]
GoblinRunning = []

for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    GoblinRunning.append(element)

#ATTACKING

img0 = pygame.image.load("Sprites/Enemy/Goblin/attack/frame_0.png")
img1 = pygame.image.load("Sprites/Enemy/Goblin/attack/frame_1.png")
img2 = pygame.image.load("Sprites/Enemy/Goblin/attack/frame_2.png")
img3 = pygame.image.load("Sprites/Enemy/Goblin/attack/frame_3.png")

OriginalSize = [img0,img1,img2,img3]
GoblinAttack = []

for element in OriginalSize:
    element = pygame.transform.scale(element, (48, height))
    GoblinAttack.append(element)

# Dying####

img0 = pygame.image.load("Sprites/Enemy/Goblin/Dead/frame_0.png")
img1 = pygame.image.load("Sprites/Enemy/Goblin/Dead/frame_1.png")
img2 = pygame.image.load("Sprites/Enemy/Goblin/Dead/frame_2.png")
img3 = pygame.image.load("Sprites/Enemy/Goblin/Dead/frame_3.png")
img4 = pygame.image.load("Sprites/Enemy/Goblin/Dead/frame_4.png")
img5 = pygame.image.load("Sprites/Enemy/Goblin/Dead/frame_5.png")

OriginalSize = [img0,img1,img2,img3,img4,img5]
GoblinDying = []

for element in OriginalSize:
    element = pygame.transform.scale(element, (width, height))
    GoblinDying.append(element)


################ T E X T ####################

# Tutorial #

tut1 = pygame.image.load("Sprites/Text/Tutorial/01.png")
tut2 = pygame.image.load("Sprites/Text/Tutorial/02.png")
tut3 = pygame.image.load("Sprites/Text/Tutorial/03.png")
tut4 = pygame.image.load("Sprites/Text/Tutorial/04.png")
tut5 = pygame.image.load("Sprites/Text/Tutorial/05.png")
tut6 = pygame.image.load("Sprites/Text/Tutorial/06.png")
tut7 = pygame.image.load("Sprites/Text/Tutorial/07.png")
