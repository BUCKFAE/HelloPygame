import pygame
from player import *
from enemy import *

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

# Creating a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

running = True

# Clock
clock = pygame.time.Clock()

# Creating a new player
player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main Loop
while running:

    # Event Q
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        # Adding new enemy?
        if event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        if event.type == QUIT:
            running = False

    screen.fill(("#0273f8"))


    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()

    # Draw all sprites
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    # Check if any enemies have collided witht he player
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()
    clock.tick(60)
