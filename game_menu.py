from pygame.locals import *
from game_hero import Hero
import pygame, sys

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Da life at MIPT')
screen = pygame.display.set_mode((500, 500),0 ,32)

font = pygame.font.SysFont(None, 20)

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

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
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

'''
pos - Position - (x, y)
size - Size - (length, width)

Draws button and text on it with same size
'''
def make_button(text, pos, size, color):
    button = pygame.Rect(pos[0], pos[1], size[0], size[1])
    pygame.draw.rect(screen, color, button)
    draw_text(text, font, BLACK, screen, pos[0], pos[1])
    return(button)

'''
Pause menu class
'''
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
            draw_text('Pause menu', font, WHITE, screen, 20, 20)

            self.button_1 = make_button('Continue', (self.button_size_y, self.button_size_x // 2 ), (self.button_size_x, self.button_size_y), RED)

            self.button_2 = make_button('Options', (self.button_size_y, self.button_size_x ), (self.button_size_x, self.button_size_y), RED)

            self.button_3 = make_button('Quit', (self.button_size_y, (3*self.button_size_x // 2) ), (self.button_size_x, self.button_size_y), RED)

        if self.options:
            '''
            Draws buttons in options branch of pause menu
            '''
            draw_text('Options', font, WHITE, screen, 20, 20)

            self.button_1 = make_button('Option #1', (self.button_size_y, self.button_size_x // 2 ), (self.button_size_x, self.button_size_y), RED)

            self.button_2 = make_button('Option #2', (self.button_size_y, self.button_size_x ), (self.button_size_x, self.button_size_y), RED)

            self.button_3 = make_button('Back', (self.button_size_y, (3*self.button_size_x // 2)), (self.button_size_x, self.button_size_y), RED)

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
                        #print("what")

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

    def render(self):
        screen.fill(BLACK)

        if self.main:
            '''
            Draws buttons in main branch of main menu
            '''
            draw_text('Main menu', font, WHITE, screen, 20, 20)

            self.button_1 = make_button('Start !', (self.button_size_y, self.button_size_x // 2 ), (self.button_size_x, self.button_size_y), RED)

            self.button_2 = make_button('Options', (self.button_size_y, self.button_size_x ), (self.button_size_x, self.button_size_y), RED)

            self.button_3 = make_button('Quit', (self.button_size_y, (3*self.button_size_x // 2) ), (self.button_size_x, self.button_size_y), RED)

        if self.options:
            '''
            Draws buttons in options branch of main menu
            '''
            draw_text('Options', font, WHITE, screen, 20, 20)

            self.button_1 = make_button('Option #1', (self.button_size_y, self.button_size_x // 2 ), (self.button_size_x, self.button_size_y), RED)

            self.button_2 = make_button('Option #2', (self.button_size_y, self.button_size_x ), (self.button_size_x, self.button_size_y), RED)

            self.button_3 = make_button('Back', (self.button_size_y, (3*self.button_size_x // 2) ), (self.button_size_x, self.button_size_y), RED)

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
                    pass

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pass

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

    def render(self):
        screen.fill(BLACK)
        preview(1, 100, 100)
        preview(0, 800, 100)
        draw_text('Welcome to the MIPT, buddy', font, WHITE, screen, 400, 50)
        draw_text('Choose your warrior', font, WHITE, screen, 400, 100)
        self.button_1 = pygame.Rect(100, 100, self.button_size_x, self.button_size_y)
        self.button_2 = pygame.Rect(800, 100, self.button_size_x, self.button_size_y)
        self.button_3 = make_button('Oh no, pls let me go ;C', (400, 500), (150, 50), BLUE)

    def check(self, events):
        mouse_x, mouse_y = pygame.mouse.get_pos(events)
        for event in events:

            if self.main:
                if self.button_1.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.main = False
                    self.gender = 1

                if self.button_2.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    self.main = False
                    self.gender = 0

                if self.button_3.collidepoint((mouse_x, mouse_y)) and (event.type == MOUSEBUTTONDOWN) and (event.button == 1):
                    pygame.quit()
                    sys.exit()

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


