from random import randrange as rnd, choice
from random import randint
import pygame
from pygame.draw import *
from game_hero import *

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


def quit_condition(pressed_button):
    """
	Checks if [X] button was pressed
	"""
    final = 0
    if pressed_button == pygame.QUIT:
        final = 1
    return final


def draw_road(width_of_pictures, distance_between_roads):
    '''
	Function draws three main roads according of the size of the left and rigth pictures and distance between roads
	'''
    width_of_road = (screen_size[0] - 2 * width_of_pictures - distance_between_roads * 2) // 3
    rect(screen, BLACK, (width_of_pictures, 0, screen_size[0] - 2 * width_of_pictures - 2, screen_size[1]))
    for i in range(3):
        rect(screen, GREY,
             (width_of_pictures + i * (width_of_road + distance_between_roads), 0, width_of_road, screen_size[1]))


def show_game_over_table(done):
    '''
	Shows "Game over" table after the hero was smashed by obstacle
	'''
    screen.fill(GREEN)
    font = pygame.font.SysFont("dejavusansmono", 100)
    over_surface = font.render("Game Over", True, WHITE)
    textRect = over_surface.get_rect()
    textRect.center = (screen_size[0] // 2, screen_size[1] // 2)
    screen.blit(over_surface, textRect)
    pygame.display.update()
    while done != 1:
        for event in pygame.event.get():
            done = quit_condition(event.type)


class Obstacle():
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.coord = [width_of_pictures + (number_of_road - 1) * (self.width_of_road + self.distance_between_roads), 0]
        self.length = self.width_of_road
        self.width = width
        self.number_of_road = number_of_road

    def motion(self):
        '''
		Move obstacles, look if they are done
		'''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] - self.width:
            self.is_alive = False

    def draw(self):
        '''
		Draws obstacles. Attention: coords are the coordinates of the left top corner
		'''
        rect(screen, MAGENTA, (self.coord[0], self.coord[1], self.length, self.width))


class Boost():
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.coord = [width_of_pictures + (number_of_road - 1) * (self.width_of_road + self.distance_between_roads), 0]
        self.width = width
        self.number_of_road = number_of_road
        self.redbull = pygame.image.load('RedBull.png')
        self.scale = pygame.transform.scale(self.redbull, (70, self.width))

    def motion(self):
        '''
        Move obstacles, look if they are done
        '''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] + self.width:
            self.is_alive = False

    def draw(self):
        '''
        Draws obstacles. Attention: coords are the coordinates of the left top corner
        '''
        screen.blit(self.scale, (self.coord[0] + self.width_of_road // 2 - self.width // 2, self.coord[1]))


class Editor():
    def __init__(self, width_of_pictures, distance_between_roads):
        '''
        Set ball's parameters and thier meanings
        '''
        self.done = 0
        self.step = (screen_size[0] - 2 * width_of_pictures - distance_between_roads * 2) // 3 + distance_between_roads
        self.hero = Hero(coord=[screen_size[0] // 2, screen_size[1] - 20])
        self.time = 0
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.obstacles = []
        self.boosts = []

    def user_events(self, events):
        '''
        Analize events from keyboard, mouse, etc.
        '''
        self.done = 0
        for event in events:
            self.done = quit_condition(event.type)
            if event.type == pygame.KEYUP:
                self.move_hero(event)
        return self.done

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
        self.hero.draw()
        for obstacle in self.obstacles:
            obstacle.draw()
        for boost in self.boosts:
            boost.draw()

    def check_bumping(self):
        '''
		Looks if it's time for the hero to die under the obstacle
		'''
        for obstacle in self.obstacles:
            if self.hero.coord[1] - self.hero.length <= obstacle.coord[1] + obstacle.width:
                if self.hero.number_of_road == obstacle.number_of_road:
                    self.hero.was_kicked = True
                    return True

    def hero_boosting(self):
        """
        Looks if the hero caught the boost
        :return:
        """
        for boost in self.boosts:
            if self.hero.coord[1] - self.hero.length <= boost.coord[1] + boost.width:
                if self.hero.number_of_road == boost.number_of_road:
		    boost.is_alive = False
                    return True

    def process(self, events):
        '''
		Manager function for all processes in program. It creates obstacles and control their movement, closes program because of pressed [X] button
		starts drawing of all process, looks if the hero was kicked
		'''
        self.time += 1
        if self.time % 20 == 0:
            self.obstacles.append(Obstacle(10, randint(1, 3), 10, self.width_of_pictures, self.distance_between_roads))
        if self.time % 47 == 0:
            self.boosts.append(Boost(10, randint(1,3), 70, self.width_of_pictures, self.distance_between_roads))
        self.done = 0
        self.done = self.user_events(events)
        self.draw()
        self.move_obstacle()
        self.move_boosts()
        if self.check_bumping():
            self.done = 2
        return self.done


if __name__ == "__main__":
    print("This module is not for direct call!")
