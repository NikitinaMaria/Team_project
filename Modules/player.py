
'''


Чтобы заработало - читай коммент ниже



'''





from random import randrange as rnd, choice
import pygame
from pygame.draw import *
import math

pygame.init()

screen_size_x = 900
screen_size_y = 700

FPS = 50
time_interval = 1/FPS

gender = 0 # 0 - female; 1 - male

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

#Player models
male_model = pygame.image.load(r"male.png") #******
female_model = pygame.image.load(r"female.png") #*******

'''
            *****
 Нужно указать местоположение артов у вас на компе (как тут) и все должно заработать.
Чекните анимацию, подправьте рисунки если хотите.

Так пока только сделано управление и еще фигня
'''

clock = pygame.time.Clock()
finished = False
finished_game = False

class Player:
    def __init__(self, x, y, scale, gender, step, direction, vel, stand):
        self.x = x
        self.y = y
        self.scale = scale
        self.gender = gender
        self.step = step
        self.direction = direction
        self.vel = vel
        self.stand = stand

    def choose(self):
        self.gender = 1

    def direction_pic(self, event):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction = 1
        if keys[pygame.K_DOWN]:
            self.direction = 0
        if keys[pygame.K_LEFT]:
            self.direction = 2
        if keys[pygame.K_RIGHT]:
            self.direction = 3

        if keys[0]:
            self.stand = 0
        else:
            self.stand = 1

    def bob(self):
        pass

    def draw(self):
        if self.gender == 1:
            player_surface = pygame.transform.scale(male_model, (936, 1132))
        elif self.gender == 0:
            player_surface = pygame.transform.scale(female_model, (936, 1132))

        screen.blit(player_surface, (self.x, self.y), (242*(int(self.step) - 1)*self.stand, 5 + 283*self.direction, 234, 283))

        if self.step > 4.9:
            self.step = 1
        else:
            self.step += 0.1

    def move(self, event):
        keys = pygame.key.get_pressed()

        if self.x > screen_size_x - 220:
            self.x = screen_size_x - 220
        elif self.x < 0:
            self.x = 0

        if self.y > screen_size_y - 280:
            self.y = screen_size_y - 280
        elif self.y < 10:
            self.y = 10

        if keys[pygame.K_UP]:
            self.y -= self.vel[1]*time_interval
        if keys[pygame.K_DOWN]:
            self.y += self.vel[1]*time_interval
        if keys[pygame.K_LEFT]:
            self.x -= self.vel[0]*time_interval
        if keys[pygame.K_RIGHT]:
            self.x += self.vel[0]*time_interval

player = Player(100, 100, 0.5, gender, 1, 0, [200, 200], 0)



'''
Заняться передвижением персонажа по трём линиям (управление стрелочками).
Поставить ограничения, чтобы не заходил за края.
Также организовать начальный экран, выбор пола, ввод никнейма, меню игры и выход из игры.
В дальнейшем добавится возможность ставить на паузу и сохранять (под вопросом).
'''
