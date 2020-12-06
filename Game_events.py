from random import randint
import numpy as np
import pygame
import game_mechanics
from pygame.draw import *
from game_mechanics import *

GOLD = (238, 201, 0)
BLACKBOARD = (65, 86, 71)
BLACKBOARD_3 = (81, 78, 36)

class Stream:
    def __init__(self):
        self.side = randint(1, 2)
        if self.side == 1:
            self.coord_x = randint(0, 150)
        else:
            self.coord_x = randint(screen_size_x - 250, screen_size_x - 130)
        self.coord_y = randint(150, 400)
        self.click_time = 100
        self.width = 120
        self.length = 130
        self.youtube = pygame.image.load('images/youtube.png')
        self.background = pygame.image.load('images/background.jpg')
        self.background_3 = pygame.image.load('images/background_3.png')
        self.background_4 = pygame.image.load('images/background_4.png')
        self.scale = pygame.transform.scale(self.youtube, (self.length, self.width))
        self.stream_is_available = False
        self.stream_is_on = False
        self.done = 0
        self.step = 1

    def draw_button(self):
        if self.stream_is_available:
            self.click_time -= 1
            self.scale = pygame.transform.scale(self.youtube, (self.length, self.width))
            screen.blit(self.scale, (self.coord_x, self.coord_y))
            if self.click_time <= 0:
                self.stream_is_available = False

    def button_check(self, events):
        for event in events:
            if self.stream_is_available and (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = event.pos
                if (mouse_x > self.coord_x) and (mouse_x < self.coord_x + self.length) and (mouse_y > self.coord_y) and \
                        (mouse_y < self.coord_y + self.width):
                    self.click_time = 0
                    self.stream_is_on = True

    def draw(self):
        if self.step == 1:
            self.scale = pygame.transform.scale(self.background, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD, (screen_size_x // 6, screen_size_y // 12, 10 * screen_size_x // 27, 4 * screen_size_y // 5 + 10))
            draw_text('Хотите задать вопрос?', screen_size_x // 3 + 25, screen_size_y // 5, WHITE, 28)
            rect(screen, WHITE, (screen_size_x // 6 + 10, 4 * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('Хочу!', screen_size_x // 3 + 25, 4 * screen_size_y // 9 + 35, WHITE, 28)
            rect(screen, WHITE, (screen_size_x // 6 + 10, 6 * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('Пожалуй, нет...', screen_size_x // 3 + 25, 6 * screen_size_y // 9 + 35, WHITE, 28)

        if self.step == 2:
            self.scale = pygame.transform.scale(self.background, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD,
                 (screen_size_x // 6, screen_size_y // 12, 10 * screen_size_x // 27, 4 * screen_size_y // 5 + 10))
            draw_text('Хорошо.', screen_size_x // 3 + 25, screen_size_y // 7, WHITE, 28)
            draw_text('Давайте ваш вопрос.', screen_size_x // 3 + 25, screen_size_y // 7 + 30, WHITE, 28)
            for i in range(6):
                rect(screen, WHITE,
                     (screen_size_x // 6 + 10, (i+2) * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('Механика', screen_size_x // 3 + 25, 2 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Термодинамика', screen_size_x // 3 + 25, 3 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Электричество', screen_size_x // 3 + 25, 4 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Магнетизм', screen_size_x // 3 + 25, 5 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Оптика', screen_size_x // 3 + 25, 6 * screen_size_y // 9 + 35, WHITE, 28)
            draw_text('Квантовая физика', screen_size_x // 3 + 25, 7 * screen_size_y // 9 + 35, WHITE, 28)

        if self.step == 3:
            self.scale = pygame.transform.scale(self.background_3, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD_3,
                 (20, screen_size_y // 12, 4 * screen_size_x // 9 - 50, 3 * screen_size_y // 5))
            draw_text('Что ж...', screen_size_x // 5 + 10, screen_size_y // 7, WHITE, 28)
            draw_text('Давайте обсудим', screen_size_x // 5 + 10, screen_size_y // 7 + 30, WHITE, 28)
            draw_text('эту тему...', screen_size_x // 5 + 10, screen_size_y // 7 + 60, WHITE, 28)
            draw_text('(Поздравляем! Вы не', screen_size_x // 5 + 10, screen_size_y // 3, WHITE, 28)
            draw_text('потратили время впустую', screen_size_x // 5 + 10, screen_size_y // 3 + 30, WHITE, 28)
            draw_text('и заработали баллы!)', screen_size_x // 5 + 10, screen_size_y // 3 + 60, WHITE, 28)
            rect(screen, WHITE, (30, screen_size_y // 2, 30 + 4 * screen_size_x // 9 - 100, 70), 3)
            draw_text('Спасибо!', screen_size_x // 5 + 10, screen_size_y // 2 + 35, WHITE, 28)

        if self.step == 4:
            self.scale = pygame.transform.scale(self.background_4, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            ellipse(screen, BLACK, (0, screen_size_y // 5, 402, 202), 3)
            ellipse(screen, WHITE, (0, screen_size_y // 5, 400, 200))
            draw_text('Как же так...', screen_size_x // 5, screen_size_y // 3, BLACK, 30)
            draw_text('Вы должны это знать!', screen_size_x // 5, screen_size_y // 3 + 35, BLACK, 30)
            rect(screen, WHITE, (2 * screen_size_x // 3 - 40, screen_size_y // 9, 350, 270))
            rect(screen, BLACK, (2 * screen_size_x // 3 - 40, screen_size_y // 9, 350, 270), 3)
            draw_text('(Поздравляем! Вы', 4 * screen_size_x // 5, screen_size_y // 9 + 40, BLACK, 24)
            draw_text('потратили время впустую', 4 * screen_size_x // 5, screen_size_y // 9 + 70, BLACK, 24)
            draw_text('и ничего не заработали.)', 4 * screen_size_x // 5, screen_size_y // 9 + 100, BLACK, 24)
            rect(screen, BLACK, (2 * screen_size_x // 3 - 30, screen_size_y // 9 + 170, 330, 70), 3)
            draw_text('Вернуться к игре', 4 * screen_size_x // 5, screen_size_y // 9 + 205, BLACK, 24)

        if self.step == 5:
            self.scale = pygame.transform.scale(self.background, (screen_size_x, screen_size_y))
            screen.blit(self.scale, (0, 0))
            rect(screen, BLACKBOARD,
                 (screen_size_x // 6, screen_size_y // 12, 10 * screen_size_x // 27, 4 * screen_size_y // 5 + 10))
            draw_text('Ну тогда до свидания.', screen_size_x // 3 + 25, screen_size_y // 5, WHITE, 28)
            rect(screen, WHITE, (screen_size_x // 6 + 10, 4 * screen_size_y // 9, 10 * screen_size_x // 27 - 20, 70), 3)
            draw_text('До свидания.', screen_size_x // 3 + 25, 4 * screen_size_y // 9 + 35, WHITE, 28)


    def answer(self, events):
        for event in events:
            self.done = game_mechanics.quit_condition(event.type)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (self.step == 1) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) and \
                        (mouse_y > 4 * screen_size_y // 9) and (mouse_y < 4 * screen_size_y // 9 + 70):
                    self.step = 2
                elif (self.step == 1) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20)\
                        and (mouse_y > 6 * screen_size_y // 9) and (mouse_y < 6 * screen_size_y // 9 + 70):
                    self.step = 5
                elif (self.step == 2) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) \
                        and (mouse_y > 2 * screen_size_y // 9) and (mouse_y < 8 * screen_size_y // 9 + 70):
                    self.step = randint(3, 4)
                elif (self.step == 3) and (mouse_x > 30) and (mouse_x < 4 * screen_size_x // 9 - 40) and \
                        (mouse_y > screen_size_y // 2) and (mouse_y < screen_size_y // 2 + 70):
                    self.stream_is_on = False
                elif (self.step == 4) and (mouse_x > 2 * screen_size_x // 3 - 30) + (mouse_x < 2 * screen_size_x // 3 + 300)\
                        and (mouse_y > screen_size_y // 9 + 170) and (mouse_y < screen_size_y // 9 + 240):
                    self.stream_is_on = False
                elif (self.step == 5) and (mouse_x > screen_size_x // 6 + 10) and \
                        (mouse_x < screen_size_x // 6 + 10 + 10 * screen_size_x // 27 - 20) and \
                        (mouse_y > 4 * screen_size_y // 9) and (mouse_y < 4 * screen_size_y // 9 + 70):
                    self.stream_is_on = False


class Ivanov_test():
    def __init__(self):
        '''
        Set test's parameters and thier meanings
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
        return (self.done, not self.time_is_over)

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
            game_mechanics.insert_text("Dancing time!", "Game-font.ttf", GREEN, (screen_size[0] // 2, screen_size[1] // 2),
                        self.time * self.time)
        else:
            if self.number_of_task <= 4 and self.time <= self.time_limit:
                self.draw_task()
                for i in range(4):
                    game_mechanics.insert_text(str(i + 1) + ') ', "Game-font.ttf", BLACK,
                                (screen_size[0] // 12, i * self.length_of_answer_pic + screen_size[1] // 5), 20)
                rect(screen, BLACK, (screen_size[0] // 2 - 5 * self.length_of_asterisk //2 - 3, 2 * screen_size[1] // 5 - self.length_of_asterisk // 2,
                               5 * self.length_of_asterisk + 6, self.length_of_asterisk + 6), 3)
            if (self.number_of_task >= 5) or (self.time >= self.time_limit):
                screen.fill(GREY)
                if self.score == 0:
                    self.draw_zero_score()
                if self.score == 4:
                    self.draw_max_score()
                if self.score == 1 or self.score == 2:
                    game_mechanics.insert_text('Not so bad', 'Game-font.ttf', BLACK,
                    (screen_size[0] // 2, 3 * screen_size[1] // 4),
                    min(screen_size[0] // 9, screen_size[1] // 9))
                if self.score == 3:
                    game_mechanics.insert_text('Just great!', 'Game-font.ttf', GREEN,
                    (screen_size[0] // 2, 3 * screen_size[1] // 4),
                    min(screen_size[0] // 9, screen_size[1] // 8))
                for i in range(4):
                    game_mechanics.insert_text(str(i + 1) + ') ', "Game-font.ttf", WHITE,
                                (screen_size[0] // 12, i * self.length_of_answer_pic + screen_size[1] // 5), 20)
            self.draw_right_or_wrong_answer()
        pygame.display.update()

    def draw_zero_score(self):
        '''
        Puts falure picture on the screen
        '''
        game_mechanics.insert_picture('images/Falure.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                      (screen_size[0], screen_size[1]))
        game_mechanics.insert_text('You need to work harder', 'Game-font.ttf', WHITE,
                    (screen_size[0] // 2, 3 * screen_size[1] // 4),
                    min(screen_size[0] // 9, screen_size[1] // 9))

    def draw_max_score(self):
        '''
        Puts happy Ivanov's picture on the screen
        '''
        game_mechanics.insert_picture('images/Happy_master.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                      (screen_size[0], screen_size[1]))
        game_mechanics.insert_text('Master is proud of you', 'Game-font.ttf', GOLD,
                    (screen_size[0] // 2, 2 * screen_size[1] // 3),
                    min(screen_size[0] // 9, screen_size[1] // 9))

    def draw_right_or_wrong_answer(self):
        '''
        Putting pictures of green arrow for right answer or red X for wrong answer
        '''
        if self.time <= self.time_limit:
            for i in range(self.numerous - 1):
                game_mechanics.insert_picture('images/asterisk.png', (
                                             screen_size[0] // 2 - 4 * self.length_of_asterisk // 2 + i * self.length_of_asterisk, 2 * screen_size[1] // 5),
                                             (self.length_of_asterisk, self.length_of_asterisk))
        for i in range(self.number_of_task - 1):
            if self.answer_list[i] == True:
                game_mechanics.insert_picture('images/right_ans.png', (
                screen_size[0] // 12 + self.length_of_answer_pic, i * self.length_of_answer_pic + screen_size[1] // 5),
                               (self.length_of_answer_pic, self.length_of_answer_pic))
            else:
                game_mechanics.insert_picture('images/wrong.jpg', (
                screen_size[0] // 12 + self.length_of_answer_pic, i * self.length_of_answer_pic + screen_size[1] // 5),
                               (self.length_of_answer_pic, self.length_of_answer_pic))

    def user_events(self, events):
        '''
        Analize events from keyboard, mouse, etc.
        '''
        for event in events:
            self.done = game_mechanics.quit_condition(event.type)
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
        rect(screen, BLACK, (self.x - self.length // 2 - 10, self.y - self.length // 2 - 10, self.length + 20, self.length + 20), 5)
        self.number = self.task[len(self.task) - 1]
        if self.number == 1:
            self.draw_for_all()
        elif self.number == 2:
            self.draw_exist()
        elif self.number == 3:
            self.draw_equivalent()
        else:
            self.draw_epsilon()
        game_mechanics.insert_picture('images/Hint.png', (4 * screen_size[0] // 5, screen_size[1] // 3),
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
        game_mechanics.insert_picture('images/epsilon.jpg', (self.x, self.y), (self.length, self.length))

#sets the logo an backstage music, but not activates it        
sound1 = pygame.mixer.Sound('audio/Hello_sound.ogg')
pygame.mixer.music.load('audio/backstage.ogg')

class Kozhevnikov_test():
    def __init__(self):
        '''
        Set test's parameters and thier meanings
        '''
        self.time = 0
        self.length = min(screen_size[0] // 7, screen_size[1] // 7)
        self.done = 0
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
                sound1.play()
            if self.time == self.growing_time + 1:
                pygame.mixer.music.play()
            if self.time <= self.growing_time:
                self.draw_logo()
            else:
                self.draw()
            self.user_events(events)
            if self.time >= self.time_start + self.answer_music_time and self.time <= self.time_start + self.answer_music_time + self.time_picture:
                if self.answer_is_set == True and self.number_of_answer == self.number_of_question:
                    self.draw_Kozhevnikov('images/Happy_Kozhevnikov.jpg', 'audio/correct.ogg', 'Right answer!',GREEN)
                    if self.time == self.time_start + self.answer_music_time:  
                        self.score += 1
                else:
                    self.draw_Kozhevnikov('images/Sad_Kozhevnikov.png', 'audio/wrong.ogg', 'Wrong answer!', RED)       
        self.time += 1
        return (self.done, not self.time_is_over)

    def create_task(self):
        '''
        Reads task from text file, puts it in list according to the number of question
        '''
        with open('text.txt', encoding='utf-8') as file:
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
        game_mechanics.insert_picture(name, (screen_size[0] // 2, screen_size[1] // 2), screen_size)
        game_mechanics.insert_text(text, 'Game-font.ttf', color, (screen_size[0] // 2, 7 * screen_size[1] // 8), min(screen_size[0] // 8, screen_size[1] // 8))
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
            self.done = game_mechanics.quit_condition(event.type)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    self.coord = pygame.mouse.get_pos()
                    if not self.in_rectangle((0, 0), 39 * screen_size[1] // 80):
                        for i in range(4):
                            if self.in_rectangle((0, (39 + 10 * i) * screen_size[1] // 80), 10 * screen_size[1] // 80) and self.answer_is_set == False:
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
        game_mechanics.insert_picture('images/quiz.jpg', (screen_size[0] // 2, screen_size[1] // 2), screen_size)

    def draw(self):
        '''
        Draws answer sheet table, make chosen answer colorized orange
        '''
        screen.fill(WHITE)
        game_mechanics.insert_picture('images/Answer_sheet' + str(self.number_of_answer) + '.png', (screen_size[0] // 2, screen_size[1] // 2), screen_size)
        game_mechanics.insert_text('Вопрос '+ str(self.number_of_task), 'Kozhevnikov.ttf', WHITE, (5 * min(screen_size[1] // 20, screen_size[0] // 20), 
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
                game_mechanics.insert_text(string, 'Kozhevnikov.ttf', WHITE, (screen_size[0] // 2, (4 + count) * screen_size[1] // 20),
                                          min(screen_size[1] // 15, screen_size[0] // 15))
            elif count >= 0 and string != 'r\n':
                game_mechanics.insert_text(string[0: len(string) - 3], 'Kozhevnikov.ttf', WHITE, (35 * int(string[len(string) - 3:len(string) - 1]) / 100 * min(screen_size[1] // 25, screen_size[0] // 25), 
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
            game_mechanics.insert_text('Not so bad', 'Game-font.ttf', BLACK,
                                      (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                       min(screen_size[0] // 9, screen_size[1] // 9))
            game_mechanics.insert_text(str(self.score), 'Game-font.ttf', BLACK,
                                      (screen_size[0] // 2, screen_size[1] // 2),
                                       min(screen_size[0] // 5, screen_size[1] // 5))
        if self.score == 4:
            game_mechanics.insert_text('Just great!', 'Game-font.ttf', GREEN,
                                      (screen_size[0] // 2, 3 * screen_size[1] // 4),
                                       min(screen_size[0] // 5, screen_size[1] // 5))
            game_mechanics.insert_text(str(self.score), 'Game-font.ttf', GREEN,
                                      (screen_size[0] // 2, screen_size[1] // 2),
                                       min(screen_size[0] // 5, screen_size[1] // 5))
        pygame.display.update()

    def draw_zero_score(self):
        '''
        Puts sad falure picture on the screen
        '''
        game_mechanics.insert_picture('images/Falure.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                      (screen_size[0], screen_size[1]))
        game_mechanics.insert_text('You need to work harder', 'Game-font.ttf', WHITE,
                    (screen_size[0] // 2, 3 * screen_size[1] // 4),
                    min(screen_size[0] // 9, screen_size[1] // 9))

    def draw_max_score(self):
        '''
        Draws Kozhevnikov in role of the master of the world picture with words on it
        '''
        game_mechanics.insert_picture('images/Master_of_the_world.jpg', (screen_size[0] // 2, screen_size[1] // 2),
                      (screen_size[0], screen_size[1]))
        game_mechanics.insert_text('Master is proud of you', 'Game-font.ttf', GOLD,
                    (screen_size[0] // 2, 2 * screen_size[1] // 3),
                    min(screen_size[0] // 9, screen_size[1] // 9))        

if __name__ == "__main__":
    print("This module is not for direct call!")
