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

debugging = True
############## !! FIN !! ###############

############# !! ASSETS !! #############
gameFolder = path.dirname(__file__)
imageDirectory = path.join(gameFolder, "images")
############## !! FIN !! ###############

############# !! CLASSES !! ############
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__() # Setting the __init__ function as the super class
        # self.image = pg.Surface((20, 40)) # Setting the height and width of the player sprite
        # self.image.fill(GREEN) # Filling the sprite image a certain color

        # Creating the player image:
        self.image = playerImage
        self.image = pg.transform.scale(playerImage, (50, 38))
        self.image.set_colorkey(BLACK)

        # Creating a bound box around the image:
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        if debugging:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = (HEIGHT - (HEIGHT*.05))

        self.speedx = 0

        self.keypressed = False

    def shoot(self):
        b = Bullet(self.rect.centerx, self.rect.top-1)
        allSprites.add(b)
        bulletGroup.add(b)

    def togglePressed(self):
        """ To use: self.togglePressed()
         This is the function that will check to see if a keypress is False. """
        self.keypressed = False
        self.speedx = 0

    def update(self):
        """ To use: self.update()
         This is the function that will update the movement of the player character. """
        keystate = pg.key.get_pressed() # Checking the Keystate, whether it is pressed or not

        ########## !!!! .. FLOW MOVEMENT .. !!!! ##########
        if self.keypressed == False:
            if keystate[pg.K_LEFT] or keystate[pg.K_a]:
                self.speedx += -3
                self.keypressed = True

            if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
                self.speedx += 3
                self.keypressed = True

        self.rect.x += self.speedx
        ########## !!!! .. FLOW FINISHED .. !!!! ##########

        # if keystate[K_SPACE]:
        #     self.shoot()

        ######### !!!! .. SCREEN BINDING .. !!!! ##########
        ## Binding player to screen area...
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        ######### !!!! .. BINDING FINISH .. !!!! ##########

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()

        ## Creating the bullet image
        # self.image = pg.Surface((10, 20))  # Setting the height and width of the player sprite
        # self.image.fill(BLUE)  # Filling the sprite image a certain color

        # Creating the player image:
        self.image = bulletImage
        self.image = pg.transform.scale(bulletImage, (8, 25))
        self.image.set_colorkey(BLACK)

        # Creating a bound box around the image:
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        if debugging:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        # Positioning the bullet
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.speedy = -5

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()  # Setting the __init__ function as the super class
        # self.image = pg.Surface((20, 20))  # Setting the height and width of the player sprite
        # self.image.fill(RED)  # Filling the sprite image a certain color

        # Random width and height of image
        self.randHeight = r.randrange(8, 55)
        self.randWidth = r.randrange(8, 55)

        # Creating the player image:
        self.image = npcImage
        self.image = pg.transform.scale(npcImage, (self.randWidth, self.randHeight))
        self.image.set_colorkey(BLACK)

        # Creating a bound box around the image:
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        if debugging:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect = self.image.get_rect()
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = (HEIGHT * .08)

        self.randSpeedX = r.randrange(-3,3)
        self.randSpeedY = r.randrange(1,8)

        self.speedx = self.randSpeedX
        self.speedy = self.randSpeedY

        self.rotation = 0
        self.rotationSpeed = r.randint(-8, 8)
        self.lastUpdate = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()

        if now - self.lastUpdate > 60:
            self.lastUpdate = now

            ## Rotating sprite
            # self.image = pg.transform.rotate(self.image, self.rotationSpeed)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH +20:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(1, 8)

        ##### !! SCREEEN WRAPPING !! #####
        if self.rect.left > WIDTH:
            self.rect.left = 0

        if self.rect.right < 0:
            self.rect.right = WIDTH

        if self.rect.top > HEIGHT:
            self.rect.top = 0

        if self.rect.bottom < 0:
            self.rect.bottom = HEIGHT
        ##### !! WRAPPING FINISH !! #####

############## !! FIN !! ###############

######### !! INITIALIZATION !! #########
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
############## !! FIN !! ###############

########### !! LOAD IMAGES !! ###########
## Loading all game graphics
## Background ##
background = pg.image.load(path.join(imageDirectory, "starfield.png")).convert()
background_rect = background.get_rect()

## Player Image ##
playerImage = pg.image.load(path.join(imageDirectory, "playerShip1_orange.png")).convert()

## NPC Image ##
npcImage = pg.image.load(path.join(imageDirectory, "meteorBrown_med1.png")).convert()

## Bullet Image ##
bulletImage = pg.image.load(path.join(imageDirectory, "laserRed16.png")).convert()
############## !! FIN !! ###############

########## !! GAME OBJECTS !! ###########
######### .. SPRITES .. ##########
player = Player()

allSprites = pg.sprite.Group()
playersGroup = pg.sprite.Group()
npcGroup = pg.sprite.Group()
bulletGroup = pg.sprite.Group()

# Adding Player and NPC to sprite groups
playersGroup.add(player)

for i in range(12):
    npc = NPC()
    npcGroup.add(npc)

bullet = Bullet(WIDTH/2, HEIGHT/2)
bulletGroup.add(bullet)
allSprites.add(bullet)

# Auto adding sprites to allSprites group
for i in playersGroup:
    allSprites.add(i)

for i in npcGroup:
    allSprites.add(i)
############## !! FIN !! ###############

############ !! GAME LOOP !! ###########
### .. GAME UPDATE VARIABLES ###
playing = True
score = 0
level = 1
difficulty = 0

FPS = 60
########## .. FIN .. ###########

######### !! GAME FUNCTIONS !! #########
def spawnNpc():
    npc = NPC()
    npcGroup.add(npc)
    allSprites.add(npc)

######### !! GAME FUNC FINISH !! #######

######## .. GAME LOOP .. ########
while playing:
    ### Timing
    clock.tick(FPS)  # Controlling the loop

    ### Collecting Input
    ##### Processing input ######
    for event in pg.event.get():  # Getting a list of events that have happened
        if event.type == pg.KEYUP: ## Getting if a key has been released
            if (event.key == pg.K_LEFT) or (event.key == pg.K_a):
                player.togglePressed()

            if (event.key == pg.K_RIGHT) or (event.key == pg.K_d):
                player.togglePressed()

            if (event.key == pg.K_UP) or (event.key == pg.K_w):
                player.togglePressed()

            if (event.key == pg.K_DOWN) or (event.key == pg.K_s):
                player.togglePressed()

        ### TEMPORARY FIX FOR BULLETS ###
        if event.type == KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()
        ####### FIN TEMPORARY FIX #######

        if event.type == pg.QUIT: ## Quitting the game when we hit "x" or hits escape
            playing = False
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False

    ### Updating Section
    ## If NPC hits Player
    hits0 = pg.sprite.spritecollide(player, npcGroup, True)

    if hits0: # Spawning an NPC when player gets hit by NPC
        spawnNpc()
    #     playing = False

    ## If Bullet hits NPC
    hits1 = pg.sprite.groupcollide(npcGroup, bulletGroup, True, True)

    if hits1: # Spawning an NPC when an asteroid hits bullet
        spawnNpc()

    allSprites.update()

    ### Display Changes / Render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    allSprites.draw(screen)

    pg.display.flip()
########## .. FIN .. ###########

pg.quit()
############## !! FIN !! ###############

