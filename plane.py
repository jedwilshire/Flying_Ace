import pygame as pg
from flyingace import Format, Color
from pygame.sprite import Sprite
class Plane(Sprite):
    def __init__(self):
        super().__init__()
        # create a basic square to represent out plane
        self.image = pg.Surface((50, 50))
        self.image.fill(Color.RED)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 50
