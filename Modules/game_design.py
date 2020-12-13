import pygame as pg
from pygame.draw import *
from random import randint
import numpy as np

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

'WINDOW'
screen_size_x, screen_size_y = 1000, 600
screen = pg.display.set_mode((screen_size_x, screen_size_y))

'IMAGES'
space = pg.image.load('images/space.jpg')
star_1 = pg.image.load('images/star.png')
star_2 = pg.image.load('images/fopf_black.png')
meteors = [star_1, star_2]

class Stars():
    def __init__(self, speed, width_of_pictures):
        self.width_start = randint(50, 75)
        self.width = self.width_start
        self.side = randint(1, 2)
        self.is_alive = True
        self.width_of_road = (screen_size_x - 2 * width_of_pictures)
        if self.side == 1:
            self.coord_x = randint(200, width_of_pictures + self.width_of_road // 4 - self.width // 2)
        else:
            self.coord_x = randint(screen_size_x - width_of_pictures - self.width_of_road // 4 + 50, screen_size_x - 150)
        self.coord_y = 0
        self.speed = speed
        self.variant = randint(0, 1)
        self.scale = pg.transform.scale(meteors[self.variant], (self.width, self.width))
        self.top_distance_from_center_x = abs(self.coord_x - screen_size_x // 2)

    def motion(self):
        self.coord_y += self.speed
        if self.coord_y >= screen_size_y + self.width:
            self.is_alive = False
        if self.side == 1:
            self.coord_x = - self.coord_y * self.top_distance_from_center_x // screen_size_y + screen_size_x // 2 - self.top_distance_from_center_x
        else:
            self.coord_x = self.coord_y * self.top_distance_from_center_x // screen_size_y + screen_size_x // 2 + self.top_distance_from_center_x
        self.width = self.width_start * (screen_size_y + self.coord_y) // screen_size_y

    def draw(self):
        self.scale = pg.transform.scale(meteors[self.variant], (self.width, self.width))
        screen.blit(self.scale, (self.coord_x - self.width // 2, self.coord_y - self.width))



def draw_road(width_of_pictures, distance_between_roads):
    """"
    The function draws road
    """
    scale = pg.transform.scale(space, (screen_size_x, screen_size_y))
    screen.blit(scale, (0, 0))
    width_of_road = (screen_size_x - 2 * width_of_pictures)
    polygon(screen, GREY, ((width_of_pictures, screen_size_y),
                           (screen_size_x - width_of_pictures, screen_size_y),
                           ((screen_size_x - width_of_road // 2) // 2 + width_of_road // 2, 0),
                           ((screen_size_x - width_of_road // 2) // 2, 0)))

    line(screen, WHITE, (width_of_pictures + (width_of_road - 2 * distance_between_roads) // 3, screen_size_y),
         ((screen_size_x - width_of_road // 2) // 2 + (width_of_road // 2 - distance_between_roads) // 3, 0),
         distance_between_roads)
    line(screen, WHITE, (width_of_pictures + 2 * width_of_road // 3 + distance_between_roads, screen_size_y),
         (screen_size_x // 2 + (width_of_road - 2 * distance_between_roads) // 12, 0),
         distance_between_roads)

if __name__ == "__main__":
    print("This module is not for direct call!")
