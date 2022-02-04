import sys, pygame
from tkinter import Y
import time
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_SCREEN = (222, 24, 111)

#135 75 blokk dimensjoner

#Create surface
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

surface.fill(COLOR_SCREEN)
#Create title
pygame.display.set_caption("(^_ ^)")

#create random icon
randomT = random.randrange(1, 4)
iconarray = []
iconarray.append(pygame.image.load('Blocks0.png'))
iconarray.append(pygame.image.load('Blocks1.png'))
iconarray.append(pygame.image.load('Blocks2.png'))
iconarray.append(pygame.image.load('Blocks3.png'))

icon = iconarray[randomT]
pygame.display.set_icon(icon)



#game clock
gameclock = pygame.time.Clock()

#sprite
blokkliste = []
for i in range (0, 4):
    blokkliste.append(pygame.image.load("Blocks" + str(i) + ".png"))

blokkNr = 0
#BLOKK

spritex = SCREEN_WIDTH/2
spritey = 50

x = 0
y = 0

def wasd(x, y):
    if event.key == pygame.K_w:
        y += 10
    if event.key == pygame.K_a:
        x -= 10
    if event.key == pygame.K_s:
        y -= 10
    if event.key == pygame.K_d:
        x += 10

class Blokk():
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        self.blokksprites = []
        
        self.blokksprites.append(pygame.image.load('Blokk00.png'))

        self.currentSprite = 0
        self.image = self.blokksprites[self.currentSprite]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

def create_blokk():
    return Blokk

def tegn_blokk():

    for b in blokkliste:
        if pygame.time.get_ticks() > ticks + 50:
            surface.blit(b.image, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            b.currentSprite += 1
            if b.currentSprite >= 25:
                b.currentSprite = 0
        surface.blit(b.image, (0, 0))

class MovingObject():
    def __init__(self):
        self.speedx = 2
        self.speedy = 2
        self.x = SCREEN_WIDTH/2
        self.y = 50
        self.size = 5
        self.sprite = []

running = True
switchSkin = 0
switchwasd = 0
#getting ticks
ticks = pygame.time.get_ticks()




while running:

    gameclock.tick(20)
    fps = str(int(gameclock.get_fps()))

    randomT2 = random.randrange(0, 3)
    randomT3 = random.randrange(1, 5)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                print (pygame.time.get_ticks())
            if event.key == pygame.K_b:
                surface.blit(blokkliste[randomT2], (x, y))

                #wasd
            if event.key == pygame.K_w:
                switchwasd = 0
            if event.key == pygame.K_a:
                switchwasd = 1
            if event.key == pygame.K_s:
                switchwasd = 2
            if event.key == pygame.K_d:
                switchwasd = 3
               
                #bytte skin
            if event.key == pygame.K_1:
                switchSkin = 0
            if event.key == pygame.K_2:
                switchSkin = 1
            if event.key == pygame.K_3:
                switchSkin = 2
            if event.key == pygame.K_4:
                switchSkin = 3
            
            #freeze screen

    if switchwasd == 0:
        y -= 5
    if switchwasd == 1:
        x -= 5
    if switchwasd == 2:
        y += 5
    if switchwasd == 3:
        x += 5
    
    #translate
    nyX = -3
    nyY = -90
    
    face = 0
    
    for j in range (0, 4):
        #y avstand
        nyY += 80
        for i in range (0, 7):
            surface.blit(blokkliste[j-1], (nyX, nyY))
            nyX += 140
            if nyX >= 890:
                nyX = -3
        face += 1
        if face == 4:
            face = 0





    # surface.blit(blokksprite, (0, 0))
    # surface.blit(blokksprite1, (150, 0))
    # surface.blit(blokksprite2, (300, 0))
    # surface.blit(blokksprite3, (450, 0))

    # if pygame.time.get_ticks() > ticks + 50:
    #     blokkNr += 1
    #     ticks = pygame.time.get_ticks()
    #     if blokkNr >= 25:
    #         blokkNr = 0
    #         ticks = pygame.time.get_ticks()-500

    

    pygame.display.update()
    #surface.fill(COLOR_WHITE)