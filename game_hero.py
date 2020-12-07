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

male_model = pygame.image.load("male.png")
female_model = pygame.image.load("female.png")

class Hero():
    def __init__(self, gender, coord=None):
        '''
        Set ball's parameters and thier meanings
    def __init__(self, x, y, scale, gender, step, direction, vel, stand):
        '''
        self.scale = 0.5
        self.gender = gender
        self.step = 1
        self.direction = 1
        self.length = 45
        if coord is None:
            coord = [screen_size[0] // 2, 0]
        self.coord = coord
        self.is_alive = True
        self.was_kicked = False
        self.number_of_road = 2
        self.size_x = 300
        self.size_y = 400

    def move(self, add_x):
        '''
		Move the hero to the nearby road
		'''
        self.coord[0] += add_x

    def draw(self):
        '''
        Draws the hero, attention: self.coord works like coordinatese of the center of the hero
        '''

        if self.gender == 1:
            player_surface = pygame.transform.scale(male_model, (self.size_x, self.size_y))
            #print(self.gender)
        elif self.gender == 0:
            player_surface = pygame.transform.scale(female_model, (self.size_x, self.size_y))
            #print(self.gender)
        screen.blit(player_surface, (self.coord[0] - 38, -75 + self.coord[1]), (((self.size_x + 4) // 4)*(int(self.step) - 1), 5 + (self.size_y // 4)*self.direction, self.size_x / 4, self.size_y / 4))

        if self.step > 4.4:
            self.step = 1
        else:
            self.step += 0.5


if __name__ == "__main__":
    print("This module is not for direct call!")
