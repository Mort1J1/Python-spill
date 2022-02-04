import sys, pygame
import time


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

#Create surface
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create title
pygame.display.set_caption("(^_ ^)")

#create icon
icon = pygame.image.load('hongbao.png')
pygame.display.set_icon(icon)

#game clock
gameclock = pygame.time.Clock()

#sprite
blokksprite = pygame.image.load('Blokk00.png')
blokkliste = []

blokkNr = 0
#BLOKK

spritex = SCREEN_WIDTH/2
spritey = 50

class Blokk():
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        self.blokksprites = []
        
        self.blokksprites.append(pygame.image.load('Blokk00.png'))

        self.currentSprite = 0
        self.image = pygame.image.load('Blokk00.png')
        self.imagee = self.blokksprites[self.currentSprite]
        
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

#getting ticks
ticks = pygame.time.get_ticks()

while running:

    gameclock.tick(20)
    fps = str(int(gameclock.get_fps()))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                print (pygame.time.get_ticks())
            if event.key == pygame.K_d:
                blkk = create_blokk()
                blokkliste.append(blkk)
    


    #surface.blit(blokksprites[blokkNr], (0, 0))

    # if pygame.time.get_ticks() > ticks + 50:
    #     blokkNr += 1
    #     ticks = pygame.time.get_ticks()
    #     if blokkNr >= 25:
    #         blokkNr = 0
    #         ticks = pygame.time.get_ticks()-500
    tegn_blokk()
    print (ticks)
    pygame.display.update()
    surface.fill(COLOR_WHITE)