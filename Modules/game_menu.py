from pygame.locals import *
from Modules.game_hero import Hero
import pygame, sys
import Modules.game_mechanics
from Modules.game_mechanics import *

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Сессия близко')
screen = pygame.display.set_mode((500, 500),0 ,32)

font = pygame.font.SysFont(None, 20)
font_in = pygame.font.SysFont(None, 40)

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
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
BLACKBOARD = (65, 86, 71)
BLACKBOARD_3 = (81, 78, 36)
BlOOD = (153, 0, 0)

def draw_text1(text, font_type, color, surface, x, y, font_size):
    font_type = pygame.font.Font(None, font_size)

    textobj = font_type.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

'''
Draws characters at (x,y) coordinates
'''
def preview(gender, x, y):
    hero = Hero(0, (x, y))
    hero.size_x = 600
    hero.size_y = 800
    if gender == 1:
        hero.gender = 1
        hero.direction = 0
        hero.draw()
    else:
        hero.gender = 0
        hero.direction = 0
        hero.draw()

def active(marker, gender):
    if marker == gender:
        return(COLOR_ACTIVE)
    else:
        return(COLOR_INACTIVE)

'''
pos - Position - (x, y)
size - Size - (length, width)

Draws button and text on it with same size
'''
def make_button(text, pos, size, color, font_size):
    button = pygame.Rect(pos[0], pos[1], size[0], size[1])
    pygame.draw.rect(screen, color, button)
    draw_text1(text, font, BLACK, screen, pos[0], pos[1], font_size)
    return(button)

'''
Pause menu class
'''
class InputBox():

    def __init__(self, x, y, w, h, text=''):
        self.box = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font_in.render(text, True, self.color)
        self.active = False

    def check(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.box.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font_in.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.box.w = width

    def render(self):
        screen.blit(self.txt_surface, (self.box.x+5, self.box.y+5))
        pygame.draw.rect(screen, self.color, self.box, 4)



class Pause():
    def __init__(self, pause, screen_size_x, screen_size_y):
        self.pause = False
        self.main = True
        self.options = False
        self.button_size_x = screen_size_x // 5
        self.button_size_y = screen_size_y // 10

    def render(self):
        screen.fill(BLACK)
        if self.main:
            '''
            Draws buttons in main branch of pause menu
            '''
            screen.fill((50, 50, 50))
            self.title_rect = pygame.Rect(40, 20, screen_size[0] - 80, 100)
            pygame.draw.rect(screen, (200, 200, 200), self.title_rect)
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (100, 70), (110, 110))
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (1000 - 100, 70), (110, 110))
            Modules.game_mechanics.insert_text('Сессия близко', 'Fonts/Session.otf', BlOOD, (500, 70), 120)

            draw_text1('Pause menu', font, WHITE, screen, 50, 150, 35)

            self.button_1 = make_button('Continue', (70, 250), (200, 70), BlOOD, 35)

            self.button_2 = make_button('Options', (70, 350), (200, 70), BlOOD, 35)

            self.button_3 = make_button('Quit',  (70, 450), (200, 70), BlOOD, 35)
        if self.options:
            '''
            Draws buttons in options branch of pause menu
            '''
            screen.fill((50, 50, 50))
            self.title_rect = pygame.Rect(40, 20, screen_size[0] - 80, 100)
            pygame.draw.rect(screen, (200, 200, 200), self.title_rect)
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (100, 70), (110, 110))
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (1000 - 100, 70), (110, 110))
            Modules.game_mechanics.insert_text('Сессия близко', 'Fonts/Session.otf', BlOOD, (500, 70), 120)

            draw_text1('Empty for now', font, WHITE, screen, 50, 150, 35)

            self.button_1 = make_button('Something #1', (70, 250), (200, 70), BlOOD, 35)

            self.button_2 = make_button('Something #2', (70, 350), (200, 70), BlOOD, 35)

            self.button_3 = make_button('Back',  (70, 450), (200, 70), BlOOD, 35)

    '''
    Checks if mouseclick was on button in two branches of pause menu
    '''
    def check(self, events):
        mouse_x, mouse_y = pygame.mouse.get_pos(events)
        for event in events:

            if self.main:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.pause = False

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.options = True
                    self.main = False

                if self.button_3.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pause = False
                        #print("what")

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if self.options:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pass

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pass

                if self.button_3.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.options = False
                    self.main = True

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pause = False

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
'''
Main menu class
'''
class Title():
    def __init__(self, title, screen_size_x, screen_size_y):
        self.title = True
        self.main = True
        self.options = False
        self.button_size_x = screen_size_x // 5
        self.button_size_y = screen_size_y // 10
        self.music_on = False
        self.phase = -1

    def render(self):

        if self.main:
            '''
            Draws buttons in main branch of main menu
            '''
            screen.fill((50, 50, 50))
            self.title_rect = pygame.Rect(40, 20, screen_size[0] - 80, 100)
            pygame.draw.rect(screen, (200, 200, 200), self.title_rect)
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (100, 70), (110, 110))
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (1000 - 100, 70), (110, 110))
            Modules.game_mechanics.insert_text('Сессия близко', 'Fonts/Session.otf', BlOOD, (500, 70), 120)

            draw_text1('Main menu', font, WHITE, screen, 50, 150, 35)

            self.button_1 = make_button('Start !', (70, 250), (200, 70), BlOOD, 35)

            self.button_2 = make_button('Options', (70, 350), (200, 70), BlOOD, 35)

            self.button_3 = make_button('Quit', (70, 450), (200, 70), BlOOD, 35)

        if self.options:
            '''
            Draws buttons in options branch of main menu
            '''
            screen.fill((50, 50, 50))
            self.title_rect = pygame.Rect(40, 20, screen_size[0] - 80, 100)
            pygame.draw.rect(screen, (200, 200, 200), self.title_rect)
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (100, 70), (110, 110))
            Modules.game_mechanics.insert_picture('images/fopf_black.png', (1000 - 100, 70), (110, 110))
            Modules.game_mechanics.insert_text('Сессия близко', 'Fonts/Session.otf', BlOOD, (500, 70), 120)

            draw_text1('Options', font, WHITE, screen, 50, 150, 35)

            if self.music_on == True:
                self.button_1 = make_button('Music on', (70, 250), (200, 70), BlOOD, 35)
            else:
                self.button_1 = make_button('Music off', (70, 250), (200, 70), BlOOD, 35)

            if self.phase == 0:
                self.button_2 = make_button('Just a button for fun :)', (70, 350), (300, 70), BlOOD, 35)
            elif self.phase == 1:
                self.button_2 = make_button('It doesnt do anything :)', (70, 350), (300, 70), BlOOD, 35)
            elif self.phase == 2:
                self.button_2 = make_button('See? Nothing changed', (70, 350), (300, 70), BlOOD, 35)
            elif self.phase == 3:
                self.button_2 = make_button('Yea, keep pressing it', (70, 350), (300, 70), BlOOD, 35)
            elif self.phase == 4:
                self.button_2 = make_button('Ok im tired so will start over', (70, 350), (400, 70), BlOOD, 35)

            self.button_3 = make_button('Back', (70, 450), (200, 70), BlOOD, 35)

    '''
    Checks if mouseclick was on button in two branches of pause menu
    '''
    def check(self, events):
        mouse_x, mouse_y = pygame.mouse.get_pos(events)
        for event in events:

            if self.main:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.title = False

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.options = True
                    self.main = False

                if self.button_3.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pygame.quit()
                    sys.exit()

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if self.options:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.music_on = not self.music_on

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    if self.phase < 4:
                        self.phase += 1
                    else:
                        self.phase = 0

                if self.button_3.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.options = False
                    self.main = True

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.pause = False
                        #print("what")

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
'''
Choosing of player model menu
'''
class Choosing:
    def __init__(self):
        self.main = True
        self.gender = 1
        self.button_size_x = 200
        self.button_size_y = 200
        self.input_box = InputBox(330, 200, 220, 40)

    def render(self):
        screen.fill((50, 50, 50))
        self.title_rect = pygame.Rect(40, 20, screen_size[0] - 80, 100)
        self.bg1 = pygame.Rect(610, 220 -50, 140, 190)
        self.bg2 = pygame.Rect(810, 220 -50, 140, 190)
        self.bg3 = pygame.Rect(605, 215 -50, 150, 200)
        self.bg4 = pygame.Rect(805, 215 -50, 150, 200)
        self.name_rect = pygame.Rect(30, 190, 550, 60)
        pygame.draw.rect(screen, (100, 100, 100), self.name_rect)
        pygame.draw.rect(screen, (200, 200, 200), self.title_rect)
        Modules.game_mechanics.insert_picture('images/fopf_black.png', (100, 70), (110, 110))
        Modules.game_mechanics.insert_picture('images/fopf_black.png', (1000 - 100, 70), (110, 110))

        Modules.game_mechanics.insert_text('Сессия близко', 'Fonts/Session.otf', BlOOD, (500, 70), 120)
        Modules.game_mechanics.insert_text('Введите Ваше имя:',None , COLOR_ACTIVE, (170, 220), 40)
        Modules.game_mechanics.insert_text('И выберите персонажа :)',None , COLOR_ACTIVE, (270, 320), 40)
        pygame.draw.rect(screen, (20, 20, 20), self.bg3)
        pygame.draw.rect(screen, (20, 20, 20), self.bg4)
        pygame.draw.rect(screen, active(1, self.gender), self.bg1)
        pygame.draw.rect(screen, active(0, self.gender), self.bg2)
        preview(1, 650, 300 -50)
        preview(0, 850, 300 -50)
        #draw_text1('Welcome to the MIPT, buddy', font, WHITE, screen, 400, 50)
        #draw_text1('Choose your warrior', font, WHITE, screen, 400, 100)
        self.button_1 = self.bg1
        self.button_2 = self.bg2

        self.start_rect = pygame.Rect(70, 450, 210, 70)
        pygame.draw.rect(screen, (80, 160, 100), self.start_rect)
        Modules.game_mechanics.insert_text('Продолжить',None , BLACK, (180, 480), 40)
        self.button_4 = self.start_rect

        self.exit_rect = pygame.Rect(820, 550, 170, 20)
        pygame.draw.rect(screen, BlOOD, self.exit_rect)
        Modules.game_mechanics.insert_text('Не, я лучше в бомонку...',None , BLACK, (910, 560), 20)
        self.button_3 = self.exit_rect

        self.input_box.update()
        self.input_box.render()

    def check(self, events):
        mouse_x, mouse_y = pygame.mouse.get_pos(events)
        for event in events:

            if self.main:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.gender = 1

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.gender = 0

                if self.button_3.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pygame.quit()
                    sys.exit()

                if self.button_4.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.main = False
                    return(self.input_box.text)

                self.input_box.check(event)

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

class Ending_menu():
    def __init__(self):
        self.main = True
        self.button_size_x = 200
        self.button_size_y = 200

    def render(self):
        self.button_1 = make_button('Try again!', (400, 500), (150, 50), RED, 35)

    def check(self, events):
        mouse_x, mouse_y = pygame.mouse.get_pos(events)
        for event in events:

            if self.main:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.main = False
                    return(1)

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
