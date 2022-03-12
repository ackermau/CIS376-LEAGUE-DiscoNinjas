import league
import ball
from pytmx.util_pygame import load_pygame


level_one = league.Scene("Level One")
level_one.set_fps(60)
map = load_pygame('test/baseMap.tmx')


engine = league.Engine("Disco Ninjas blue ball          z", level_one)
engine.init_pygame()
for layer in map.layers:
    for x, y, image in map.tiles():
        tmp = league.DUGameObject()
        tmp._layer = layer
        tmp.image = image
        tmp.rect = tmp.image.get_rect()
        tmp.rect.x = x * map.tilewidth
        tmp.rect.y = y * map.tileheight
        level_one.drawables.append(tmp)

# ball = ball.Ball(engine)
# level_one.drawables.append(ball)
# level_one.updateables.append(ball)

engine.run()

