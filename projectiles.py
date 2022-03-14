import league
import game_math as gm
import pygame as pg

class Enemy(league.DUGameObject):
    def __init__(self,engine,scene):
        self.engine = engine
        self.scene = scene

    def set_y(self, index):
        self.start_y = index
        self.y = index
    def set_x(self, index):
        self.x = index
        self.start_x = index

    def update(self):
        if(self.start_x < 20):
            self.direction_x = 20
        else:
            self.direction_x = -20
        self.direction_y = 0

            # Moves our enemies
        if self.x > 30:
            self.x = 0
        if self.x < 0:
            self.x = 25
        self.x = self.x + self.engine.delta_time * self.direction_x
        self.y = self.y + self.engine.delta_time * self.direction_y
        self.rect.x = self.x * 32
        self.rect.y = self.y