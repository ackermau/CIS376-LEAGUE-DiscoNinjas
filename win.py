import league
import pygame as pg

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)  

class WinController(league.DUGameObject):
    def __init__(self):
        super().__init__()
        self._layer = 1
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        text = self.font.render(f"You Win", True, blue)
        self.rect = text.get_rect()
        self.rect.center = (100, 500)
        self.image = text
