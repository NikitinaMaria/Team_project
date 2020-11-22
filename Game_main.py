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

explanatories = []
for i in range(3):
    explanatories.append(Explanatory(i+1))

mood_scale = Mood_scale()

boost_scale = Boost_scale()

timer = Timer()

edit_events = Editor(250, 6)

clock = pygame.time.Clock()
done = False
finished_game = False
# pygame.mixer.music.load('Ramones_Rock_N_Roll_High_School_1.ogg')
# pygame.mixer.music.play()

while not done:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)
    done = edit_events.process(pygame.event.get())
    if edit_events.hero_boosting():
        boost_scale.boost_points = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            finished_game = True
    mood_scale.draw()
    boost_scale.draw()
    timer.draw()
    if mood_scale.mood_points <= 0:
        done = True

if done == 2:
    show_game_over_table(done)

pygame.quit()
