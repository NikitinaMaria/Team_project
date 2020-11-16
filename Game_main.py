from random import randrange as rnd, choice
import pygame
from pygame.draw import *
import math

pygame.init()

screen_size_x = 900
screen_size_y = 700
FPS = 50

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIL = (190, 0, 255)
DARK_GREEN = (0, 128, 0)
GREY = (128, 128, 128)

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
screen.fill(WHITE)

clock = pygame.time.Clock()
finished = False
finished_game = False

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
