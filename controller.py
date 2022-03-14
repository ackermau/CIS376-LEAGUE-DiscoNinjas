import league
import pygame as pg

# Lets use this to draw our scoreboards too.

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)  

class GameController(league.DUGameObject):
    def __init__(self, engine, total_torches):
        super().__init__()
        self.engine = engine
        self.score = 0
        self.lives = 5
        self.totLives = 5
        self.total = total_torches
        self.font = pg.font.Font(pg.font.get_default_font(), 16)
        text = self.font.render(f"Torches: {self.score}/{self.total}", True, blue)
        self.rect = text.get_rect()
        self.rect.center = (10, 10)
        self.image = text
        

    def update(self):
        if self.score < 15:
            text = self.font.render(f"Score: {self.score}/{self.total}", True, blue)
            self.rect = text.get_rect()
            self.rect.center = (50, 50)
            self.rect = text.get_rect()
            self.image = text
        else:
            text = self.font.render(f"You Win", True, blue)
            self.rect = text.get_rect()
            self.rect.center = (50, 50)
            self.rect = text.get_rect()
            self.image = text
