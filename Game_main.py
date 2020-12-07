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

explanatories = []
for i in range(3):
    explanatories.append(Explanatory(i + 1))

gender = 1
edit_events = Editor(gender, 250, 6)
pause_menu = Pause(False, screen_size_x, screen_size_y)
main_menu = Title(True, screen_size_x, screen_size_y)
choose = Choosing()

clock = pygame.time.Clock()
done = False
finished_game = False
# pygame.mixer.music.load('Ramones_Rock_N_Roll_High_School_1.ogg')
# pygame.mixer.music.play()

while not done:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)

    keys = pygame.key.get_pressed()

    if choose.main == True:
        choose.render()
        choose.check(pygame.event.get())
        edit_events.gender = choose.gender
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
                print(edit_events.gender)

if done == 2:
    show_game_over_table(done)

print(edit_events.gender)
pygame.quit()
