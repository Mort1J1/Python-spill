from math import sqrt
import sys, pygame
from matplotlib.pyplot import draw
from turtle import update
import time
import random

from sqlalchemy import intersect
import vector

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_SCREEN = (222, 24, 111)

antallBlokker = 0

#Create surface
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#audio init

#   (sqrt(((v.x - m.x)**2)+((v.y - m.y)**2)) <= (m.size + v.size))

pygame.mixer.init()

class Rekkert(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()
        self.image = pygame.image.load(sprite)
        #pygame.transform.scale(sprite, (320, 30))
        #rect left, top, width, height (0, 160, 320, 60)
        self.rect = self.image.get_rect()
        self.size = 80
    def update(self):
        self.mousex, self.mousey = pygame.mouse.get_pos()
        pygame.draw.circle(surface, (255, 0, 0), (self.mousex, 600), self.size, 4)
        self.rect.center = (self.mousex, 600)

class Ball(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()
        self.image = pygame.image.load(sprite)
        self.spx = random.randrange(-5, 5, 2)
        self.spy = random.randrange(-4, -3)
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2 + 100
        self.rect = self.image.get_rect()
        self.size = 10
        self.score = 0
        Ball.antalBlokker = 21


    def update(self, rekkert: Rekkert):
        self.rect.center = [self.x, self.y]
        if Gswitch == 1:
            if self.x + self.size >= SCREEN_WIDTH or self.x - self.size <= 0:
                self.spx *= -1
                wallBounce.play()
            if self.y - self.size <= 0:
                self.spy *= -1
                wallBounce.play()
            if self.y + self.size >= SCREEN_HEIGHT:
                pygame.sprite.Group.remove(ball_group, ball)
                playerdød.play()
            pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), 20, 4)
            self.x += self.spx
            self.y += self.spy

            if self.rect.colliderect(rekkert.rect):
                self.y -= 10
                self.spy *= -1
                print ('jalla')
            if (sqrt(((self.x - rekkert.mousex)**2)+((self.y - 600)**2)) <= (self.size + rekkert.size)):
                pygame.draw.line(surface, (255, 0, 0), (self.x, self.y), (rekkert.mousex, 600))
                if self.rect.colliderect(rekkert.rect):
                    print (self.x - rekkert.mousex, " / ", self.y - 600, " = ", ((self.x - rekkert.mousex) - self.y -600))
                
            #(sqrt(((self.x - rekkert.mousex)**2)+((self.y - 600)**2)) <= (self.size + rekkert.size))
            # if vector.intersect_circles((rekkert.mousex, rekkert.mousey), 35, (self.x, self.y), 20):
            #     lydball.play()
            #     self.spx, self.spy = (vector.intersect_circles((rekkert.x, rekkert.y), 35, (self.x, self.y), 20) *2 * (-1)) 

            
        # pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
        # if rekkert.rect.collidedict(self.rect):
        #     self.spy *= -

class Blokk(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        super().__init__()
        # self.sprite = []
        # for i in range (0, 4):
        #     self.sprite.append(pygame.image.load("Blocks" + str(i) + ".png"))
        # randomBlokk = random.randrange(0, 4)
        # self.image = self.sprite[randomBlokk]
        # self.imageEx = pygame.image.load('Blocks0.png')
        # self.rect = self.imageEx.get_rect()
        self.x = x
        self.y = y
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        Blokk.antallBlokker = 20
        Blokk.antallBlokker += 1


    def update(self, b: Ball):
        if self.rect.colliderect(b.rect):
            b.score += 1
            b.spy *= 1.01
            Blokk.antallBlokker -=1
            pygame.sprite.Group.remove(blokk_group, self)
            b.spy *= -1
            rTall = random.randrange(1, 3)
            if rTall == 1:
                død1.play()
            elif rTall == 2:
                død2.play()
            

#Score display
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(fontx, fonty, score_value, b: Blokk):
    score = font.render("Score: " + str(score_value) + " Antall blokker: " + str(Blokk.antallBlokker), True, (255, 255, 255))
    surface.blit(score, (fontx, fonty))

#spill meny

menyDone = False

def meny(menyDone):
    choises = 0
    welcome = font.render("Welcome Bootleg Breakout!", True, (255, 255, 255))
    surface.blit(welcome, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

#135 75 blokk dimensjoner

#lyd effekter

sang = pygame.mixer.Sound("funk118.wav")
død1 = pygame.mixer.Sound('BlokkDød1.wav')
død2 = pygame.mixer.Sound('BlokkDød2.wav')
lydball = pygame.mixer.Sound('Ballhit.wav')
playerdød = pygame.mixer.Sound('PlayerDød.wav')
wallBounce = pygame.mixer.Sound('BallVeggBounce.wav')
cntr = 1
clicksound = pygame.mixer.Sound('click.wav')
clicksound.set_volume(0.2)



#Create background
background = pygame.image.load('space.jpg')

#Create title
pygame.display.set_caption("Sprites")

#remove mouse
pygame.mouse.set_visible(False)

#create random icon
randomT = random.randrange(1, 4)
iconarray = []
for i in range (0, 4):
    iconarray.append(pygame.image.load("Blocks" + str(i) + ".png"))

icon = iconarray[randomT]
pygame.display.set_icon(icon)

#game clock
gameclock = pygame.time.Clock()

#sprite
blokkliste = []
for i in range (0, 4):
    blokkliste.append(pygame.image.load("Blocks" + str(i) + ".png"))



#getting ticks
ticks = pygame.time.get_ticks()

#switches
running = True
switchwasd = 0
Gswitch = 0

# create ball sprite
ball_group = pygame.sprite.Group()
ball = Ball("Ball.png")
ball_group.add(ball)
ballen = True

#create block sprite
poX, poY = 80, 65
distX, distY = 140, 80

blokk_group = pygame.sprite.Group()
def Add_blocks(poX, poY, distX, distY):    
    for blokk in range (3):
        for blokk in range (7):
            RspriteTall = random.randrange(0, 4)
            Rsprite = ["Blocks0.png", "Blocks1.png", "Blocks2.png", "Blocks3.png"]
            new_block = Blokk(Rsprite[RspriteTall], poX, poY)
            blokk_group.add(new_block)
            if poX == 80 + (distX*6):
                poX = 80
            else:
                poX += distX
        poY += distY
Add_blocks(poX, poY, distX, distY)
#create rekkert sprite

rekkert = Rekkert('Øye.png')
rekkert_group = pygame.sprite.Group()
rekkert_group.add(rekkert)

#score
score_value = 0

#infinite loop for game

while running:

    gameclock.tick(60)
    fps = str(int(gameclock.get_fps()))

    randomT2 = random.randrange(0, 3)
    randomT3 = random.randrange(1, 5)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                print (pygame.time.get_ticks(), "sprite rect:", rekkert.rect)

                #wasd
            if event.key == pygame.K_w:
                switchwasd = 0
            if event.key == pygame.K_a:
                switchwasd = 1
            if event.key == pygame.K_s:
                switchwasd = 2
            if event.key == pygame.K_d:
                switchwasd = 3
            if event.key == pygame.K_t:
                print(rekkert.rect)
            if event.key == pygame.K_SPACE:
                if Gswitch == 1:
                    Gswitch = 0
                elif Gswitch == 0:
                    Gswitch = 1
                clicksound.play()
            if event.key == pygame.K_n:
                Add_blocks(poX, poY, distX, distY)
            #freeze screen



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

    krav = 21
    level = 0

    surface.blit(background, (0, 0))

    rekkert_group.draw(surface)
    ball_group.draw(surface)
    ball_group.update(rekkert)
    blokk_group.draw(surface)
        #pygame.draw.rect(surface, (255, 0, 0), rekkert.rect, 3)
    rekkert_group.update()
    blokk_group.update(ball)
    show_score(10, 10, ball.score, Blokk)
    pygame.display.update()

        #surface.fill(COLOR_WHITE)