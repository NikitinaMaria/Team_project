import pygame
from game_stats import *
from game_mechanics import *

pygame.init()

screen_size_x = 1000
screen_size_y = 600
FPS = 15

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
screen.fill(WHITE)

draw_stats = Draw_stats()

edit_events = Editor(250, 6)

clock = pygame.time.Clock()
done_mechanics = False
done_stats = False
# pygame.mixer.music.load('Ramones_Rock_N_Roll_High_School_1.ogg')
# pygame.mixer.music.play()

while (not done_mechanics) and (not done_stats):
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)
    done_mechanics = edit_events.process(pygame.event.get())
    done_stats = draw_stats.draw()
    if edit_events.hero_boosting():
        draw_stats.boost_scale.boost_points = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done_mechanics = True

if done_mechanics == 2:
    show_game_over_table(done_mechanics)

pygame.quit()
