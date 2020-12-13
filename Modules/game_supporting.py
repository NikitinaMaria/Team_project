import Modules.game_mechanics
from Modules.game_mechanics import *
import pygame
from pygame.draw import *

BlOOD = (153, 0, 0)
FPS = 15

class Boost:
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_all_road = screen_size_x - 2 * width_of_pictures
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.width_start = width // 2
        self.width = self.width_start
        self.length = 35
        self.number_of_road = number_of_road
        self.coord = [width_of_pictures + self.width_of_all_road // 4 + self.width_of_road // 4 - self.length // 2 +
                      (number_of_road - 1) * (self.width_of_road // 2 + self.distance_between_roads // 2), 0]
        self.redbull = pygame.image.load('images/RedBull.png')
        self.scale = pygame.transform.scale(self.redbull, (self.length, self.width))
        if number_of_road == 2:
            self.lower_distance_from_center_x = self.length // 4
        elif number_of_road == 1:
            self.lower_distance_from_center_x = self.width_of_road // 2 + self.length // 2 + self.distance_between_roads // 2
        else:
            self.lower_distance_from_center_x = self.width_of_road // 2 - self.length // 2 + self.distance_between_roads // 2

    def motion(self):
        '''
        Move obstacles, look if they are done
        '''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] + self.width:
            self.is_alive = False
        self.length = 35 * (screen_size_y + self.coord[1]) // screen_size_y
        self.width = self.width_start * (screen_size_y + self.coord[1]) // screen_size_y
        if self.number_of_road != 3:
            self.coord[0] = - self.coord[
                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 - self.lower_distance_from_center_x
        else:
            self.coord[0] = self.coord[
                                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 + self.lower_distance_from_center_x

    def draw(self):
        '''
        Draws obstacles. Attention: coords are the coordinates of the left top corner
        '''
        self.scale = pygame.transform.scale(self.redbull, (self.length, self.width))
        screen.blit(self.scale, (self.coord[0], self.coord[1]))

class Obstacle:
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.type = randint(1, 2)
        if self.type == 1:
            self.bed = pygame.image.load('images/bed.png')
        else:
            self.bed = pygame.image.load('images/sofa.png')
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_all_road = screen_size_x - 2 * width_of_pictures
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.coord = [width_of_pictures + self.width_of_all_road // 4 + (number_of_road - 1) * (
                self.width_of_road // 2 + self.distance_between_roads // 2), 0]
        self.length = self.width_of_road // 2
        self.width = width
        self.number_of_road = number_of_road
        if number_of_road == 2:
            self.lower_distance_from_center_x = self.width_of_road // 4
        elif number_of_road == 3:
            self.lower_distance_from_center_x = self.width_of_road // 4 + self.distance_between_roads
        else:
            self.lower_distance_from_center_x = self.width_of_road // 4 * 3 + self.distance_between_roads

    def motion(self):
        '''
        Move obstacles, look if they are done
        '''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] - self.width:
            self.is_alive = False
        self.length = self.width_of_road // 2 * (screen_size_y + self.coord[1]) // screen_size_y
        if self.number_of_road != 3:
            self.coord[0] = - self.coord[
                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 - self.lower_distance_from_center_x
        else:
            self.coord[0] = self.coord[
                                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 + self.lower_distance_from_center_x

    def draw(self):
        '''
        Draws obstacles. Attention: coords are the coordinates of the left top corner
        '''
        self.scale = pygame.transform.scale(self.bed, (self.length, self.width))
        screen.blit(self.scale, (self.coord[0], self.coord[1]))


def draw_emergency_table(self):
    if self.time >= self.time_for_Kozhevnikov_test - 50 and self.time <= self.time_for_Kozhevnikov_test and self.time % 6 != 0:
        rect(screen, RED, (
        screen_size[0] - self.width_of_pictures, 2 * screen_size[1] // 3, 3 * self.width_of_pictures // 4,
        screen_size[1] // 8))
        Modules.game_mechanics.insert_text('Attention', 'Fonts/Game-font.ttf', WHITE,
                    (screen_size[0] - 6 * self.width_of_pictures // 10, 2 * screen_size[1] // 3 + screen_size[1] // 30),
                    screen_size[1] // 30)
        Modules.game_mechanics.insert_text('Test is coming', 'Fonts/Game-font.ttf', WHITE,
                    (screen_size[0] - 6 * self.width_of_pictures // 10, 2 * screen_size[1] // 3 + screen_size[1] // 13),
                    screen_size[1] // 37)

def draw_titers(self):
    if self.time <= 3 * FPS // 2:
        Modules.game_mechanics.insert_picture('images/DGAP-MIPT.png', (screen_size[0] // 2, screen_size[1] // 2), screen_size)
    elif self.time <= 3 * FPS and self.time > 3 * FPS // 2:
        Modules.game_mechanics.insert_text('Presents', 'Fonts/Presents.ttf', WHITE, (screen_size[0] // 2, screen_size[1] // 2),
                    min(screen_size[0] // 3, screen_size[1] // 3))
    elif self.time <= 9 * FPS // 2 and self.time > 3 * FPS:
        Modules.game_mechanics.insert_picture('images/DGAP-cat.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                       (self.time * 7, self.time * 7))
    elif self.time <= 6 * FPS and self.time > 9 * FPS // 2:
        Modules.game_mechanics.insert_text('Сессия близко', 'Fonts/Session.otf', BlOOD, (screen_size[0] // 2, screen_size[1] // 2),
                    min(screen_size[0] // 3, screen_size[1] // 3))
    elif self.time <= 9 * FPS and self.time > 6 * FPS:
        Modules.game_mechanics.insert_text('С благодарностью за то, что они есть', 'Fonts/Kozhevnikov.ttf', WHITE,
                    (screen_size[0] // 2, screen_size[1] // 20), min(screen_size[0] // 10, screen_size[1] // 10))
        Modules.game_mechanics.insert_text('и вообще всем, кто делает ФОПФ таким, каким мы его знаем', 'Fonts/Kozhevnikov.ttf', WHITE,
                    (screen_size[0] // 2, 19 * screen_size[1] // 20), min(screen_size[0] // 16, screen_size[1] // 16))
        for i in range(1, 4, 1):
            if self.time >= (5 + i) * FPS + 1:
                Modules.game_mechanics.insert_picture('images/Thank_you_' + str(i) + '.jpg',
                               (i * screen_size[0] // 4, 41 * screen_size[1] // 80),
                               (screen_size[0] // 2, 64 * screen_size[1] // 80))
    elif self.time > 9 * FPS and self.time <= 15 * FPS:
        Modules.game_mechanics.insert_picture('images/Disclaimer.jpg', (screen_size[0] // 2, screen_size[1] // 2), screen_size)
    if self.time <= 15 * FPS:
        return True
    else:
        return False