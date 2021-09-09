import pygame as pg
import os, random, flyingace
from pygame.sprite import Sprite
CLOUD_SPEED = 1
class Cloud(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((100, 50))
        pg.draw.ellipse(self.image, flyingace.Color.WHITE, pg.Rect(0, 0, 100, 50))
        self.image.set_colorkey(flyingace.Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x -= CLOUD_SPEED
        if self.rect.right < 0:
            self.rect.left = flyingace.Format.WIDTH
            self.rect.y = random.randint(50, flyingace.Format.HEIGHT - 50)
        