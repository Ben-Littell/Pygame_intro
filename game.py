import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, BLACK]

# Math Constants
PI = math.pi

# Game Constants
SIZE = (700, 500)
FPS = 60

##############################################################################
##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('My First Pygame')

clock = pygame.time.Clock()

running = True
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print('You pressed a key')
        elif event.type == pygame.KEYUP:
            print('You pressed a key up')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('You Pressed the mouse button down')
        elif event.type == pygame.MOUSEBUTTONUP:
            print('You Pressed the mouse button up')

    # game logic goes here
    screen.fill(WHITE)
    # Drawing goes here
    # rect first 2 are xy (55,50) upper left corner then width and height (20,250)
    pygame.draw.rect(screen, RED, (55, 50, 200, 250))
    pygame.draw.arc(screen, WHITE, (55, 50, 200, 200), 0, 5*PI/4, width=5)
    for multiplier in range(14):
        color = random.choice(COLORS)
        pygame.draw.line(screen, color, (20 + 15*multiplier, 10), (60 + 15*multiplier, 50), 5)

    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
