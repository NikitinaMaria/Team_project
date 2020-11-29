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
building_bio = pg.image.load('bio.png')
building_kpm = pg.image.load('kpm.png')
building_lab = pg.image.load('lab.png')
buidings = [building_bio, building_kpm, building_lab]

class Building():
    def __init__(self, speed, width_of_pictures):
        self.width_start = randint(50, 100)
        self.width = self.width_start
        self.side = randint(1, 2)
        self.width_of_road = (screen_size_x - 2 * width_of_pictures)
        if self.side == 1:
            self.coord_x = randint(200, width_of_pictures + self.width_of_road // 4 - self.width // 2)
        else:
            self.coord_x = randint(screen_size_x - width_of_pictures - self.width_of_road // 4 + self.width // 2, screen_size_x)
        self.coord_y = 0
        self.speed = speed
        self.variant = randint(0, 2)
        self.scale = pg.transform.scale(buidings[self.variant], (self.width, self.width))
        self.top_distance_from_center_x = abs(self.coord_x - screen_size_x // 2)
        self.lower_distance_from_center_x = 2 * self.top_distance_from_center_x
        self.distance_from_center_x = self.lower_distance_from_center_x

    def motion(self):
        print(self.coord_x)
        print(self.coord_y)
        self.coord_y += self.speed
        self.distance_from_center_x = abs(self.coord_x - screen_size_x // 2)
        self.coord_x = - self.lower_distance_from_center_x // screen_size_y * self.coord_y // 2 + screen_size_x // 2 - self.top_distance_from_center_x
        self.width = self.width_start * self.distance_from_center_x // self.top_distance_from_center_x

    def draw(self):
        self.scale = pg.transform.scale(buidings[self.variant], (self.width, self.width))
        screen.blit(self.scale, (self.coord_x - self.width // 2, self.coord_y - self.width))



def draw_road(width_of_pictures, distance_between_roads):
    """"
    The function draws road
    """
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

buiding = Building(5, 200)

FPS = 15
clock = pg.time.Clock()
done = False

while not done:
    clock.tick(FPS)
    pg.display.update()
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    draw_road(200, 6)
    buiding.motion()
    buiding.draw()

pg.quit()
