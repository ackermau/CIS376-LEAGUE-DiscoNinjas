import league
import pygame as pg


# class Ball(league.GameObject):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self._layer = 1
#         self.dirty = 2
#         self.image = pg.Surface((32,32))
#         self.image.fill((255,255,0,0))
#         pg.draw.circle(self.image, (0,101,164), (16, 16), 16)
#         self.rect = self.image.get_rect()
#         self.x = 0
#         self.y = 0
#         self.direction_x = 1
#         self.direction_y = 1
#     def update(self):
#         self.x = self.x + league.Engine.delta_time * 100 * self.direction_x
#         self.y = self.y + league.Engine.delta_time * 100 * self.direction_y
#         self.rect.x = self.x
#         self.rect.y = self.y
#         if self.rect.left < 0:
#             self.rect.left = 0
#             self.direction_x = self.direction_x * -1
#         if self.rect.right > 1023:
#             self.rect.right = 1023
#             self.direction_x = self.direction_x * -1
#         if self.rect.top < 0:
#             self.rect.top = 0
#             self.direction_y = self.direction_y * -1
#         if self.rect.bottom > 768:
#             self.rect.bottom = 768
#             self.direction_y = self.direction_y * -1

class Square():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        


level_one = league.Scene("Level One")
level_one.set_fps(10)

level_one.updateables.append()

engine = league.Engine("EMGGG", level_one)

engine.run()

# engine.stop()

