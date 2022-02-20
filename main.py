import league
import ball

level_one = league.Scene("Level One")
level_one.set_fps(60)

engine = league.Engine("Disco Ninjas blue ball          z", level_one)
ball = ball.Ball(engine)
level_one.drawables.append(ball)
level_one.updateables.append(ball)

engine.run()

