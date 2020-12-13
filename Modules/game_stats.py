import pygame
from pygame.draw import *

pygame.init()

screen_size_x = 1000
screen_size_y = 600
FPS = 15

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
ORANGE = (255, 128, 0)

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
screen.fill(WHITE)


def draw_text(text, x, y, color, size):
    """
    The function adds a field with text
    """
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color)
    place = text.get_rect()
    place.center = (x, y)
    screen.blit(text, place)


class Points:
    def __init__(self):
        self.coord_x = screen_size_x - 100
        self.coord_y = 150
        self.points = 0

    def draw(self):
        '''
        The function draws user's points
        '''
        draw_text('Ваша оценка: ' + str(self.points), self.coord_x, self.coord_y, WHITE, 16)


class Mood_scale:
    def __init__(self):
        self.mood_points = 400
        self.mood_color = GREEN
        self.mood_750 = pygame.image.load('images/750.png')
        self.mood_500 = pygame.image.load('images/500.png')
        self.mood_250 = pygame.image.load('images/250.png')
        self.mood_0 = pygame.image.load('images/0.png')
        self.scale = pygame.transform.scale(self.mood_750, (50, 50))

    def draw(self):
        draw_text('Настроение:', screen_size_x - 100, 20, WHITE, 16)
        if self.mood_points >= 300:
            self.mood_color = GREEN
            self.scale = pygame.transform.scale(self.mood_750, (50, 50))
        elif self.mood_points >= 200:
            self.mood_color = YELLOW
            self.scale = pygame.transform.scale(self.mood_500, (50, 50))
        elif self.mood_points >= 100:
            self.mood_color = ORANGE
            self.scale = pygame.transform.scale(self.mood_250, (50, 50))
        else:
            self.mood_color = RED
            self.scale = pygame.transform.scale(self.mood_0, (50, 50))
        self.mood_points -= 1
        rect(screen, self.mood_color, (screen_size_x - self.mood_points // 2 - 50, 35, self.mood_points // 2, 15))
        rect(screen, BLACK, (screen_size_x - 250, 35, 200, 15), 2)
        screen.blit(self.scale, (screen_size_x - 50, 20))


class Boost_scale:
    def __init__(self):
        self.boost_points = 0
        self.boost_color = LIL

    def draw(self):
        draw_text('Усиление:', 40, 20, WHITE, 16)
        if self.boost_points > 0:
            self.boost_points -= 1
            rect(screen, self.boost_color, (10 - self.boost_points + 100, 35, self.boost_points, 15))
            rect(screen, BLACK, (10, 35, 100, 15), 2)


class Timer:
    def __init__(self):
        self.time = 1000
        self.alarm = pygame.image.load('images/alarm.png')
        self.alarm_r = pygame.image.load('images/alarm_r.png')
        self.alarm_l = pygame.image.load('images/alarm_l.png')

    def draw(self):
        if self.time >= 500:
            self.scale = pygame.transform.scale(self.alarm, (50, 50))
        elif (self.time * 2 // FPS) % 2 == 1:
            self.scale = pygame.transform.scale(self.alarm_r, (50, 50))
        else:
            self.scale = pygame.transform.scale(self.alarm_l, (50, 50))
        draw_text('Оставшееся время: ' + str(self.time // FPS), screen_size_x - 150, 100, WHITE, 16)
        screen.blit(self.scale, (screen_size_x - 50, 70))
        self.time -= 1


class Draw_stats:
    def __init__(self):
        self.mood_scale = Mood_scale()
        self.boost_scale = Boost_scale()
        self.timer = Timer()
        self.points = Points()

    def draw_esc(self):
        '''
        The function draws esc hint
        '''
        draw_text('Для паузы нажмите ESC', screen_size_x - 120, screen_size_y - 20, WHITE, 16)

    def draw(self):
        self.mood_scale.draw()
        self.boost_scale.draw()
        self.timer.draw()
        self.points.draw()
        self.draw_esc()
        if self.mood_scale.mood_points <= 0:
            done = 3
        else:
            done = 0
        if self.timer.time <=0:
            done = 4
        return done

if __name__ == "__main__":
    print("This module is not for direct call!")