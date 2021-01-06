import pygame
from player import *

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

from settings import *

pygame.init()

# Setting up the screen
screen = pygame.display.set_mode([SCREEN_WIDHT, SCREEN_HEIGHT])

running = True

# Creating a new player
player = Player()

# Main Loop
while running:

    # Event Q
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == QUIT:
            running = False

    screen.fill(("#0273f8"))


    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    pygame.display.flip()
