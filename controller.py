import league
import pygame as pg

# Lets use this to draw our scoreboards too.

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)  

class GameController(league.DUGameObject):
    def __init__(self, engine, total_torches, screen):
        super().__init__()
        self.engine = engine
        self.score = 0
        self.lives = 5
        self.total_lives = 5
        self.screen = screen
        self.total = total_torches
        self.font = pg.font.Font(pg.font.get_default_font(), 16)
        
    def update(self):
        if self.score < 15 and self.lives > 0:
            self.torch_text = self.font.render(f"Score: {self.score}/{self.total}                                                                                                                                                               Lives: {self.lives}/{self.total_lives}", True, blue)
            self.rect = self.torch_text.get_rect()
            self.rect.topleft = (0, 0)
            self.image = self.torch_text
        elif self.score == 15:
            self.win_text = self.font.render(f"You Win", True, blue)
            self.rect = self.win_text.get_rect()
            self.rect.topleft = (0, 0)
            self.image = self.win_text
        elif self.lives == 0:
            self.lose_text = self.font.render(f"You Lose", True, blue)
            self.rect = self.lose_text.get_rect()
            self.rect.topleft = (0, 0)
            self.image = self.lose_text
