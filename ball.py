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
        self.jump = gm.Vector3(0,-300,0)
        self.j = 0

    def update(self):

        # Did we collide?
        on_platform = False
        can_move = True

        for collideable in self.scene.collideables:
            if self.rect.colliderect(collideable.rect):
                if collideable.type == "torch":
                    self.controller.score += 1
                    self.scene.collideables.remove(collideable)
                    self.scene.drawables.remove(collideable)
                if collideable.type == "shots":
                    self.controller.lives -= 1
                    self.x = 400
                    self.y = 1500
                    
                if collideable.type == "platform":
                    on_platform = True
                    if self.rect.collidepoint(collideable.rect.midleft) or self.rect.collidepoint(collideable.rect.midright):
                        can_move = False
                        self.vel.x = 0
                        self.accel.x = 0
                    if self.rect.collidepoint(collideable.rect.midbottom):
                        self.vel.y *= -1

        # if self.rect.collidepoint(self.rect.left) or self.rect.collid(self.rect.right):
        #     can_move = False
        #     print(can_move)

        if self.x > 800:
            self.x = 0
        
        if self.x < 0:
            self.x = 800

        if on_platform and self.j == 0:
            self.vel.y = 0
            self.accel.y = 0
            if (not can_move):
                self.vel.x = 0
                self.accel.x = 0
            self.can_jump = True
        if on_platform == False:
            can_move = True
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
    def __init__(self,engine,scene):
        self.engine = engine
        self.scene = scene
        self.start_y = 0
        self.x = 0
        self.y = 0
        self.start_x = 0

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
        self.rect.y = self.y * 32
