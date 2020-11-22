from random import randrange as rnd, choice
from random import randint
import pygame
from pygame.draw import *
import math

pygame.init()

screen_size_x = 1000
screen_size_y = 600
screen_size = (screen_size_x, screen_size_y)

screen = pygame.display.set_mode(screen_size)

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

class Hero():
    def __init__(self, coord=None):
        '''
        Set ball's parameters and thier meanings
        '''
        if coord is None:
            coord = [screen_size[0] // 2, 0]
        self.coord = coord
        self.is_alive = True
        self.was_kicked = False
        self.length = 100  # Full length of hero from top to the bottom
        self.number_of_road = 2
        self.gender = 0  # 0 - female; 1 - male

    def move(self, add_x):
        '''
		Move the hero to the nearby road
		'''
        self.coord[0] += add_x

    def draw(self):
        '''
        Draws obstacles. Attention: coords are the coordinates of the left top corner
        '''
        rect(screen, MAGENTA, (self.coord[0], self.coord[1], self.length, self.width))

if __name__ == "__main__":
    print("This module is not for direct call!")
