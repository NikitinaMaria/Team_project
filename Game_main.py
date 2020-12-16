import pygame
import Modules.game_stats
from Modules.game_stats import *
from Modules.game_mechanics import *
from Modules.game_menu import *
from Modules.game_leaderboards import *

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

edit_events = Editor(None, 250, 6)
#edit_events.time = 15*FPS-1

clock = pygame.time.Clock()
done = False
done_1 = False
finished_game = False
name = ''

choose.main = False
main_menu.title = False

while not done_1:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)

    keys = pygame.key.get_pressed()

    if choose.main == True:
        choose.render()
        name = choose.check(pygame.event.get())
    else:
        if name == '':
            name = 'Anonymous'
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
                edit_events.hero.gender = choose.gender
                done = edit_events.process(pygame.event.get())
                if edit_events.time == 15*FPS:
                    choose.main = True
                    main_menu.title = True

    if (done != 0) and (done != 1):
        endings = Endings(done, edit_events.stats.points.points)
        endings.end()
        save_score(str(name) + endings.score)

'''
        if endings.done == 1:
            main_menu.title = True
            edit_events = Editor(choose.gender, 250, 6)
'''
pygame.quit()
