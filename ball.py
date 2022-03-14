import league
import game_math as gm
import pygame as pg


class Ball(league.DUGameObject):
    def __init__(self, engine, scene, controller):
        super().__init__()
        self.engine = engine
        self.scene = scene
        self._layer = 1
        self.dirty = 2
        self.can_jump = False
        self.controller = controller

        # Making of our ball
        self.image = pg.Surface((32, 32))
        self.image.fill((150, 210, 220, 0))
        self.image.set_alpha(255)
        pg.draw.circle(self.image, (0, 101, 164), (16, 16), 16)

        # Sets the Starting point of our Ball
        self.rect = self.image.get_rect()
        self.x = 400
        self.y = 1500
        self.direction_x = 1
        self.direction_y = 1
        self.vel = gm.Vector3(0,0,0)
        self.accel = gm.Vector3(0,400,0)
        self.jump = gm.Vector3(0,-200,0)
        self.j = 0

    def update(self):

        # Did we collide?
        on_platform = False

        for collideable in self.scene.collideables:
            if self.rect.colliderect(collideable.rect):
                if collideable.type == "torch":
                    self.controller.score += 1
                    self.scene.collideables.remove(collideable)
                    self.scene.drawables.remove(collideable)
                if collideable.type == "platform":
                    on_platform = True

        if self.x > 800:
            self.x = 0
        
        if self.x < 0:
            self.x = 800

        if on_platform and self.j == 0:
            self.vel.y = 0
            self.accel.y = 0
            self.can_jump = True
        if on_platform == False:
            self.accel.y = 300
            self.j = 0
            self.can_jump = False

        # Moves our ball
        self.vel += self.accel.scale(self.engine.delta_time)
        self.x = self.x + self.engine.delta_time * self.vel.x * self.direction_x
        self.y = self.y + self.engine.delta_time * self.vel.y * self.direction_y
        self.rect.x = self.x
        self.rect.y = self.y

        # Keeps the ball on screen
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > self.engine.width:
        #     self.rect.right = self.engine.width

        for event in self.engine.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.vel.x -= 50
                if event.key == pg.K_d:
                    self.vel.x += 50
                if event.key == pg.K_SPACE:
                    if self.can_jump:
                        self.accel.y = 400
                        self.vel += self.jump
                        self.j = 1

class Enemy(league.DUGameObject):
    def __init__(self, engine, scene, start_x, start_y):
        super().__init__()
        self.engine = engine
        self.scene = scene
        self._layer =  1
        self.dirty = 2
        self.can_jump = False


        # Making of our ball
        self.image = pg.Surface((32, 32))
        self.image.fill((150, 210, 220, 0))
        self.image.set_alpha(255)
        pg.draw.circle(self.image, (0, 101, 164), (16, 16), 16)

        # Sets the Starting point of our Ball
        self.rect = self.image.get_rect()
        self.x = start_x
        self.y = start_y
        self.start_x = self.x
        self.start_y = self.y
        self.direction_x = 1
        self.direction_y = 1

    def update(self):

    # Downwards acceleration
        self.direction_x = 500
        self.direction_y = 0

        # Did we collide?
        on_platform = False

        in_bounds = True

        for collideable in self.scene.collideables:
            if self.rect.colliderect(collideable.rect):
                if collideable.type == "platform":
                    on_platform = True

        if on_platform:
            self.direction_y = 0

        while in_bounds:
            # Moves our ball
            if self.x > 800:
                self.x = 0
                self.y = self.start_y
            self.x = self.x + self.engine.delta_time * self.direction_x
            self.y = self.y + self.engine.delta_time * self.direction_y
            self.rect.x = self.x
            self.rect.y = self.y
            in_bounds = False

        # Moves our ball
