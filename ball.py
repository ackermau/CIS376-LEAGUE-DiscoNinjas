import league
import pygame as pg

class Ball(league.DUGameObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self._layer = 1
        self.dirty = 2
        self.image = pg.Surface((32,32))
        self.image.fill((255,255,255,0))
        pg.draw.circle(self.image, (0,101,164), (16, 16), 16)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.direction_x = 1
        self.direction_y = 1

    def update(self):
        self.x = self.x + self.engine.delta_time * 100 * self.direction_x
        self.y = self.y + self.engine.delta_time * 100 * self.direction_y
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction_x = self.direction_x * -1
        if self.rect.right > 1023:
            self.rect.right = 1023
            self.direction_x = self.direction_x * -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction_y = self.direction_y * -1
        if self.rect.bottom > 768:
            self.rect.bottom = 768
            self.direction_y = self.direction_y * -1 