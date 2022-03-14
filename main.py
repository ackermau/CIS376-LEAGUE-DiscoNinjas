from pytmx.util_pygame import load_pygame
import league
import ball
import pygame
import pytmx
level_one = pytmx.TiledMap('Map/baseMap.tmx')

level_one = league.Scene("Level One")
level_one.set_fps(60)
engine = league.Engine("Disco Ninjas blue ball          z", level_one)
engine.init_pygame()

screen = pygame.display.set_mode((1600, 800))
map = load_pygame('Map/baseMap.tmx')


for x, y, image in map.layers[0].tiles():
    tmp = league.DGameObject()
    tmp._layer = map.layers[0].tiles()
    tmp.image = image
    tmp.rect = tmp.image.get_rect()
    tmp.rect.x = x * map.tilewidth
    tmp.rect.y = y * map.tileheight
    level_one.drawables.append(tmp)

for x, y, image in map.layers[1].tiles():
    tmp = league.DGameObject()
    tmp._layer = map.layers[1].tiles()
    tmp.image = image
    tmp.rect = tmp.image.get_rect()
    tmp.rect.x = x * map.tilewidth
    tmp.rect.y = y * map.tileheight
    tmp.type = "platform"
    level_one.drawables.append(tmp)
    level_one.collideables.append(tmp)

for x, y, image in map.layers[2].tiles():
    tmp = league.DUGameObject()
    tmp._layer = map.layers[2].tiles()
    tmp.image = image
    tmp.rect = tmp.image.get_rect()
    tmp.rect.x = x * map.tilewidth
    tmp.rect.y = y * map.tileheight
    tmp.type = "torch"
    level_one.drawables.append(tmp)
    level_one.updateables.append(tmp)
    level_one.collideables.append(tmp)

ball = ball.Ball(engine, level_one)
level_one.drawables.append(ball)
level_one.updateables.append(ball)

engine.run()
