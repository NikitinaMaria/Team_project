from random import randrange as rnd, choice
from random import randint
import numpy as np
import pygame
from pygame.draw import *
from game_hero import *
from game_stats import *
from Game_events import *

pygame.init()

screen_size_x = 1000
screen_size_y = 600
screen_size = (screen_size_x, screen_size_y)

screen = pygame.display.set_mode(screen_size)

# Colors
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


def insert_picture(name, position, size):
    '''
    Paste image according to its position and size which written like (full_size_x, full_size_y)
    '''
    surf = pygame.image.load(name)
    surf = pygame.transform.scale(surf, size)
    rect = surf.get_rect(center=position)
    screen.blit(surf, rect)


def insert_text(string, font, color, position, size):
    '''
    Paste text according to the position of its center
    '''
    text_style = pygame.font.Font(font, size)
    surface = text_style.render(string, True, color)
    textRect = surface.get_rect(center=position)
    screen.blit(surface, textRect)


def quit_condition(pressed_button):
    """
	Checks if [X] button was pressed
	"""
    final = 0
    if pressed_button == pygame.QUIT:
        final = 1
    return final


def draw_road(width_of_pictures, distance_between_roads):
    """"
    The function draws road
    """
    width_of_road = screen_size_x - 2 * width_of_pictures
    polygon(screen, GREY, ((width_of_pictures, screen_size_y),
                           (screen_size_x - width_of_pictures, screen_size_y),
                           ((screen_size_x - width_of_road // 2) // 2 + width_of_road // 2, 0),
                           ((screen_size_x - width_of_road // 2) // 2, 0)))

    line(screen, WHITE, (width_of_pictures + (width_of_road - 2 * distance_between_roads) // 3, screen_size_y),
         ((screen_size_x - width_of_road // 2) // 2 + (width_of_road // 2 - distance_between_roads) // 3, 0),
         distance_between_roads)
    line(screen, WHITE, (width_of_pictures + 2 * width_of_road // 3 + distance_between_roads, screen_size_y),
         (screen_size_x // 2 + (width_of_road - 2 * distance_between_roads) // 12, 0),
         distance_between_roads)


def show_game_over_table(done):
    '''
	Shows "Game over" table after the hero was smashed by obstacle
	'''
    screen.fill(GREEN)
    insert_text("Game Over", "Game-font.ttf", WHITE, (screen_size[0] // 2, screen_size[1] // 2), 100)
    pygame.display.update()
    while done != 1:
        for event in pygame.event.get():
            done = quit_condition(event.type)


class Obstacle:
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.type = randint(1, 2)
        if self.type == 1:
            self.bed = pygame.image.load('images/bed.png')
        else:
            self.bed = pygame.image.load('images/sofa.png')
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_all_road = screen_size_x - 2 * width_of_pictures
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.coord = [width_of_pictures + self.width_of_all_road // 4 + (number_of_road - 1) * (
                    self.width_of_road // 2 + self.distance_between_roads // 2), 0]
        self.length = self.width_of_road // 2
        self.width = width
        self.number_of_road = number_of_road
        if number_of_road == 2:
            self.lower_distance_from_center_x = self.width_of_road // 4
        elif number_of_road == 3:
            self.lower_distance_from_center_x = self.width_of_road // 4 + self.distance_between_roads
        else:
            self.lower_distance_from_center_x = self.width_of_road // 4 * 3 + self.distance_between_roads

    def motion(self):
        '''
		Move obstacles, look if they are done
		'''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] - self.width:
            self.is_alive = False
        self.length = self.width_of_road // 2 * (screen_size_y + self.coord[1]) // screen_size_y
        if self.number_of_road != 3:
            self.coord[0] = - self.coord[
                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 - self.lower_distance_from_center_x
        else:
            self.coord[0] = self.coord[
                                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 + self.lower_distance_from_center_x

    def draw(self):
        '''
		Draws obstacles. Attention: coords are the coordinates of the left top corner
		'''
        self.scale = pygame.transform.scale(self.bed, (self.length, self.width))
        screen.blit(self.scale, (self.coord[0], self.coord[1]))


class Boost:
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_all_road = screen_size_x - 2 * width_of_pictures
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.width_start = width // 2
        self.width = self.width_start
        self.length = 35
        self.number_of_road = number_of_road
        self.coord = [width_of_pictures + self.width_of_all_road // 4 + self.width_of_road // 4 - self.length // 2 +
                      (number_of_road - 1) * (self.width_of_road // 2 + self.distance_between_roads // 2), 0]
        self.redbull = pygame.image.load('images/RedBull.png')
        self.scale = pygame.transform.scale(self.redbull, (self.length, self.width))
        if number_of_road == 2:
            self.lower_distance_from_center_x = self.length // 4
        elif number_of_road == 1:
            self.lower_distance_from_center_x = self.width_of_road // 2 + self.length // 2 + self.distance_between_roads // 2
        else:
            self.lower_distance_from_center_x = self.width_of_road // 2 - self.length // 2 + self.distance_between_roads // 2

    def motion(self):
        '''
        Move obstacles, look if they are done
        '''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] + self.width:
            self.is_alive = False
        self.length = 35 * (screen_size_y + self.coord[1]) // screen_size_y
        self.width = self.width_start * (screen_size_y + self.coord[1]) // screen_size_y
        if self.number_of_road != 3:
            self.coord[0] = - self.coord[
                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 - self.lower_distance_from_center_x
        else:
            self.coord[0] = self.coord[
                                1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 + self.lower_distance_from_center_x

    def draw(self):
        '''
        Draws obstacles. Attention: coords are the coordinates of the left top corner
        '''
        self.scale = pygame.transform.scale(self.redbull, (self.length, self.width))
        screen.blit(self.scale, (self.coord[0], self.coord[1]))


class Editor:
    def __init__(self, gender, width_of_pictures, distance_between_roads):
        """
        Set parameters and their meanings
        """
        self.gender = gender
        self.done = 0
        self.step = (screen_size[0] - 2 * width_of_pictures - distance_between_roads * 2) // 3 + distance_between_roads
        self.hero = Hero(self.gender, coord=[screen_size[0] // 2, screen_size[1] - 20])
        self.time = 0
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.obstacles = []
        self.boosts = []
        self.event_is_on = False
        self.stats = Draw_stats()
        self.boost_color = pygame.Surface((screen_size_x, screen_size_y))
        self.boost_color.set_alpha(100)
        self.stream = Stream()
        self.analit = Analit()
        self.time_for_Kozhevnikov_test = 500

    def user_events(self, events):
        '''
        Analize events from keyboard, mouse, etc.
        '''
        self.done = 0
        for event in events:
            self.done = quit_condition(event.type)
            if not self.event_is_on:
                if event.type == pygame.KEYUP:
                    self.move_hero(event)

    def move_hero(self, event):
        '''
		Let hero run to the nearby road, but doesn't give him permission to go out of roads' borders
		'''
        if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (self.hero.number_of_road <= 2):
            self.hero.move(self.step)
            self.hero.number_of_road += 1
        if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and (self.hero.number_of_road >= 2):
            self.hero.move(- self.step)
            self.hero.number_of_road -= 1

    def move_obstacle(self):
        '''
		Increase y coordinate of obstacles, user see, how they are falling
		'''
        dead_obstacles = []
        for j, obstacle in enumerate(self.obstacles):
            obstacle.motion()
            if not obstacle.is_alive:  # looks if the obstacle is dead, add it to the "Death book" if it's its time to die
                dead_obstacles.append(j)
        for j in reversed(dead_obstacles):
            self.obstacles.pop(j)

    def move_boosts(self):
        '''
    	Increase y coordinate of boosts, user see, how they are falling
    	'''
        dead_boosts = []
        for j, boost in enumerate(self.boosts):
            boost.motion()
            if not boost.is_alive:  # looks if the obstacle is dead, add it to the "Death book" if it's its time to die
                dead_boosts.append(j)
        for j in reversed(dead_boosts):
            self.boosts.pop(j)

    def draw(self):
        '''
		Turns on all object's drawings processes
		'''
        draw_road(self.width_of_pictures, self.distance_between_roads)
        for obstacle in self.obstacles:
            obstacle.draw()
        for boost in self.boosts:
            boost.draw()
        self.stats.draw()
        self.hero.draw()
        self.stream.draw_button()
        draw_emergency_table(self)

    def check_bumping(self):
        '''
		Looks if it's time for the hero to die under the obstacle
		'''
        for obstacle in self.obstacles:
            if self.hero.coord[1] - 65 <= obstacle.coord[1] + obstacle.width:
                if (self.hero.number_of_road == obstacle.number_of_road) and not (self.stats.boost_scale.boost_points > 0):
                    self.hero.was_kicked = True
                    return True
                if (self.hero.number_of_road == obstacle.number_of_road) and (self.stats.boost_scale.boost_points > 0):
                    ellipse(screen, BLACK, (self.hero.coord[0] + 50, self.hero.coord[1] - 110, 150, 70), 2)
                    ellipse(screen, WHITE, (self.hero.coord[0] + 50, self.hero.coord[1] - 110, 149, 69))
                    draw_text('Я не хочу спать!', self.hero.coord[0] + 125, self.hero.coord[1] - 75, BLACK, 16)

    def hero_boosting(self):
        """
        Looks if the hero caught the boost
        """
        for boost in self.boosts:
            if self.hero.coord[1] - 45 // 4 <= boost.coord[1] + boost.width:
                if self.hero.number_of_road == boost.number_of_road:
                    boost.is_alive = False
                    self.stats.boost_scale.boost_points = 100
                    self.stats.mood_scale.mood_points += 200
                    if self.stats.mood_scale.mood_points > 1000:
                        self.stats.mood_scale.mood_points = 1000

    def boost_time(self):
        if ((self.stats.timer.time % 100 - self.stats.timer.time % 10) // 10) % 2 == 0:
            color = RED
        else:
            color = LIL
        self.boost_color.fill(color)
        screen.blit(self.boost_color, (0, 0))
        circle_sur = pygame.Surface((screen_size_x, screen_size_y))
        circle(circle_sur, BLUE, self.hero.coord, 85)
        circle_sur.set_alpha(100)
        screen.blit(circle_sur, (0, 0))
        draw_text('Ты полон энергии и неуязвим!', screen_size_x // 2, 15, CYAN, 20)

    def process(self, events):
        '''
		Manager function for all processes in program. It creates obstacles and control their movement, closes program because of pressed [X] button
		starts drawing of all process, looks if the hero was kicked
		'''
        if not self.event_is_on:
            self.time += 1
            if self.time % 40 == 0:
                self.obstacles.append(
                    Obstacle(10, randint(1, 3), 50, self.width_of_pictures, self.distance_between_roads))
            if self.time % 67 == 0:
                self.boosts.append(Boost(10, randint(1, 3), 70, self.width_of_pictures, self.distance_between_roads))
            self.done = 0
            self.user_events(events)
            self.draw()
            self.move_obstacle()
            self.move_boosts()
            self.hero_boosting()
            if self.stats.boost_scale.boost_points > 0:
            	self.boost_time()
            if self.check_bumping():
            	self.done = 2
            select_event(self, events)
        elif self.event_is_on:
            return_list = self.Event.progress(events)
            self.done = return_list[0]
            self.event_is_on = return_list[1]
            self.stats.points.points += return_list[2]
        return self.done

def select_event(self, events):
	if self.analit.pressed_or_not_button(events) and self.event_is_on == False:
		self.event_is_on = True
		self.Event = self.analit
	if self.time % 500 == 0 and self.time != self.time_for_Kozhevnikov_test:
		self.event_is_on = True
		self.Event = Ivanov_test()
	if self.time % 200 == 0:
		self.stream.stream_is_available = True
		self.stream.click_time = 100
	if self.stream.pressed_or_not_button(events) and self.event_is_on == False:
		self.event_is_on = True
		self.Event = self.stream
	if self.time == self.time_for_Kozhevnikov_test:
		self.event_is_on = True
		self.Event = Kozhevnikov_test()

def draw_emergency_table(self):
	if self.time >= self.time_for_Kozhevnikov_test - 50 and self.time <= self.time_for_Kozhevnikov_test and self.time % 6 != 0:
	    rect(screen, RED, (screen_size[0] - self.width_of_pictures, 2 * screen_size[1] // 3, 3 * self.width_of_pictures // 4, screen_size[1] // 8))
	    insert_text('Attention', 'Game-font.ttf', WHITE, (screen_size[0] - 6 * self.width_of_pictures // 10, 2 * screen_size[1] // 3 + screen_size[1] // 30), screen_size[1] // 30)
	    insert_text('Test is coming', 'Game-font.ttf', WHITE, (screen_size[0] - 6 * self.width_of_pictures // 10, 2 * screen_size[1] // 3 + screen_size[1] // 13), screen_size[1] // 37 )


if __name__ == "__main__":
    print("This module is not for direct call!")
