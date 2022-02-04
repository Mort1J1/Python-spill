from cmath import pi
from math import sqrt
from turtle import Screen
import pygame
import sys
import random
from pyparsing import Or


from scipy import rand

from soupsieve import match
from sqlalchemy import case, false

pygame.init()


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

#Create surface
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create title
pygame.display.set_caption("(^_ ^)")

#create icon
icon = pygame.image.load('hongbao.png')
pygame.display.set_icon(icon)

#antall virus og murlocs for "score"
AntM = 0
AntV = 0
font = pygame.font.Font('freesansbold.ttf', 32)
fontPosx, fontPosy = 20, 20

def show_score(x, y):
    scoreV = font.render("Virus: " + str(AntV), True, (255, 255, 255))


pos_x = SCREEN_WIDTH/2 + random.randrange(-200, 200)
pos_y = SCREEN_HEIGHT/2 + random.randrange(-200, 200)



running = True

murloclist = []
viruslist = []

def move_ball():
    global pos_x
    global pos_y

    pos_x += 1
    pos_y += 1

class Murloc():
    def __init__(self):
        self.x = SCREEN_WIDTH/2 + random.randrange(-200, 200)
        self.y = SCREEN_HEIGHT/2 + random.randrange(-200, 200)
        self.infected = False
        self.size = random.randrange(10, 50)
        self.color = (255, 0, random.randrange(0, 100))
        self.spx = random.randrange(-5, 5, 2)
        self.spy = random.randrange(-5, 5, 2)
        self.infectedTime = 0
        
class Virus():
    def __init__(self):
        self.x = SCREEN_WIDTH/2 + random.randrange(-200, 200)
        self.y = SCREEN_HEIGHT/2 + random.randrange(-200, 200)
        self.spx = random.randrange(-7, 7, 2)
        self.spy = random.randrange(-7, 7, 2)
        self.size = random.randrange(4, 6)
        self.infectiousR = random.randrange(0, 95)
        self.color = (175, self.infectiousR+87, self.infectiousR+100)
        self.copy = random.randrange(1, 3)




def create_murloc():
    return Murloc()
  #  pygame.draw.circle(surface, m.color, (m.x, m.y), m.size)

def create_virus():
    return Virus()

def move(m: Murloc):
    
    Alive = True
    i = 1000

    while i > 0:
        move_murlocs()

        i -= 10


        pygame.display.update()

        surface.fill(COLOR_BLACK)

def clone_virus(m: Murloc):
    for i in range (1, random.randrange(0, 6)):
        v = create_virus()
        v.x = m.x
        v.y = m.y
        viruslist.append(v)

def move_murlocs():

    for m in murloclist:
        if m.x + m.size >= SCREEN_WIDTH or m.x - m.size <= 0:
            m.spx *= -1
        if m.y + m.size >= SCREEN_HEIGHT or m.y - m.size <= 0:
            m.spy *= -1
        if m.infected == True and m.infectedTime+5000<pygame.time.get_ticks():
            clone_virus(m)
            murloclist.remove(m)

       
        pygame.draw.circle(surface, m.color, (m.x, m.y), m.size)
        m.x += m.spx
        m.y += m.spy

def move_virus():

    for m in viruslist:
        if m.x + m.size >= SCREEN_WIDTH or m.x - m.size <= 0:
            m.spx *= -1
        if m.y + m.size >= SCREEN_HEIGHT or m.y - m.size <= 0:
            m.spy *= -1

        m.x += m.spx
        m.y += m.spy
        pygame.draw.circle(surface, m.color, (m.x, m.y), m.size)
        # if m.x + m.size >= SCREEN_WIDTH:
        #     Alive = False
        # elif m.x - m.size <= SCREEN_WIDTH:
        #     Alive = False
        # elif m.y + m.size >= SCREEN_HEIGHT:
        #     Alive = False
        # elif m.y - m.size <= SCREEN_HEIGHT:
        #     Alive = False
    
def infections(murloclist, viruslist):
    for m in murloclist:
        for v in viruslist:
            if m.infected == False and (sqrt(((v.x - m.x)**2)+((v.y - m.y)**2)) <= (m.size + v.size)):
                m.infected = True
                m.infectedTime = pygame.time.get_ticks()
                m.color = (39,134,39)
                viruslist.remove(v)


while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_m:
                m = create_murloc()
                murloclist.append(m)
            if event.key == pygame.K_c:
                surface.fill(COLOR_BLACK)
            if event.key == pygame.K_v:
                v = create_virus()
                viruslist.append(v)
            if event.key == pygame.K_d:
                swch = 4      
    

    move_murlocs()
    move_virus()
    infections(murloclist, viruslist)

    pygame.display.update()
    surface.fill(COLOR_BLACK)