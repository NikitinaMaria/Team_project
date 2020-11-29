from random import randrange as rnd, choice
from random import randint
import numpy as np
import pygame
from pygame.draw import *
from game_hero import *
from game_stats import *

#from Game.game_hero import Hero

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

def insert_picture(name, position, size):
    '''
    Paste image according to its position and size which written like (full_size_x, full_size_y)
    '''
    surf = pygame.image.load(name)
    surf = pygame.transform.scale(surf, size)
    rect = surf.get_rect(center = position)
    screen.blit(surf, rect)

def insert_text(string, font, color, position, size):
    '''
    Paste text according to the position of its center
    '''
    text_style = pygame.font.Font(font, size)
    surface = text_style.render(string, True, color)
    textRect = surface.get_rect(center = position)
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


class Obstacle():
    def __init__(self, speed, number_of_road, width, width_of_pictures, distance_between_roads):
        self.is_alive = True
        self.speed = speed
        self.width_of_road = (screen_size[0] - 2 * (width_of_pictures + distance_between_roads)) // 3
        self.width_of_all_road = screen_size_x - 2 * width_of_pictures
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.coord = [width_of_pictures + self.width_of_all_road // 4 + (number_of_road - 1) * (self.width_of_road // 2 + self.distance_between_roads // 2), 0]
        self.length = self.width_of_road // 2
        self.width = width
        self.number_of_road = number_of_road
        if number_of_road == 2:
            self.lower_distance_from_center_x = self.width_of_road // 4
        elif number_of_road == 3:
            self.lower_distance_from_center_x = self.width_of_road // 4 + self.distance_between_roads // 2
        else:
            self.lower_distance_from_center_x = self.width_of_road // 4 * 3 + self.distance_between_roads // 2

    def motion(self):
        '''
		Move obstacles, look if they are done
		'''
        self.coord[1] += self.speed
        if self.coord[1] >= screen_size[1] - self.width:
            self.is_alive = False
        self.length = self.width_of_road // 2 * (screen_size_y + self.coord[1]) // screen_size_y
        if self.number_of_road != 3:
            self.coord[0] = - self.coord[1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 - self.lower_distance_from_center_x
        else:
            self.coord[0] = self.coord[1] * self.lower_distance_from_center_x // screen_size_y + screen_size_x // 2 + self.lower_distance_from_center_x
        print(self.coord[0])
        print(self.coord[1])
        print(self.lower_distance_from_center_x)


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
        Set parameters and thier meanings
        '''
        self.done = 0
        self.step = (screen_size[0] - 2 * width_of_pictures - distance_between_roads * 2) // 3 + distance_between_roads
        self.hero = Hero(coord=[screen_size[0] // 2, screen_size[1] - 20])
        self.time = 0
        self.width_of_pictures = width_of_pictures
        self.distance_between_roads = distance_between_roads
        self.obstacles = []
        self.boosts = []
        self.test_is_on = False
        self.timer = Timer(self)
        self.mood_scale = Mood_scale(self)
        self.boost_scale = Boost_scale(self)

    def user_events(self, events):
        '''
        Analize events from keyboard, mouse, etc.
        '''
        self.done = 0
        for event in events:
            self.done = quit_condition(event.type)
            if not self.test_is_on:
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
        self.hero.draw()
        for obstacle in self.obstacles:
            obstacle.draw()
        for boost in self.boosts:
            boost.draw()
        self.mood_scale.draw()
        self.boost_scale.draw()
        self.timer.draw()

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
        if not self.test_is_on:
            self.time += 1
            if self.time % 20 == 0:
                self.obstacles.append(Obstacle(10, randint(1, 3), 10, self.width_of_pictures, self.distance_between_roads))
            if self.time % 47 == 0:
                self.boosts.append(Boost(10, randint(1,3), 70, self.width_of_pictures, self.distance_between_roads))
            self.done = 0
            self.user_events(events)
            self.draw()
            self.move_obstacle()
            self.move_boosts()   
            if self.hero_boosting():
                self.boost_scale.boost_points = 100
            if self.mood_scale.mood_points <= 0:
                self.done = 1
            if self.check_bumping():
                self.done = 2
            if self.time % 50 == 0:
                self.test_is_on = True
                self.Test = Ivanov_test()
        else:
            return_list = self.Test.progress(events)
            self.done = return_list[0]
            self.test_is_on = return_list[1]
        return self.done

class Ivanov_test():
    def __init__(self):
        '''
        Set test's parameters and thier meanings
        '''
        self.time = 0
        self.length = min(screen_size[0] // 7, screen_size[1] // 7 )
        self.done = 0
        self.time_is_over = False
        self.time_limit = 15 * FPS
        self.growing_time = 1 * FPS
        self.x = screen_size[0] // 2
        self.y = screen_size[1] // 4
        self.task = []
        self.length_of_answer_pic = self.length // 3
        self.create_task()
        self.number_of_task = 1
        self.answer_list = []
        self.score = 0
        
    def progress(self, events):
        '''
        Manager function for all proccesses in test
        '''
        self.time += 1
        self.draw()
        self.user_events(events)
        if self.time == self.time_limit:
            self.time_is_over = True
        return (self.done, not self.time_is_over)

    def create_task(self):
        '''
        Make the new list with numbers for numers wich mean:
        1 - for all
        2 - exist
        3 - equivalent (then and only then, when)
        4 - epsilon
        '''
        self.task = []
        for i in range(5):
            self.task.append(randint(1, 4))

    def draw(self):
        '''
        Draws all images and pictures in test
        '''
        time_scale = screen_size[0] / self.time_limit
        rect(screen, RED, (0, 0, int(self.time * time_scale), 10))
        if self.time <= self.growing_time:
            insert_text("Dancing time!", "Game-font.ttf", GREEN, (screen_size[0] // 2, screen_size[1] // 2), self.time * self.time)
        elif self.number_of_task <= 4:
            rect(screen, BLACK, (self.x - self.length // 2 - 10, self.y - self.length // 2 - 10, self.length + 20, self.length + 20), 5)
            self.number = self.task[len(self.task) - 1]
            if self.number == 1:
                self.draw_for_all()
            elif self.number == 2:
                self.draw_exist()
            elif self.number == 3:
                self.draw_equivalent()
            else:
                self.draw_epsilon() 
            insert_picture('Hint.png', (4 * screen_size[0] // 5, screen_size[1] // 3), (screen_size[0] // 3, screen_size[1] // 4))   
            for i in range(4):
                insert_text(str(i + 1) + ') ', "Game-font.ttf", BLACK, (screen_size[0] // 12, i * self.length_of_answer_pic + screen_size[1] // 5), 20)
        elif self.number_of_task >= 5:
            self.time = max(self.time, self.time_limit - (self.growing_time * 2))
            if self.score == 0:
                insert_picture('Falure.jpg', (screen_size[0] // 2, screen_size[1] // 2), (screen_size[0], screen_size[1])) 
                insert_text('You need to work harder', 'Game-font.ttf', WHITE, (screen_size[0] // 2, 3 * screen_size[1] // 4), min(screen_size[0] // 9, screen_size[1] // 9))
            for i in range(4):
                insert_text(str(i + 1) + ') ', "Game-font.ttf", BLACK, (screen_size[0] // 12, i * self.length_of_answer_pic + screen_size[1] // 5), 20)
            if self.score > 0:
                insert_text('Congrats! Your score: ' + str(self.score), "Game-font.ttf", RED, (screen_size_x // 2, screen_size_y // 2), 50)
        self.draw_right_or_wrong_answer()
        pygame.display.update()

    def draw_right_or_wrong_answer(self):
        '''
        Putting pictures of green arrow for right answer or red X for wrong answer
        '''
        for i in range(self.number_of_task - 1):
            if self.answer_list[i] == True:
                insert_picture('right_ans.png', (screen_size[0] // 12 +  self.length_of_answer_pic, i * self.length_of_answer_pic + screen_size[1] // 5), 
                              (self.length_of_answer_pic, self.length_of_answer_pic))
            else:
                insert_picture('wrong.jpg', (screen_size[0] // 12 +  self.length_of_answer_pic, i * self.length_of_answer_pic + screen_size[1] // 5), 
                              (self.length_of_answer_pic, self.length_of_answer_pic))
        
    def user_events(self, events):
        '''
        Analize events from keyboard, mouse, etc.
        '''
        for event in events: 
            self.done = quit_condition(event.type)
            if (self.time >= self.growing_time) and (event.type == pygame.KEYUP):
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (self.number == 4):
                    self.task.pop(len(self.task) - 1)
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and (self.number == 3):
                    self.task.pop(len(self.task) - 1)
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and (self.number == 1):
                    self.task.pop(len(self.task) - 1)
                elif (event.key == pygame.K_w or event.key == pygame.K_UP) and (self.number == 2):
                    self.task.pop(len(self.task) - 1)
                else:
                    self.answer_list.append(False)
                    self.create_task()
                    self.number_of_task += 1
                if len(self.task) == 0:
                    self.create_task()
                    self.answer_list.append(True)
                    self.number_of_task += 1
                    self.score += 1
    
    def draw_for_all(self):
        line(screen, BLACK, (self.x - self.length // 2, self.y - self.length // 2), (self.x , self.y + self.length // 2), 5)
        line(screen, BLACK, (self.x , self.y + self.length // 2), (self.x + self.length // 2, self.y - self.length // 2), 5)
        line(screen, BLACK, (self.x - self.length // 4, self.y ), (self.x + self.length // 4, self.y ), 5)

    def draw_exist(self):
        for i in range(3):
            line(screen, BLACK, (self.x - self.length // 4, self.y - self.length // 2 + (self.length // 2) * i), 
                (self.x + self.length // 2, self.y - self.length // 2 + (self.length // 2) * i), 5 )
        line(screen, BLACK, (self.x + self.length // 2, self.y - self.length // 2), (self.x + self.length // 2, self.y + self.length // 2), 5)

    def draw_equivalent(self):
        line(screen, BLACK, (self.x - self.length // 4, self.y - self.length // 8), (self.x + self.length // 4, self.y - self.length // 8), 5)
        line(screen, BLACK, (self.x - self.length // 4, self.y + self.length // 8), (self.x + self.length // 4, self.y + self.length // 8), 5)
        for i in range(-1, 3, 2):
            line(screen, BLACK, (self.x - i * self.length // 2, self.y), (self.x - i * self.length // 13, self.y - self.length // 4 + 4 ), 5)
            line(screen, BLACK, (self.x - i * self.length // 2, self.y), (self.x - i * self.length // 13, self.y + self.length // 4 - 4 ), 5)
    
    def draw_epsilon(self):
        insert_picture('epsilon.jpg', (self.x, self.y), (self.length, self.length))

if __name__ == "__main__":
    print("This module is not for direct call!")
