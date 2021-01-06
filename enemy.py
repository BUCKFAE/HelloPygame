import random
import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill("#69373b")
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDHT + 20, SCREEN_WIDHT + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
