import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDHT = 800
SCREEN_HEIGHT = 600

# Setting up the screen
screen = pygame.display.set_mode([SCREEN_WIDHT, SCREEN_WIDHT])

running = True

# Main Loop
while running:

    # Event Q
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == QUIT:
            running = False
