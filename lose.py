import league
import pygame as pg

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)  

class LoseController(league.DUGameObject):
    def __init__(self):
        super().__init__()
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        text = self.font.render(f"You Lose", True, green)
        self.rect = text.get_rect()
        self.rect.center = (100, 100)
        self.image = text