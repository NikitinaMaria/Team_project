from pygame.locals import *
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


class Pause():
    def __init__(self, pause):
        self.pause = False
        self.button_1 = pygame.Rect(50, 100, 200, 50)
        self.button_2 = pygame.Rect(50, 200, 200, 50)
        self.button_3 = pygame.Rect(50, 300, 200, 50)
        self.main = True
        self.options = False

    def render(self):
        screen.fill(BLACK)

        if self.main:
            draw_text('Pause menu', font, WHITE, screen, 20, 20)

            self.button_1 = pygame.Rect(50, 100, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_1)
            draw_text('Continue', font, BLACK, screen, 50, 100)

            self.button_2 = pygame.Rect(50, 200, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_2)
            draw_text('Options', font, BLACK, screen, 50, 200)

            self.button_3 = pygame.Rect(50, 300, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_3)
            draw_text('Quit', font, BLACK, screen, 50, 300)

        if self.options:
            draw_text('Options', font, WHITE, screen, 20, 20)

            self.button_1 = pygame.Rect(50, 100, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_1)
            draw_text('Option #1', font, BLACK, screen, 50, 100)

            self.button_2 = pygame.Rect(50, 200, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_2)
            draw_text('Option #2', font, BLACK, screen, 50, 200)

            self.button_3 = pygame.Rect(50, 300, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_3)
            draw_text('Back', font, BLACK, screen, 50, 300)

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

class Title():
    def __init__(self, title):
        self.title = True
        self.button_1 = pygame.Rect(50, 100, 200, 50)
        self.button_2 = pygame.Rect(50, 200, 200, 50)
        self.button_3 = pygame.Rect(50, 300, 200, 50)
        self.main = True
        self.options = False

    def render(self):
        screen.fill(BLACK)

        if self.main:
            draw_text('Main menu', font, WHITE, screen, 20, 20)

            self.button_1 = pygame.Rect(50, 100, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_1)
            draw_text('Start!', font, BLACK, screen, 50, 100)

            self.button_2 = pygame.Rect(50, 200, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_2)
            draw_text('Options', font, BLACK, screen, 50, 200)

            self.button_3 = pygame.Rect(50, 300, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_3)
            draw_text('Quit', font, BLACK, screen, 50, 300)

        if self.options:
            draw_text('Options', font, WHITE, screen, 20, 20)

            self.button_1 = pygame.Rect(50, 100, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_1)
            draw_text('Option #1', font, BLACK, screen, 50, 100)

            self.button_2 = pygame.Rect(50, 200, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_2)
            draw_text('Option #2', font, BLACK, screen, 50, 200)

            self.button_3 = pygame.Rect(50, 300, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), self.button_3)
            draw_text('Back', font, BLACK, screen, 50, 300)

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
