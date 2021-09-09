import pygame as pg
import os, flyingace
from pygame.sprite import Sprite


class Plane(Sprite):
    def __init__(self):
        super().__init__()
        # create a basic square to represent out plane
        self.image = pg.image.load(os.path.join(flyingace.Format.img_folder, 'biplane.png')).convert()
        self.image.set_colorkey(flyingace.Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 50
        self.vy = 0
        self.vx = 0
        self.engine_sound = pg.mixer.Sound(os.path.join(flyingace.Format.sounds_folder, 'engine_hum.ogg'))
        self.engine_sound.play(loops = -1)
        self.alive = True
    def update(self):
        if self.alive:
            if not (self.rect.right >= flyingace.Format.WIDTH and self.vx > 0) and not (self.rect.left <= 0 and self.vx < 0):
                self.rect.x += self.vx
            if not (self.rect.top <= 0 and self.vy < 0) and not (self.rect.bottom >= flyingace.Format.HEIGHT and self.vy > 0):
                self.rect.y += self.vy
        elif not self.alive:
            self.rect.y += self.vy
        if not self.alive and self.rect.top > flyingace.Format.HEIGHT:
            self.kill()

    def break_up(self):
        self.image = pg.image.load(os.path.join(flyingace.Format.img_folder, 'biplane_broken.png')).convert()
        self.image.set_colorkey(flyingace.Color.BLACK)
        self.alive = False
        self.vy = 4



