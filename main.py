import league
import ball
import pygame
import pytmx
level_one = pytmx.TiledMap('Map/baseMap.tmx')
from pytmx.util_pygame import load_pygame

level_one = league.Scene("Level One")
level_one.set_fps(60)
engine = league.Engine("Disco Ninjas blue ball          z", level_one)
engine.init_pygame()

screen = pygame.display.set_mode((1600, 800))
map = load_pygame('Map/baseMap.tmx')

for layer in map.layers:
    for x, y, image in layer.tiles():
        tmp = league.DGameObject()
        tmp._layer = layer
        tmp.image = image
        tmp.rect = tmp.image.get_rect()
        tmp.rect.x = x * map.tilewidth
        tmp.rect.y = y * map.tileheight
        level_one.drawables.append(tmp)

ball = ball.Ball(engine)
level_one.drawables.append(ball)
level_one.updateables.append(ball)

engine.run()

