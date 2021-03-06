from random import randint
import pygame
from pygame.draw import *
from Modules.game_hero import *
from Modules.game_stats import *
from Modules.Game_events import *
from Modules.game_supporting import *
from Modules.game_design import *

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
    :param pressed_button: User action
    :return: Finish the game or not
    """
    final = 0
    if pressed_button == pygame.QUIT:
        final = 1
    return final


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
        self.stars = []
        self.event_is_on = False
        self.stats = Draw_stats()
        self.boost_color = pygame.Surface((screen_size_x, screen_size_y))
        self.boost_color.set_alpha(100)
        self.stream = Stream()
        self.analit = Analit()
        self.time_for_Kozhevnikov_test = 600

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
            if not boost.is_alive:  # looks if the boost is dead, add it to the "Death book" if it's its time to die
                dead_boosts.append(j)
        for j in reversed(dead_boosts):
            self.boosts.pop(j)

    def move_stars(self):
        '''
    	Increase y coordinate of stars, user see, how they are falling
    	'''
        dead_stars = []
        for j, star in enumerate(self.stars):
            star.motion()
            if not star.is_alive:  # looks if the star is dead, add it to the "Death book" if it's its time to die
                dead_stars.append(j)
        for j in reversed(dead_stars):
            self.stars.pop(j)

    def draw(self):
        '''
        Turns on all object's drawings processes
        '''
        screen.fill(BLACK)
        if not draw_titers(self):
            draw_road(self.width_of_pictures, self.distance_between_roads)
            for star in self.stars:
                star.draw()
            for obstacle in self.obstacles:
                obstacle.draw()
            for boost in self.boosts:
                boost.draw()
            if self.done != 1:
                self.done = self.stats.draw()
            self.hero.draw()
            self.stream.draw_button()
            draw_emergency_table(self)
            self.analit.draw_sweater()

    def check_bumping(self):
        '''
		Looks if it's time for the hero to die under the obstacle
		'''
        for obstacle in self.obstacles:
            if self.hero.coord[1] - 65 <= obstacle.coord[1] + obstacle.width:
                if (self.hero.number_of_road == obstacle.number_of_road) and not (
                        self.stats.boost_scale.boost_points > 0):
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
                    if self.stats.mood_scale.mood_points > 400:
                        self.stats.mood_scale.mood_points = 400

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
            self.user_events(events)
            self.draw()
            if self.time > 15 * FPS:
                if self.time % 40 == 0:
                    self.obstacles.append(
                        Obstacle(10, randint(1, 3), 50, self.width_of_pictures, self.distance_between_roads))
                if self.time % 67 == 0:
                    self.boosts.append(
                        Boost(10, randint(1, 3), 70, self.width_of_pictures, self.distance_between_roads))
                if self.time % 30 == 0:
                    self.stars.append(Stars(10, self.width_of_pictures))
                self.move_stars()
                self.move_obstacle()
                self.move_boosts()
                self.hero_boosting()
                if self.stats.boost_scale.boost_points > 0:
                    self.boost_time()
                if self.check_bumping():
                    self.done = 2
                self.select_event(events)
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
        if self.time % 900 == 0 and self.time != self.time_for_Kozhevnikov_test:
            self.event_is_on = True
            FPS = 20
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
        if self.time == 400:
            self.event_is_on = True
            self.Event = Evening()


if __name__ == "__main__":
    print("This module is not for direct call!")
