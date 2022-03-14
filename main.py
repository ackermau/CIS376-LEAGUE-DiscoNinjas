from pytmx.util_pygame import load_pygame
import league
import ball
import pygame
import pytmx
from controller import GameController

from scroller import Scroller


level_one = league.Scene("Level One")
level_one.set_fps(60)
engine = league.Engine("Disco Ninjas blue ball          z", level_one)
engine.init_pygame()

screen = pygame.display.set_mode((800, 1600))
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

torch_count = 0
for x, y, image in map.layers[2].tiles():
    torch_count += 1
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

enemy = ball.Enemy(engine, level_one, 0, 400)
enemy2 = ball.Enemy(engine, level_one, 0, 200)
enemy3 = ball.Enemy(engine, level_one, 0, 560)
enemy4 = ball.Enemy(engine, level_one, 0, 860)


enemy.type = "enemy"
level_one.drawables.append(enemy)
level_one.updateables.append(enemy)
level_one.collideables.append(enemy)

enemy2.type = "enemy"
level_one.drawables.append(enemy2)
level_one.updateables.append(enemy2)
level_one.collideables.append(enemy2)

enemy3.type = "enemy"
level_one.drawables.append(enemy3)
level_one.updateables.append(enemy3)
level_one.collideables.append(enemy3)

enemy4.type = "enemy"
level_one.drawables.append(enemy4)
level_one.updateables.append(enemy4)
level_one.collideables.append(enemy4)

controller = GameController(engine, torch_count)
level_one.updateables.append(controller)
level_one.drawables.append(controller)


player = ball.Ball(engine, level_one, controller)
level_one.drawables.append(player)
level_one.updateables.append(player)

scroller = Scroller(engine, level_one, player)
level_one.updateables.append(scroller)

engine.run()
