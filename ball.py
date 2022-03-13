import league
import pygame as pg


class Ball(league.DUGameObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self._layer = 1
        self.dirty = 2

        #Makeing of our ball
        self.image = pg.Surface((32, 32))
        self.image.fill((150,210,220,0))
        self.image.set_alpha(128)
        pg.draw.circle(self.image, (0,101,164), (16, 16), 16)

        #Sets the Starting point of our Ball
        self.rect = self.image.get_rect()
        self.x = 400
        self.y = 400
        self.direction_x = 1
        self.direction_y = 1

    def update(self):

        #Moves our ball
        self.x = self.x + self.engine.delta_time * self.direction_x
        self.y = self.y + self.engine.delta_time * self.direction_y
        self.rect.x = self.x
        self.rect.y = self.y

        #Keeps the ball on screen
        # if self.rect.left < 0:
        #     self.rect.left = 0
        #     self.direction_x = 1
        # if self.rect.right > 1023:
        #     self.rect.right = 1023
        #     self.direction_x = -1
        # if self.rect.top < 0:
        #     self.rect.top = 0
        #     self.direction_y = 1
        # if self.rect.bottom > 768:
        #     self.rect.bottom = 768
        #     self.direction_y = -1
        
        for event in self.engine.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.direction_x = -2
                if event.key == pg.K_d:
                    self.direction_x = 2
  
