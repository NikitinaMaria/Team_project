import pygame
from game_stats import *
from game_mechanics import *
from game_menu import *

pygame.init()

screen_size_x = 1000
screen_size_y = 600
FPS = 15

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
screen.fill(WHITE)

pause_menu = Pause(False, screen_size_x, screen_size_y)
main_menu = Title(True, screen_size_x, screen_size_y)
choose = Choosing()

clock = pygame.time.Clock()
done = False
finished_game = False

while not done:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)

    keys = pygame.key.get_pressed()

    if choose.main == True:
        choose.render()
        choose.check(pygame.event.get())
        edit_events = Editor(choose.gender, 250, 6)
    else:
        if main_menu.title == True:
            main_menu.render()
            main_menu.check(pygame.event.get())
        else:

            if keys[pygame.K_ESCAPE] and (pause_menu.pause == False):
                pause_menu.pause = True
            if pause_menu.pause:
                pause_menu.render()
                pause_menu.check(pygame.event.get())

            else:
                done = edit_events.process(pygame.event.get())

if (done != 0) and (done != 1):
    endings = Endings(done, edit_events.stats.points.points)
    endings.end()

pygame.quit()