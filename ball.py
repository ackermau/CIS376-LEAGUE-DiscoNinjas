import league
import pygame as pg


class Ball(league.DUGameObject):
    def __init__(self, engine, scene):
        super().__init__()
        self.engine = engine
        self.scene = scene
        self._layer = 1
        self.dirty = 2
        self.can_jump = False

        # Making of our ball
        self.image = pg.Surface((32, 32))
        self.image.fill((150, 210, 220, 0))
        self.image.set_alpha(255)
        pg.draw.circle(self.image, (0, 101, 164), (16, 16), 16)

        # Sets the Starting point of our Ball
        self.rect = self.image.get_rect()
        self.x = 400
        self.y = 400
        self.direction_x = 1
        self.direction_y = 1

    def update(self):

        # Downwards acceleration
        self.direction_y += 10

        # Did we collide?
        collide = False

        for collideable in self.scene.collideables:
            if self.rect.colliderect(collideable.rect):
                collide = True

        if collide:
            self.direction_y = 0
            self.can_jump = True

        # Moves our ball
        self.x = self.x + self.engine.delta_time * self.direction_x
        self.y = self.y + self.engine.delta_time * self.direction_y
        self.rect.x = self.x
        self.rect.y = self.y

        # Keeps the ball on screen
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
                    self.direction_x = -100
                if event.key == pg.K_d:
                    self.direction_x = 100
                if event.key == pg.K_SPACE:
                    if self.can_jump:
                        self.direction_y = 100
