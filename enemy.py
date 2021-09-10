import pygame as pg
import os, flyingace, random
from pygame.sprite import Sprite
ENEMY_SPEED = 2
class Enemy(Sprite):
    def __init__(self, x, y, player_plane):
        super().__init__()
        self.image = pg.image.load(os.path.join(flyingace.Format.img_folder, 'blue_plane.png')).convert()
        self.image.set_colorkey(flyingace.Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # add a reference to the player's plane to access player plane members
        self.player_plane = player_plane
    
    def update(self):
        self.rect.x -= ENEMY_SPEED
        if self.rect.right <= 0:
            self.rect.left = flyingace.Format.WIDTH
            self.rect.y = random.randint(50, flyingace.Format.HEIGHT - 50)
            self.player_plane.points += 1
        