import league

level_one = league.Scene("Level One")
level_one.set_fps(10)

engine = league.Engine("EMGGG", level_one)

engine.run()

# engine.stop()