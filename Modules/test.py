import pygame

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_size_x = 1000
screen_size_y = 600
FPS = 5

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))

def draw_text(text, x, y, color, size):
    """
    The function adds a field with text
    :param text: What you need to write
    :param x: Coordinate x of the text center
    :param y: Coordinate y of the text center
    :param color: Text color
    :param size: Text size
    """
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color)
    place = text.get_rect()
    place.center = (x, y)
    screen.blit(text, place)

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

clock = pygame.time.Clock()
done = 0
time = 0
add = 1

while not done:
    for event in pygame.event.get():
        done = quit_condition(event.type)
    screen.fill(BLACK)
    draw_text('Testing', screen_size_x // 2, time, WHITE, 50)
    time += add
    if time >= screen_size_y:
        add = -1
    if time <= 0:
        add = 1
    pygame.display.update()

pygame.quit()