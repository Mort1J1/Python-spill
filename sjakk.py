import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

grid = (640/8)



# class Brikke():
#     def __init__(self):
#         self.x = grid
#         self.y = grid

class Bonde(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("BondeHvit.png")

    def update(self):
        surface.blit(pygame.image.load("BondeHvit.png"), (grid, grid))

# def TegnBrikke(sprite, type, team):
#     x = grid*2
#     y = grid
#     if team:
#         surface.blit(sprite, (x, y))

pygame.init()

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

SjakkBrett = pygame.transform.scale(pygame.image.load("SjakkBrett.png"), (640, 640), surface)

bonder = pygame.sprite.Group


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    surface.blit(SjakkBrett, (0, 0))
    for i in range (1, 9):
        #pygame.draw.circle(surface, (255, 0, 0), (((grid) * i) - 40, grid - 40), 5)
        for j in range (1, 9):
            pygame.draw.circle(surface, (255, 0, 0), ((grid * i) - 40, (grid * j) - 40), 5)

    pygame.display.update()
