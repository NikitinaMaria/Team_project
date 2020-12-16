from random import randint
import numpy as np
import pygame
import Modules.game_mechanics
import Modules.game_menu
from pygame.draw import *
from Modules.game_mechanics import *
from Modules.game_menu import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_RED = (168, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (238, 201, 0)
BLACKBOARD = (65, 86, 71)
BLACKBOARD_3 = (81, 78, 36)


class Stream:
    def __init__(self):
        '''
        Set stream's parameters and their meanings
        '''
        # Coordinates of the YouTube button
        self.coord_x = randint(0, 150)
        self.coord_y = randint(150, 400)

        # Time to press the button
        self.click_time = 100

        # The length and width of the button
        self.width = 120
        self.length = 130

        # Images
        self.youtube = pygame.image.load('images/youtube.png')
        self.background = pygame.image.load('images/background.jpg')
        self.background_3 = pygame.image.load('images/background_3.png')
        self.background_4 = pygame.image.load('images/background_4.png')
        self.scale = pygame.transform.scale(self.youtube, (self.length, self.width))

        # Is the event button active or not
        self.stream_is_available = False

        # Is the event active or not
        self.stream_is_on = False

        # Is the user logged out of the game
        self.done = 0

        # The project step depends on the user's choices
        self.step = 1

        # User points
        self.points = 0

    def draw_button(self):
        '''
        The function draws the event button in a random place
        '''
        if self.stream_is_available:
            self.click_time -= 1
            self.scale = pygame.transform.scale(self.youtube, (self.length, self.width))
            screen.blit(self.scale, (self.coord_x, self.coord_y))
            if self.click_time <= 0:
                self.stream_is_available = False

    def button_check(self, events):
        '''
        The function checks whether the user clicked the button
        '''
        for event in events:
            if self.stream_is_available and (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = event.pos
                if (mouse_x > self.coord_x) and (mouse_x < self.coord_x + self.length) and (mouse_y > self.coord_y) and \
                        (mouse_y < self.coord_y + self.width):
                    self.click_time = 0
                    self.stream_is_on = True
                    return True
            else:
                return False

    def pressed_or_not_button(self, events):
        self.draw_button()
        return self.button_check(events)

    def draw(self):
        '''
        The function draws all steps of the event
        '''

        # Start page
        if self.step == 1:
            # Background
            self.scale = pygame.transform.scale(self.background, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD, (screen_size_x // 6, screen_size_y // 12, 10 * screen_size_x // 27,
                                      4 * screen_size_y // 5 + 10))

            # The question of the teacher
            draw_text('Хотите задать вопрос?', screen_size_x // 3 + 25, screen_size_y // 5, WHITE, 28)

            # Answers
            rect(screen, WHITE, (screen_size_x // 6 + 10, 4 * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('Хочу!', screen_size_x // 3 + 25, 4 * screen_size_y // 9 + 35, WHITE, 28)
            rect(screen, WHITE, (screen_size_x // 6 + 10, 6 * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('Пожалуй, нет...', screen_size_x // 3 + 25, 6 * screen_size_y // 9 + 35, WHITE, 28)

        # Selecting a question
        if self.step == 2:

            # Background
            self.scale = pygame.transform.scale(self.background, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD,
                 (screen_size_x // 6, screen_size_y // 12, 10 * screen_size_x // 27, 4 * screen_size_y // 5 + 10))

            # The question of the teacher
            draw_text('Хорошо.', screen_size_x // 3 + 25, screen_size_y // 7, WHITE, 28)
            draw_text('Давайте Ваш вопрос.', screen_size_x // 3 + 25, screen_size_y // 7 + 30, WHITE, 28)

            # Answers
            for i in range(6):
                rect(screen, WHITE,
                     (screen_size_x // 6 + 10, (i + 2) * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('Механика', screen_size_x // 3 + 25, 2 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Термодинамика', screen_size_x // 3 + 25, 3 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Электричество', screen_size_x // 3 + 25, 4 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Магнетизм', screen_size_x // 3 + 25, 5 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Оптика', screen_size_x // 3 + 25, 6 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Квантовая физика', screen_size_x // 3 + 25, 7 * screen_size_y // 9 + 35, WHITE, 28)

        if self.step == 3:
            # Background
            self.scale = pygame.transform.scale(self.background_3, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD_3,
                 (20, screen_size_y // 12, 4 * screen_size_x // 9 - 50, 3 * screen_size_y // 5))

            # Teacher's phrase and congratulations
            draw_text('Что ж...', screen_size_x // 5 + 10, screen_size_y // 7, WHITE, 28)
            draw_text('Давайте обсудим', screen_size_x // 5 + 10, screen_size_y // 7 + 30, WHITE, 28)
            draw_text('эту тему...', screen_size_x // 5 + 10, screen_size_y // 7 + 60, WHITE, 28)
            draw_text('(Поздравляем! Вы не', screen_size_x // 5 + 10, screen_size_y // 3, WHITE, 28)
            draw_text('потратили время впустую', screen_size_x // 5 + 10, screen_size_y // 3 + 30, WHITE, 28)
            draw_text('и заработали балл!)', screen_size_x // 5 + 10, screen_size_y // 3 + 60, WHITE, 28)

            # Answer
            rect(screen, WHITE, (30, screen_size_y // 2, 30 + 4 * screen_size_x // 9 - 100, 70), 3)
            draw_text('Спасибо!', screen_size_x // 5 + 10, screen_size_y // 2 + 35, WHITE, 28)

        if self.step == 4:
            # Background
            self.scale = pygame.transform.scale(self.background_4, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))

            # Teacher's phrase and congratulations
            ellipse(screen, BLACK, (0, screen_size_y // 5, 402, 202), 3)
            ellipse(screen, WHITE, (0, screen_size_y // 5, 400, 200))
            draw_text('Как же так...', screen_size_x // 5, screen_size_y // 3, BLACK, 30)
            draw_text('Вы должны это знать!', screen_size_x // 5, screen_size_y // 3 + 35, BLACK, 30)
            rect(screen, WHITE, (2 * screen_size_x // 3 - 40, screen_size_y // 9, 350, 270))
            rect(screen, BLACK, (2 * screen_size_x // 3 - 40, screen_size_y // 9, 350, 270), 3)
            draw_text('(Поздравляем! Вы', 4 * screen_size_x // 5, screen_size_y // 9 + 40, BLACK, 24)
            draw_text('потратили время впустую', 4 * screen_size_x // 5, screen_size_y // 9 + 70, BLACK, 24)
            draw_text('и ничего не заработали.)', 4 * screen_size_x // 5, screen_size_y // 9 + 100, BLACK, 24)

            # Answer
            rect(screen, BLACK, (2 * screen_size_x // 3 - 30, screen_size_y // 9 + 170, 330, 70), 3)
            draw_text('Вернуться к игре', 4 * screen_size_x // 5, screen_size_y // 9 + 205, BLACK, 24)

        if self.step == 5:
            # Background
            self.scale = pygame.transform.scale(self.background, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD,
                 (screen_size_x // 6, screen_size_y // 12, 10 * screen_size_x // 27, 4 * screen_size_y // 5 + 10))

            # Teacher's phrase
            draw_text('Ну тогда до свидания.', screen_size_x // 3 + 25, screen_size_y // 5, WHITE, 28)
            rect(screen, WHITE, (screen_size_x // 6 + 10, 4 * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)

            # Answer
            draw_text('До свидания.', screen_size_x // 3 + 25, 4 * screen_size_y // 9 + 35, WHITE, 28)

    def answer(self, events):
        '''
        The function checks the user's responses and proceeds to the appropriate stages
        '''
        for event in events:
            # Checking out of the game
            self.done = Modules.game_mechanics.quit_condition(event.type)

            # Checking mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # Responses to the 1 step
                if (self.step == 1) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) and \
                        (mouse_y > 4 * screen_size_y // 9) and (mouse_y < 4 * screen_size_y // 9 + 70):
                    self.step = 2
                elif (self.step == 1) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) \
                        and (mouse_y > 6 * screen_size_y // 9) and (mouse_y < 6 * screen_size_y // 9 + 70):
                    self.step = 5
                    self.points = 0

                # Responses to the 2 step
                elif (self.step == 2) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) \
                        and (mouse_y > 2 * screen_size_y // 9) and (mouse_y < 8 * screen_size_y // 9 + 70):
                    self.step = randint(3, 4)

                # Responses to the 3 step
                elif (self.step == 3) and (mouse_x > 30) and (mouse_x < 4 * screen_size_x // 9 - 40) and \
                        (mouse_y > screen_size_y // 2) and (mouse_y < screen_size_y // 2 + 70):
                    self.stream_is_on = False
                    self.points = 1

                # Responses to the 4 step
                elif (self.step == 4) and (mouse_x > 2 * screen_size_x // 3 - 30) + (
                        mouse_x < 2 * screen_size_x // 3 + 300) \
                        and (mouse_y > screen_size_y // 9 + 170) and (mouse_y < screen_size_y // 9 + 240):
                    self.stream_is_on = False
                    self.points = 0

                # Responses to the 5 step
                elif (self.step == 5) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) and \
                        (mouse_y > 4 * screen_size_y // 9) and (mouse_y < 4 * screen_size_y // 9 + 70):
                    self.stream_is_on = False
                    self.points = 0

    def progress(self, events):
        self.draw()
        self.answer(events)
        if self.stream_is_on == False:
            self.step = 1
            if self.points == 1:
                return (self.done, self.stream_is_on, self.points)
            else:
                return (self.done, self.stream_is_on, 0)
            self.points = 0
        else:
            return (self.done, self.stream_is_on, 0)


class Analit:
    def __init__(self):
        self.ask_time = 100
        self.sweater_time = 200
        self.sweater_is_available = True
        self.done = 0
        self.step = 1
        self.points = 0

        # Images
        self.sweater = pygame.image.load('images/sweater.png')
        self.start_page = pygame.image.load('images/start_page.png')
        self.two_hours = pygame.image.load('images/2_hours.jpg')
        self.bla_bla = pygame.image.load('images/bla_0.png')
        self.bla_0 = pygame.image.load('images/bla_1.png')
        self.bla_1 = pygame.image.load('images/bla_2.png')
        self.bla_2 = pygame.image.load('images/bla_3.png')
        self.bla_3 = pygame.image.load('images/bla_4.png')
        self.bla_4 = pygame.image.load('images/bla_5.png')
        self.bla_5 = pygame.image.load('images/bla_6.png')
        self.bla_6 = pygame.image.load('images/bla_7.png')
        self.bla_7 = pygame.image.load('images/bla_8.png')
        self.bla_8 = pygame.image.load('images/bla_9.png')
        self.bla_9 = pygame.image.load('images/bla_10.png')
        self.bla = [self.bla_0, self.bla_1, self.bla_2, self.bla_3, self.bla_4, self.bla_5, self.bla_6, self.bla_7,
                    self.bla_8, self.bla_9]
        self.bla_x = []
        self.bla_y = []
        for i in range(10):
            self.bla_x.append(randint(0, screen_size_x - 300))
            self.bla_y.append(randint(0, screen_size_y - 400))

        self.bla_bla_time = 0
        self.bla_bla_scale = pygame.transform.scale(self.bla_bla, (800, 1000))
        self.bla_bla_scale.set_colorkey(WHITE)

        self.width = 80
        self.length = 100
        self.scale = pygame.transform.scale(self.sweater, (self.length, self.width))
        self.coord_x = randint(0, screen_size_x - 100)
        self.coord_y = self.coord_y = randint(100, 500)
        self.speed_x = randint(-15, 15)
        self.speed_y = randint(-15, 15)
        self.analit_is_on = False

    def draw_sweater(self):
        if self.sweater_is_available:
            self.scale = pygame.transform.scale(self.sweater, (self.length, self.width))
            self.coord_x += self.speed_x
            self.coord_y += self.speed_y
            if self.coord_x <= 0:
                self.coord_x = 0
                self.speed_x = - self.speed_x
            if self.coord_y <= 0:
                self.coord_y = 0
                self.speed_y = - self.speed_y
            if self.coord_x >= screen_size_x - self.length:
                self.coord_x = screen_size_x - self.length
                self.speed_x = - self.speed_x
            if self.coord_y >= screen_size_y - self.width:
                self.coord_y = screen_size_y - self.width
                self.speed_y = - self.speed_y
            screen.blit(self.scale, (self.coord_x, self.coord_y))

    def check_sweater(self, events):
        for event in events:
            if self.sweater_is_available and (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = event.pos
                if (mouse_x > self.coord_x) and (mouse_x < self.coord_x + self.length) and (mouse_y > self.coord_y) and \
                        (mouse_y < self.coord_y + self.width):
                    self.sweater_is_available = False
                    self.analit_is_on = True
                    return True

    def draw(self):
        self.scale = pygame.transform.scale(self.start_page, (screen_size_x, screen_size_y))
        screen.blit(self.scale, (0, 0))
        if self.step == 1:
            if self.ask_time > 0:
                rect(screen, GOLD, (
                    200 - self.ask_time * 2 + screen_size_x // 5 + 50, screen_size_y // 5 - 50, self.ask_time * 2, 20))
                rect(screen, BLACK, (screen_size_x // 5 + 50, screen_size_y // 5 - 50, 200, 20), 5)
                self.ask_time -= 1
                ellipse(screen, BLACK, (screen_size_x // 5, screen_size_y // 5, 302, 202), 3)
                ellipse(screen, WHITE, (screen_size_x // 5, screen_size_y // 5, 300, 200))
                draw_text('Здавствуйте!', screen_size_x // 5 + 150, screen_size_y // 5 + 60, BLACK, 24)
                draw_text('Хотите что-то нужное', screen_size_x // 5 + 150, screen_size_y // 5 + 90, BLACK, 24)
                draw_text('или интересное?', screen_size_x // 5 + 150, screen_size_y // 5 + 120, BLACK, 24)
                ellipse(screen, BLACK, (screen_size_x // 5, 3 * screen_size_y // 5, 402, 101), 3)
                ellipse(screen, WHITE, (screen_size_x // 5, 3 * screen_size_y // 5, 400, 100))
                draw_text('Давайте обсудим домашку', screen_size_x // 5 + 200, 3 * screen_size_y // 5 + 50, BLACK, 24)
                ellipse(screen, BLACK, (screen_size_x // 5, 4 * screen_size_y // 5, 402, 101), 3)
                ellipse(screen, WHITE, (screen_size_x // 5, 4 * screen_size_y // 5, 400, 100))
                draw_text('Что-то другое...', screen_size_x // 5 + 200, 4 * screen_size_y // 5 + 50, BLACK, 24)
            else:
                self.step = 3
        if self.step == 2:
            self.points = 1
            ellipse(screen, BLACK, (screen_size_x // 5, screen_size_y // 5 - 40, 402, 302), 3)
            ellipse(screen, WHITE, (screen_size_x // 5, screen_size_y // 5 - 40, 400, 300))
            draw_text('Поздравляю!', screen_size_x // 5 + 200, screen_size_y // 5 + 60, BLACK, 24)
            draw_text('Вы сделали мудрый выбор,', screen_size_x // 5 + 200, screen_size_y // 5 + 90, BLACK, 24)
            draw_text('и усвоенный вами материал', screen_size_x // 5 + 200, screen_size_y // 5 + 120, BLACK, 24)
            draw_text('наверняка пригодится Вам', screen_size_x // 5 + 200, screen_size_y // 5 + 150, BLACK, 24)
            draw_text('на экзамене.', screen_size_x // 5 + 200, screen_size_y // 5 + 180, BLACK, 24)
            ellipse(screen, BLACK, (screen_size_x // 5, 4 * screen_size_y // 5, 402, 101), 3)
            ellipse(screen, WHITE, (screen_size_x // 5, 4 * screen_size_y // 5, 400, 100))
            draw_text('Спасибо!', screen_size_x // 5 + 200, 4 * screen_size_y // 5 + 50, BLACK, 24)
        if self.step == 3:
            if self.bla_bla_time == 0:
                pygame.mixer.music.load('audio/Fine.mp3')
                pygame.mixer.music.play()
            if self.bla_bla_time < 400:
                for i in range(10):
                    if self.bla_bla_time > i * 40:
                        self.bla_scale = pygame.transform.scale(self.bla[i], (350, 500))
                        screen.blit(self.bla_scale, (self.bla_x[i], self.bla_y[i]))
                screen.blit(self.bla_bla_scale, (100, - self.bla_bla_time))
                self.bla_bla_time += 2
            elif (self.bla_bla_time >= 400) and (self.bla_bla_time <= 471):
                if self.bla_bla_time == 400:
                    pygame.mixer.music.load('audio/Later.mp3')
                    pygame.mixer.music.play()
                self.scale = pygame.transform.scale(self.two_hours, (screen_size_x, screen_size_y))
                screen.blit(self.scale, (0, 0))
                self.bla_bla_time += 2
            else:
                self.analit_is_on = False

    def pressed_or_not_button(self, events):
        # self.draw_sweater()
        return self.check_sweater(events)

    def answer(self, events):
        for event in events:
            self.done = Modules.game_mechanics.quit_condition(event.type)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (self.step == 1) and (mouse_x >= screen_size_x // 5) and (mouse_x <= screen_size_x // 5 + 400) \
                        and (mouse_y >= 3 * screen_size_y // 5) and (mouse_y <= 3 * screen_size_y // 5 + 100):
                    self.step = 2
                if (self.step == 1) and (mouse_x >= screen_size_x // 5) and (mouse_x <= screen_size_x // 5 + 400) \
                        and (mouse_y >= 4 * screen_size_y // 5) and (mouse_y <= 4 * screen_size_y // 5 + 100):
                    self.step = 3
                if (self.step == 2) and (mouse_x >= screen_size_x // 5) and (mouse_x <= screen_size_x // 5 + 400) \
                        and (mouse_y >= 4 * screen_size_y // 5) and (mouse_y <= 4 * screen_size_y // 5 + 100):
                    self.analit_is_on = False

    def progress(self, events):
        self.draw()
        self.answer(events)
        if self.analit_is_on == False:
            self.step = 1
            self.ask_time = 100
            self.sweater_time = 200
            if self.points == 1:
                return (self.done, self.analit_is_on, self.points)
            else:
                return (self.done, self.analit_is_on, 0)
            self.points = 0
        else:
            return (self.done, self.analit_is_on, 0)


class Ivanov_test():
    def __init__(self):
        '''
        Set test's parameters and their meanings
        '''
        self.time = 0
        self.length = min(screen_size[0] // 7, screen_size[1] // 7)
        self.done = 0
        self.time_is_over = False
        self.time_limit = 15 * FPS
        self.growing_time = 1 * FPS
        self.x = screen_size[0] // 2
        self.y = screen_size[1] // 4
        self.task = []
        self.length_of_answer_pic = self.length // 3
        self.create_task()
        self.number_of_task = 1
        self.answer_list = []
        self.score = 0
        self.length_of_asterisk = self.length_of_answer_pic
        self.numerous = 1

    def progress(self, events):
        '''
        Manager function for all processes in test
        '''
        self.time += 1
        self.draw()
        self.user_events(events)
        if self.time == self.time_limit + 3 * self.growing_time:
            self.time_is_over = True
        if self.time_is_over:
            return (self.done, not self.time_is_over, self.score)
        else:
            return (self.done, not self.time_is_over, 0)

    def create_task(self):
        '''
        Make the new list with numbers for numbers wich mean:
        1 - for all
        2 - exist
        3 - equivalent (then and only then, when)
        4 - epsilon
        '''
        self.task = []
        for i in range(5):
            self.task.append(randint(1, 4))

    def draw(self):
        '''
        Draws all images and pictures in test
        '''
        time_scale = screen_size[0] / self.time_limit
        rect(screen, RED, (0, 0, int(self.time * time_scale), 10))
        if self.time <= self.growing_time:
            Modules.game_mechanics.insert_text("Dancing time!", "Fonts/Game-font.ttf", GREEN,
                                               (screen_size[0] // 2, screen_size[1] // 2),
                                               self.time * self.time)
        else:
            if self.number_of_task <= 4 and self.time <= self.time_limit:
                self.draw_task()
                for i in range(4):
                    Modules.game_mechanics.insert_text(str(i + 1) + ') ', "Fonts/Game-font.ttf", BLACK,
                                                       (screen_size[0] // 12,
                                                        i * self.length_of_answer_pic + screen_size[1] // 5), 20)
                rect(screen, BLACK, (screen_size[0] // 2 - 5 * self.length_of_asterisk // 2 - 3,
                                     2 * screen_size[1] // 5 - self.length_of_asterisk // 2,
                                     5 * self.length_of_asterisk + 6, self.length_of_asterisk + 6), 3)
                self.draw_Celentano()
            if (self.number_of_task >= 5) or (self.time >= self.time_limit):
                screen.fill(GREY)
                FPS = 15
                pygame.mixer.music.stop()
                if self.score == 0:
                    self.draw_zero_score()
                if self.score == 4:
                    self.draw_max_score()
                if self.score == 1 or self.score == 2:
                    Modules.game_mechanics.insert_text('Not so bad', 'Fonts/Game-font.ttf', BLACK,
                                                       (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                                       min(screen_size[0] // 9, screen_size[1] // 9))
                if self.score == 3:
                    Modules.game_mechanics.insert_text('Just great!', 'Fonts/Game-font.ttf', GREEN,
                                                       (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                                       min(screen_size[0] // 9, screen_size[1] // 8))
                for i in range(4):
                    Modules.game_mechanics.insert_text(str(i + 1) + ') ', "Fonts/Game-font.ttf", WHITE,
                                                       (screen_size[0] // 12,
                                                        i * self.length_of_answer_pic + screen_size[1] // 5), 20)
            self.draw_right_or_wrong_answer()
        pygame.display.update()

    def draw_zero_score(self):
        '''
        Puts falure picture on the screen
        '''
        Modules.game_mechanics.insert_picture('images/Falure.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                                              (screen_size[0], screen_size[1]))
        Modules.game_mechanics.insert_text('You need to work harder', 'Fonts/Game-font.ttf', WHITE,
                                           (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                           min(screen_size[0] // 9, screen_size[1] // 9))

    def draw_max_score(self):
        '''
        Puts happy Ivanov's picture on the screen
        '''
        Modules.game_mechanics.insert_picture('images/Happy_master.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                                              (screen_size[0], screen_size[1]))
        Modules.game_mechanics.insert_text('Master is proud of you', 'Fonts/Game-font.ttf', GOLD,
                                           (screen_size[0] // 2, 2 * screen_size[1] // 3),
                                           min(screen_size[0] // 9, screen_size[1] // 9))

    def draw_Celentano(self):
        if self.time <= 9:
            Modules.game_mechanics.insert_picture('Videos1/ezgif-frame-00' + str(self.time) + '.jpg',
                                                  (screen_size[0] // 4, 3 * screen_size[1] // 4),
                                                  (screen_size[0] // 2, screen_size[1] // 2))
        elif self.time <= 99 and self.time >= 10:
            Modules.game_mechanics.insert_picture('Videos1/ezgif-frame-0' + str(self.time) + '.jpg',
                                                  (screen_size[0] // 4, 3 * screen_size[1] // 4),
                                                  (screen_size[0] // 2, screen_size[1] // 2))
        elif self.time >= 100 and self.time <= 199:
            Modules.game_mechanics.insert_picture('Videos2/ezgif-frame-' + str(self.time) + '.jpg',
                                                  (screen_size[0] // 4, 3 * screen_size[1] // 4),
                                                  (screen_size[0] // 2, screen_size[1] // 2))
        elif self.time > 199 and self.time <= 208:
            Modules.game_mechanics.insert_picture('Videos1/ezgif-frame-00' + str(self.time - 199) + '.jpg',
                                                  (screen_size[0] // 4, 3 * screen_size[1] // 4),
                                                  (screen_size[0] // 2, screen_size[1] // 2))
        else:
            Modules.game_mechanics.insert_picture('Videos1/ezgif-frame-0' + str(self.time - 199) + '.jpg',
                                                  (screen_size[0] // 4, 3 * screen_size[1] // 4),
                                                  (screen_size[0] // 2, screen_size[1] // 2))

    def draw_right_or_wrong_answer(self):
        '''
        Putting pictures of green arrow for right answer or red X for wrong answer
        '''
        if self.time <= self.time_limit:
            for i in range(self.numerous - 1):
                Modules.game_mechanics.insert_picture('images/asterisk.png', (
                    screen_size[0] // 2 - 4 * self.length_of_asterisk // 2 + i * self.length_of_asterisk,
                    2 * screen_size[1] // 5),
                                                      (self.length_of_asterisk, self.length_of_asterisk))
        for i in range(self.number_of_task - 1):
            if self.answer_list[i] == True:
                Modules.game_mechanics.insert_picture('images/right_ans.png', (
                    screen_size[0] // 12 + self.length_of_answer_pic,
                    i * self.length_of_answer_pic + screen_size[1] // 5),
                                                      (self.length_of_answer_pic, self.length_of_answer_pic))
            else:
                Modules.game_mechanics.insert_picture('images/wrong.jpg', (
                    screen_size[0] // 12 + self.length_of_answer_pic,
                    i * self.length_of_answer_pic + screen_size[1] // 5),
                                                      (self.length_of_answer_pic, self.length_of_answer_pic))

    def user_events(self, events):
        '''
        Analize events from keyboard, mouse, etc.
        '''
        for event in events:
            self.done = Modules.game_mechanics.quit_condition(event.type)
            if (self.time >= self.growing_time) and (event.type == pygame.KEYUP) and (self.time <= self.time_limit):
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (self.number == 4):
                    self.task.pop(len(self.task) - 1)
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and (self.number == 3):
                    self.task.pop(len(self.task) - 1)
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and (self.number == 1):
                    self.task.pop(len(self.task) - 1)
                elif (event.key == pygame.K_w or event.key == pygame.K_UP) and (self.number == 2):
                    self.task.pop(len(self.task) - 1)
                else:
                    if self.number_of_task <= 4:
                        self.answer_list.append(False)
                        self.create_task()
                        self.number_of_task += 1
                        self.numerous = 0
                if len(self.task) == 0 and self.number_of_task <= 4:
                    self.create_task()
                    self.answer_list.append(True)
                    self.number_of_task += 1
                    self.score += 1
                    self.numerous = 0
                if (self.numerous <= 4) and (self.number_of_task <= 4):
                    self.numerous += 1
                if self.number_of_task == 5:
                    self.time = self.time_limit

    def draw_task(self):
        '''
        Draws pictures of epsilon, for_all and so on according to the final element of the task_list
        '''
        rect(screen, BLACK,
             (self.x - self.length // 2 - 10, self.y - self.length // 2 - 10, self.length + 20, self.length + 20), 5)
        self.number = self.task[len(self.task) - 1]
        if self.number == 1:
            self.draw_for_all()
        elif self.number == 2:
            self.draw_exist()
        elif self.number == 3:
            self.draw_equivalent()
        else:
            self.draw_epsilon()
        Modules.game_mechanics.insert_picture('images/Hint.png', (4 * screen_size[0] // 5, screen_size[1] // 3),
                                              (screen_size[0] // 3, screen_size[1] // 3))

    def draw_for_all(self):
        line(screen, BLACK, (self.x - self.length // 2, self.y - self.length // 2), (self.x, self.y + self.length // 2),
             5)
        line(screen, BLACK, (self.x, self.y + self.length // 2), (self.x + self.length // 2, self.y - self.length // 2),
             5)
        line(screen, BLACK, (self.x - self.length // 4, self.y), (self.x + self.length // 4, self.y), 5)

    def draw_exist(self):
        for i in range(3):
            line(screen, BLACK, (self.x - self.length // 4, self.y - self.length // 2 + (self.length // 2) * i),
                 (self.x + self.length // 2, self.y - self.length // 2 + (self.length // 2) * i), 5)
        line(screen, BLACK, (self.x + self.length // 2, self.y - self.length // 2),
             (self.x + self.length // 2, self.y + self.length // 2), 5)

    def draw_equivalent(self):
        line(screen, BLACK, (self.x - self.length // 4, self.y - self.length // 8),
             (self.x + self.length // 4, self.y - self.length // 8), 5)
        line(screen, BLACK, (self.x - self.length // 4, self.y + self.length // 8),
             (self.x + self.length // 4, self.y + self.length // 8), 5)
        for i in range(-1, 3, 2):
            line(screen, BLACK, (self.x - i * self.length // 2, self.y),
                 (self.x - i * self.length // 13, self.y - self.length // 4 + 4), 5)
            line(screen, BLACK, (self.x - i * self.length // 2, self.y),
                 (self.x - i * self.length // 13, self.y + self.length // 4 - 4), 5)

    def draw_epsilon(self):
        Modules.game_mechanics.insert_picture('images/epsilon.jpg', (self.x, self.y), (self.length, self.length))


class Kozhevnikov_test():
    def __init__(self):
        '''
        Set test's parameters and thier meanings
        '''
        self.time = 0
        self.length = min(screen_size[0] // 7, screen_size[1] // 7)
        self.done = 0
        # sets the logo an backstage music, but not activates it
        self.sound_logo = pygame.mixer.Sound('audio/Hello_sound.ogg')
        pygame.mixer.music.load('audio/backstage.ogg')
        self.time_is_over = False
        self.time_limit = 65 * FPS
        self.growing_time = 5 * FPS
        self.answer_music_time = 4 * FPS
        self.time_picture = 3 * FPS
        self.time_start = self.time_limit + 4 * self.growing_time
        self.number_of_task = 1
        self.task_list = []
        self.create_task()
        self.score = 0
        self.number_of_answer = 0
        self.answer_is_set = False
        self.number_of_question = 0

    def progress(self, events):
        '''
        Manager function for all processes in test, makes it work and finish
        '''
        if self.time >= self.time_limit:
            self.draw_score()
            if self.time == self.time_limit + self.time_picture:
                self.time_is_over = True
                pygame.mixer.music.stop()
        else:
            if self.time == 0:
                self.sound_logo.play()
            if self.time == self.growing_time + 1:
                pygame.mixer.music.play()
            if self.time <= self.growing_time:
                self.draw_logo()
            else:
                self.draw()
            self.user_events(events)
            if self.time >= self.time_start + self.answer_music_time and self.time <= self.time_start + self.answer_music_time + self.time_picture:
                if self.answer_is_set == True and self.number_of_answer == self.number_of_question:
                    self.draw_Kozhevnikov('images/Happy_Kozhevnikov.jpg', 'audio/correct.ogg', 'Right answer!', GREEN)
                    if self.time == self.time_start + self.answer_music_time:
                        self.score += 1
                else:
                    self.draw_Kozhevnikov('images/Sad_Kozhevnikov.png', 'audio/wrong.ogg', 'Wrong answer!', RED)
        self.time += 1
        if self.time_is_over:
            return (self.done, not self.time_is_over, 4 * self.score // 5)
        else:
            return (self.done, not self.time_is_over, 0)

    def create_task(self):
        '''
        Reads task from text file, puts it in list according to the number of question
        '''
        with open('Text_files/text.txt', encoding='utf-8') as file:
            array = []
            for line in file:
                if line == 'fff\n':
                    self.task_list.append(array)
                    array = []
                else:
                    line.encode()
                    array.append(line)

    def draw_Kozhevnikov(self, name, audio, text, color):
        '''
        Draws picture with the text on it, turns on and off backstage music, switches active question form to another
        '''
        Modules.game_mechanics.insert_picture(name, (screen_size[0] // 2, screen_size[1] // 2), screen_size)
        Modules.game_mechanics.insert_text(text, 'Fonts/Game-font.ttf', color,
                                           (screen_size[0] // 2, 7 * screen_size[1] // 8),
                                           min(screen_size[0] // 8, screen_size[1] // 8))
        if self.time == self.time_start + self.answer_music_time:
            sound2 = pygame.mixer.Sound(audio)
            sound2.play()
        if self.time == self.time_start + self.answer_music_time + self.time_picture:
            if self.number_of_task == 5:
                self.time = self.time_limit
            else:
                self.number_of_task += 1
                self.number_of_answer = 0
                self.answer_is_set = False
                pygame.mixer.music.load('audio/backstage.ogg')
                pygame.mixer.music.play()

    def in_rectangle(self, position, length):
        '''
        Looks, if user's click was in appropriate rectangle such as, for example, variant of answer
        '''
        if self.coord[1] >= position[1] and self.coord[1] < position[1] + length:
            return True
        else:
            return False

    def user_events(self, events):
        '''
        Analyzes user's actions such as clicking, if the click was on variant of answer make a veto on choosing another variant
        Don't count the click on the other field like the question table
        '''
        for event in events:
            self.done = Modules.game_mechanics.quit_condition(event.type)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    self.coord = pygame.mouse.get_pos()
                    if not self.in_rectangle((0, 0), 39 * screen_size[1] // 80):
                        for i in range(4):
                            if self.in_rectangle((0, (39 + 10 * i) * screen_size[1] // 80),
                                                 10 * screen_size[1] // 80) and self.answer_is_set == False:
                                self.number_of_answer = 1 + i
                                self.answer_is_set = True
                                pygame.mixer.music.stop()
                                sound2 = pygame.mixer.Sound('audio/answer.ogg')
                                sound2.play()
                                self.time_start = self.time
                                if self.time + self.answer_music_time + self.time_picture >= self.time_limit:
                                    self.time_limit = self.time + self.answer_music_time + self.time_picture

    def draw_logo(self):
        '''
        Draws logo of the game
        '''
        Modules.game_mechanics.insert_picture('images/quiz.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                                              screen_size)

    def draw(self):
        '''
        Draws answer sheet table, make chosen answer colorized orange
        '''
        screen.fill(WHITE)
        Modules.game_mechanics.insert_picture('images/Answer_sheet' + str(self.number_of_answer) + '.png',
                                              (screen_size[0] // 2, screen_size[1] // 2), screen_size)
        Modules.game_mechanics.insert_text('Вопрос ' + str(self.number_of_task), 'Fonts/Kozhevnikov.ttf', WHITE,
                                           (5 * min(screen_size[1] // 20, screen_size[0] // 20),
                                            1 * screen_size[1] // 20), min(screen_size[1] // 15, screen_size[0] // 15))
        count = 0
        task = self.task_list[self.number_of_task - 1]
        inserted_text_of_question = False
        for string in task:
            if string == 'f\n':
                inserted_text_of_question = True
                count = -1
            if string == 'r\n':
                self.number_of_question = count + 1
                count += -1
            if not inserted_text_of_question:
                Modules.game_mechanics.insert_text(string, 'Fonts/Kozhevnikov.ttf', WHITE,
                                                   (screen_size[0] // 2, (4 + count) * screen_size[1] // 20),
                                                   min(screen_size[1] // 15, screen_size[0] // 15))
            elif count >= 0 and string != 'r\n':
                Modules.game_mechanics.insert_text(string[0: len(string) - 3], 'Fonts/Kozhevnikov.ttf', WHITE, (
                    35 * int(string[len(string) - 3:len(string) - 1]) / 100 * min(screen_size[1] // 25,
                                                                                  screen_size[0] // 25),
                    (44 + 10 * count) * screen_size[1] // 80), min(screen_size[1] // 15, screen_size[0] // 15))
            count += 1

    def draw_score(self):
        '''
        Draws different variants of the final table score according to the user's score
        '''
        screen.fill(GREY)
        if self.score == 0 or self.score == 1:
            self.draw_zero_score()
        if self.score == 5:
            self.draw_max_score()
        if self.score == 3 or self.score == 2:
            Modules.game_mechanics.insert_text('Not so bad', 'Fonts/Game-font.ttf', BLACK,
                                               (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                               min(screen_size[0] // 9, screen_size[1] // 9))
            Modules.game_mechanics.insert_text(str(self.score), 'Fonts/Game-font.ttf', BLACK,
                                               (screen_size[0] // 2, screen_size[1] // 2),
                                               min(screen_size[0] // 5, screen_size[1] // 5))
        if self.score == 4:
            Modules.game_mechanics.insert_text('Just great!', 'Fonts/Game-font.ttf', GREEN,
                                               (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                               min(screen_size[0] // 5, screen_size[1] // 5))
            Modules.game_mechanics.insert_text(str(self.score), 'Fonts/Game-font.ttf', GREEN,
                                               (screen_size[0] // 2, screen_size[1] // 2),
                                               min(screen_size[0] // 5, screen_size[1] // 5))
        pygame.display.update()

    def draw_zero_score(self):
        '''
        Puts sad falure picture on the screen
        '''
        Modules.game_mechanics.insert_picture('images/Falure.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                                              (screen_size[0], screen_size[1]))
        Modules.game_mechanics.insert_text('You need to work harder', 'Fonts/Game-font.ttf', WHITE,
                                           (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                           min(screen_size[0] // 9, screen_size[1] // 9))

    def draw_max_score(self):
        '''
        Draws Kozhevnikov in role of the master of the world picture with words on it
        '''
        Modules.game_mechanics.insert_picture('images/Master_of_the_world.jpg',
                                              (screen_size[0] // 2, screen_size[1] // 2),
                                              (screen_size[0], screen_size[1]))
        Modules.game_mechanics.insert_text('Master is proud of you', 'Fonts/Game-font.ttf', GOLD,
                                           (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                           min(screen_size[0] // 9, screen_size[1] // 9))


class Endings:
    def __init__(self, number, final_points):
        self.number = number
        self.final_points = final_points

        # Images
        self.fox = pygame.image.load('images/fox.png')
        self.hor = pygame.image.load('images/hor.png')
        self.konfetti = pygame.image.load('images/konfetti.png')
        self.fail = pygame.image.load('images/fail.jpg')
        self.fail_black = pygame.image.load('images/fail_black.jpg')
        self.sleep = pygame.image.load('images/sleep.jpg')
        self.matrix = pygame.image.load('images/matrix.jpg')
        self.left_cloud = pygame.image.load('images/left_cloud.png')
        self.right_cloud = pygame.image.load('images/right_cloud.png')
        self.cat = pygame.image.load('images/DGAP-cat.jpg')
        self.fopf = pygame.image.load('images/fopf.jpg')
        self.cry = pygame.image.load('images/cry.jpg')
        self.impossible = pygame.image.load('images/impossible.jpg')

    def quit_or_not(self):
        while self.number != 1:
            for event in pygame.event.get():
                self.number = Modules.game_mechanics.quit_condition(event.type)

    def end_2(self):
        # The player encountered an obstacle
        screen.fill(WHITE)
        self.scale = pygame.transform.scale(self.fail, (screen_size_x // 5, screen_size_y // 4))
        screen.blit(self.scale, (0, 0))
        draw_text('Притяжение к кровати оказалось сильнее Вас...', screen_size_x // 2,
                  screen_size_y // 2 - 90, BLACK, 24)
        self.scale = pygame.transform.scale(self.sleep, (screen_size_x // 4, screen_size_y // 3))
        screen.blit(self.scale, (screen_size_x // 2 - screen_size_x // 10, screen_size_y // 2))
        pygame.display.update()
        self.quit_or_not()
        self.score = ': уснул :)'
        self.rank = 2

    def end_3(self):
        # The player has run out of mood scale
        screen.fill(WHITE)
        self.scale = pygame.transform.scale(self.fail, (screen_size_x // 5, screen_size_y // 4))
        screen.blit(self.scale, (0, 0))
        draw_text('Вы настолько увлеклись подготовкой к экзаменам,', screen_size_x // 2,
                  screen_size_y // 2 - 150, BLACK, 24)
        draw_text('что забыли про реальную жизнь.', screen_size_x // 2,
                  screen_size_y // 2 - 120, BLACK, 24)
        draw_text('Дни превратились в одну сплошную учёбу без каких-либо радостей,', screen_size_x // 2,
                  screen_size_y // 2 - 90, BLACK, 24)
        draw_text('и в какой-то момент Ваше настроение скатилось к нулю.', screen_size_x // 2,
                  screen_size_y // 2 - 60, BLACK, 24)
        draw_text('Уныние погубило Вас...', screen_size_x // 2,
                  screen_size_y // 2 - 30, BLACK, 24)
        self.scale = pygame.transform.scale(self.fox, (screen_size_x // 5, screen_size_y // 3))
        screen.blit(self.scale, (screen_size_x // 2 - screen_size_x // 10, screen_size_y // 2))
        pygame.display.update()
        self.quit_or_not()
        self.score = ': взгрустнул :('
        self.rank = 1

    def end_5(self):
        # Bad end
        screen.fill(BLACK)
        self.scale = pygame.transform.scale(self.fail_black, (screen_size_x // 5 + 50, screen_size_y // 4))
        screen.blit(self.scale, (0, 0))
        self.scale = pygame.transform.scale(self.cat, (screen_size_x // 2, 2 * screen_size_y // 3))
        screen.blit(self.scale, (screen_size_x // 4, screen_size_y // 2 - 150))
        draw_text('До встречи через год...', screen_size_x // 2, screen_size_y // 3 - 50, DARK_RED, 50)
        draw_text('И помните: это только начало...', screen_size_x // 2, screen_size_y - 30, DARK_RED, 39)
        pygame.display.update()
        self.quit_or_not()
        self.score = ': академщик :O'
        self.rank = 0

    def end_6(self):
        # Normal end
        screen.fill(WHITE)
        self.scale = pygame.transform.scale(self.cry, (screen_size_x // 5, screen_size_y // 3))
        screen.blit(self.scale, (screen_size_x // 2 - screen_size_x // 10, screen_size_y // 2))
        draw_text('Стипендии Вам не видать, но Вы хотя бы смогли выжить.', screen_size_x // 2,
                  screen_size_y // 2 - 120, BLACK, 24)
        draw_text('Это уже можно считать достижением! Поздравляем!', screen_size_x // 2,
                  screen_size_y // 2 - 90, BLACK, 24)
        draw_text('Ваш балл: уд(' + str(self.final_points) + ')', screen_size_x // 2,
                  screen_size_y // 2 - 60, BLACK, 24)
        pygame.display.update()
        self.quit_or_not()
        self.score = ': удос ' + str(self.final_points) + ' =]'
        self.rank = 3

    def end_7(self):
        # Good end
        screen.fill(WHITE)
        self.scale = pygame.transform.scale(self.hor, (screen_size_x // 5, screen_size_y // 3))
        screen.blit(self.scale, (screen_size_x // 2 - screen_size_x // 10, screen_size_y // 2))
        draw_text('На абрамовку Вы не тянете, но результат очень неплох.', screen_size_x // 2,
                  screen_size_y // 2 - 120, BLACK, 24)
        draw_text('Поздавляем! Вы заслужили небольшой отдых и стипендию!', screen_size_x // 2,
                  screen_size_y // 2 - 90, BLACK, 24)
        draw_text('Ваш балл: хор(' + str(self.final_points) + ')', screen_size_x // 2,
                  screen_size_y // 2 - 60, BLACK, 24)
        pygame.display.update()
        self.quit_or_not()
        self.score = ': хорош ' + str(self.final_points) + ' =>'
        self.rank = 4

    def end_8(self):
        # Happy end
        screen.fill(WHITE)
        self.scale = pygame.transform.scale(self.fopf, (screen_size_x // 5, screen_size_y // 3))
        screen.blit(self.scale, (screen_size_x // 2 - screen_size_x // 10, screen_size_y // 2))
        draw_text('Непрерывный бот принёс свои плоды.', screen_size_x // 2,
                  screen_size_y // 2 - 150, BLACK, 24)
        draw_text('Мы восхищены Вами! Результат настоящего ФОПФа.', screen_size_x // 2,
                  screen_size_y // 2 - 120, BLACK, 24)
        draw_text('(Если, конечно, Вы не списали).', screen_size_x // 2,
                  screen_size_y // 2 - 90, BLACK, 24)
        draw_text('Ваш балл: отл(' + str(self.final_points) + ')', screen_size_x // 2,
                  screen_size_y // 2 - 60, BLACK, 24)
        pygame.display.update()
        self.quit_or_not()
        self.score = ': отл (nice) ' + str(self.final_points) + ' =3'
        self.rank = 5

    def end_9(self):
        # Best end
        screen.fill(WHITE)
        self.scale = pygame.transform.scale(self.impossible, (screen_size_x // 2, screen_size_y // 2 - 30))
        screen.blit(self.scale, (screen_size_x // 2 - screen_size_x // 4, screen_size_y // 2))
        self.scale = pygame.transform.scale(self.konfetti, (screen_size_x, screen_size_y))
        screen.blit(self.scale, (0, 0))
        draw_text('Не верится глазам! Вы совершили невозможное!', screen_size_x // 2,
                  screen_size_y // 2 - 150, BLACK, 24)
        draw_text('Признайтесь, Вы использовали грязные приёмы.', screen_size_x // 2,
                  screen_size_y // 2 - 120, BLACK, 24)
        draw_text('Что ж... От души поздравляем!', screen_size_x // 2,
                  screen_size_y // 2 - 90, BLACK, 24)
        draw_text('Ваш балл: отл(10)', screen_size_x // 2,
                  screen_size_y // 2 - 60, BLACK, 24)
        pygame.display.update()
        self.quit_or_not()
        self.score = ': отл (wow) ' + str(self.final_points) + ' =D'
        self.rank = 6

    def end_4(self):
        # Time's up
        if self.final_points <= 2:

            # Event when the player has a low score
            screen.fill(WHITE)
            self.scale = pygame.transform.scale(self.matrix, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACK, (screen_size_x // 5, 0, 3 * screen_size_x // 5, 75), 3)
            rect(screen, WHITE, (screen_size_x // 5, 0, 3 * screen_size_x // 5, 75))
            draw_text('Ваши баллы слишком малы.', screen_size_x // 2, 25, BLACK, 24)
            draw_text('У меня есть для Вас два варианта.', screen_size_x // 2, 50, BLACK, 24)
            self.scale = pygame.transform.scale(self.left_cloud, (screen_size_x // 3, screen_size_y // 3))
            screen.blit(self.scale, (0, screen_size_y // 2))
            draw_text('Академ', screen_size_x // 6, 2 * screen_size_y // 3 - 20, RED, 30)
            self.scale = pygame.transform.scale(self.right_cloud, (screen_size_x // 3, screen_size_y // 3))
            screen.blit(self.scale, (2 * screen_size_x // 3, screen_size_y // 2))
            draw_text('Академ', 5 * screen_size_x // 6, 2 * screen_size_y // 3 - 20, BLUE, 30)
            pygame.display.update()
            self.score = ': академщик :O'
            self.rank = 0

            # Checking user selection
            while self.number != 1:
                for event in pygame.event.get():
                    self.number = Modules.game_mechanics.quit_condition(event.type)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if (((mouse_x >= 0) and (mouse_x <= screen_size_x // 3)) or ((mouse_x >= 2 * screen_size_x // 3) and (mouse_x <= screen_size_x))) and (mouse_y >= screen_size_y // 2) and (mouse_y <= 5 * screen_size_y // 6):
                            self.end_5()
        else:
            if (self.final_points >= 3) and (self.final_points <= 4):
                self.end_6()
            elif (self.final_points >= 5) and (self.final_points <= 7):
                self.end_7()
            elif (self.final_points >= 8) and (self.final_points <= 9):
                self.end_8()
            elif self.final_points >= 10:
                self.end_9()

    def end(self):
        if self.number == 2:
            self.end_2()
        elif self.number == 3:
            self.end_3()
        elif self.number == 4:
            self.end_4()

class Evening():
    def __init__(self):
        '''
        Set test's parameters and thier meanings
        '''
        self.time = 0
        self.done = 0
        self.time_is_over = False
        self.time_limit = 21 * FPS
        self.time_text = 10 * FPS
        self.reading_time = 10 * FPS
        self.text_list = self.text_choice1 = self.text_choice0 = []
        self.score = 0
        self.text_list = self.read_file('Evening')
        self.text_choice0 = self.read_file('Choice0')
        self.text_choice1 = self.read_file('Choice1')
        self.choice = 1

    def progress(self, events):
        '''
        Manager function for all processes in test, makes it work and finish
        If time for the choice is over gives back resalt for choice 0
        '''
        self.user_events(events)
        if self.time >= self.time_limit - self.reading_time:
            self.draw_result()
            if self.time == self.time_limit:
                self.time_is_over = True
        else:
            if self.time <= self.time_text:
                self.draw_text()
            else:
                self.draw()
                self.time -= 1
        self.time += 1
        if self.time_is_over:
            return (self.done, not self.time_is_over, self.score)
        else:
            return (self.done, not self.time_is_over, 0)

    def draw_result(self):
        '''
        Draws final page with results of user's choice
        '''
        if self.choice == 0:
            Modules.game_mechanics.insert_picture('images/Lab.jpg', (screen_size[0] // 2, 3 * screen_size[1] // 4), (screen_size[0] // 2, screen_size[1] // 2))
            self.print_text(self.text_choice0, screen_size[0] // 2)
        if self.choice == 1:
            Modules.game_mechanics.insert_picture('images/Horror.jpg', (screen_size[1] // 3, screen_size[1] // 2),
                                                 (2 * screen_size[1] // 3, screen_size[1]))
            self.print_text(self.text_choice1, 11 * screen_size[0] // 16)

    def read_file(self, name):
        '''
        Returns back the list with strings from the file named in name
        '''
        array = []
        with open('Text_files/'+ name + '.txt', encoding='utf-8') as file:
            String = []
            for line in file:
                if line == '\n':
                    array.append(String)
                    String = []
                else:
                    line.encode()
                    String.append(line)
        return array

    def print_text(self, array, position):
        '''
        Prints text on the screan according to its x position
        '''
        count = 0
        for string in array:
            count += 1
            Modules.game_mechanics.insert_text(string[0], 'Fonts/Kozhevnikov.ttf', BLACK,
                                               (position, (count) * screen_size[1] // 13),
                                               min(screen_size[1] // 15, screen_size[0] // 15))
    def draw_text(self):
        '''
        Draws text in the beggining
        '''
        screen.fill(GREY)
        count = -1
        for string in self.text_list:
            count += 1
            Modules.game_mechanics.insert_text(string[0], 'Fonts/Kozhevnikov.ttf', GOLD,
                                                   (screen_size[0] // 2, (4 + count) * screen_size[1] // 13),
                                                   min(screen_size[1] // 12, screen_size[0] // 12))

    def user_events(self, events):
        '''
        Analyzes user's actions such as clicking, if the click was on variant of answer make a veto on choosing another variant
        Don't count the click on the other field like the question table
        '''
        for event in events:
            self.done = Modules.game_mechanics.quit_condition(event.type)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    self.coord = pygame.mouse.get_pos()
                    if self.in_ellipse((screen_size[0] // 12, 5 * screen_size[1] // 7, screen_size[0] // 3, screen_size[1] // 5)):
                        self.choice = 0
                    if self.in_ellipse((4 * screen_size[0] // 6, 4 * screen_size[1] // 6, screen_size[0] // 5, screen_size[1] // 5)):
                        self.choice = 1
                        self.score = 1

    def in_ellipse(self, parameters):
        '''
        Checks if the click was in ellipse with given parameters
        '''
        x = parameters[0] + parameters[2] // 2 - self.coord[0]
        y = parameters[3] // 2 + parameters [1] - self.coord[1]
        if (x * 2 // parameters[2]) ** 2 + (y * 2 // parameters[3]) ** 2 <= 1:
            self.time = self.time_limit - self.reading_time + 5
            return True
        else:
            return False

    def draw(self):
        '''
        Draws page with Laptop to chose button
        '''
        Modules.game_mechanics.insert_picture('images/Laptop.jpg', (screen_size[0] // 2, screen_size[1] // 2), screen_size)
        ellipse(screen, WHITE, (screen_size[0] // 12, 5 * screen_size[1] // 7, screen_size[0] // 3, screen_size[1] // 5))
        ellipse(screen, BLACK, (screen_size[0] // 12, 5 * screen_size[1] // 7, screen_size[0] // 3, screen_size[1] // 5), 7)
        ellipse(screen, WHITE, (4 * screen_size[0] // 6, 4 * screen_size[1] // 6, screen_size[0] // 5, screen_size[1] // 5))
        ellipse(screen, GREY, (4 * screen_size[0] // 6, 4 * screen_size[1] // 6, screen_size[0] // 5, screen_size[1] // 5), 7)
        Modules.game_mechanics.insert_text('Фильм ужасов', 'Fonts/Kozhevnikov.ttf', BLACK,
                                                   (screen_size[0] // 12 + screen_size[0] // 6, 5 * screen_size[1] // 7 + screen_size[1] // 10),
                                                   min(screen_size[1] // 12, screen_size[0] // 12))
        Modules.game_mechanics.insert_text('Лабка', 'Fonts/Kozhevnikov.ttf', BLACK,
                                                   (4 * screen_size[0] // 6 + screen_size[0] // 10, 4 * screen_size[1] // 6 + screen_size[1] // 10),
                                                   min(screen_size[1] // 12, screen_size[0] // 12))

if __name__ == "__main__":
    print("This module is not for direct call!")
