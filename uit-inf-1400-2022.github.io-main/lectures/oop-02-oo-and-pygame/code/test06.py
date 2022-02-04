#!/usr/bin/env python3

import random
import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "Chapter03/sushiplate.jpg"
MOUSE_FNAME = "Chapter03/fugu.png"
BALL_FNAME = "ball.png"


pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img  = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()

ball_img = pygame.image.load(BALL_FNAME).convert_alpha()


class MovingObj:
    def __init__(self):
        self.x = 42
        self.y = 200
        self.speed = [50 + 100 * random.random(), 50 + 100 * random.random()]

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])
        if self.x > SCREEN_X:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y:
            self.speed[1] = -abs(self.speed[1])

    def draw(self):
        pass


class Ball(MovingObj):
    def __init__(self):
        super().__init__()
        self.img = ball_img

    def draw(self):
        screen.blit(self.img, (round(self.x), round(self.y)))


class Circle(MovingObj):
    def __init__(self):
        super().__init__()
        self.radius = 30
        self.col = (255, 128, 128)

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)), self.radius)


class Rect(MovingObj):
    def __init__(self):
        super().__init__()
        self.w = 30
        self.h = 20
        self.col = (255, 255, 0)

    def draw(self):
        pygame.draw.rect(screen, self.col, (round(self.x), round(self.y), self.w, self.h))



ball1 = Ball()
objs = [
    Ball(),
    Ball(),
    Ball(),
    Ball(),
    Ball(),
    Circle(),
    Circle(),
    Rect(),
    Rect(),
]
clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    time_passed = clock.tick(30) / 1000.0

    # Flytt objekter
    ball1.move(time_passed)
    for obj in objs:
        obj.move(time_passed)

    # Tegn bakgrunn
    screen.blit(background, (0, 0))

    # Tegn opp ball
    ball1.draw()
    for obj in objs:
        obj.draw()

    # Hent ut musposisjon og tegn opp "musepeker"
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    screen.blit(mouse_img, (round(mouse_x - mouse_size_x / 2), round(mouse_y - mouse_size_y / 2)))

    pygame.display.update()

    # print(event)

print("Ferdig")
