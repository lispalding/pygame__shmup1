# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 02/25/2021
# DATE LAST MODIFIED: 03/05/2021
# PYTHON VER. USED: 3.8
# FILE NAME: main.py

########### !! IMPORTS !! ############
import pygame as pg
from pygame.locals import *
import random as r
from colors import *
from math import *
from os import *
############## !! FIN !! ###############

########### !! CONSTANTS !! ############
title = "Shmup"

WIDTH = 300
HEIGHT = 600

FPS = 60
############## !! FIN !! ###############

############# !! CLASSES !! ############
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__() # Setting the __init__ function as the super class
        self.image = pg.Surface((50, 40)) # Setting the height and width of the player sprite
        self.image.fill(GREEN) # Filling the sprite image a certain color

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = (HEIGHT - (HEIGHT*.05))

        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()  # Setting the __init__ function as the super class
        self.image = pg.Surface((50, 40))  # Setting the height and width of the player sprite
        self.image.fill(RED)  # Filling the sprite image a certain color

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = (HEIGHT * .08)

        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

############## !! FIN !! ###############

######### !! INITIALIZATION !! #########
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock
############## !! FIN !! ###############

########## !! GAME OBJECTS !! ###########
player = Player()
npc = NPC()
############## !! FIN !! ###############

######### !! SPRITE GROUPS !! ##########
allSprites = pg.sprite.Group()
playersGroup = pg.sprite.Group()
npcGroup = pg.sprite.Group()

# Adding Player and NPC to sprite groups
playersGroup.add(player)
npcGroup.add(npc)

# Auto adding sprites to allSprites group
for i in playersGroup:
    allSprites.add(i)
for i in npcGroup:
    allSprites.add(i)
############## !! FIN !! ###############

########### !! LOAD IMAGES !! ###########

############## !! FIN !! ###############

############ !! GAME LOOP !! ###########
### .. GAME UPDATE VARIABLES ###
playing = True
score = 0
level = 1
difficulty = 0
########## .. FIN .. ###########

######## .. GAME LOOP .. ########
while playing:
    ### Timing


    ### Collecting Input
    ## Quitting the game when we hit "x" or hits escape
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False

    ### Updating Section

    ### Display Changes / Render
    screen.fill(BLACK)
    allSprites.draw(screen)

    pg.display.flip()
########## .. FIN .. ###########

pg.quit()
############## !! FIN !! ###############

