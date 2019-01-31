import arcade
from game.game import Game

'''
TO DO list:
- push key -> jet (not only one)
- add perturbation in order to make sure the ATS doesn't go straight

BONUS:
- set difficulties levels
- 
'''

FULLSCREEN = True
DEBUG_MODE = True
SCALE_SPEED = 0.0003
INIT_DELTA_TIME = 5

game = Game(fullscreen=FULLSCREEN, debug_mode=DEBUG_MODE, scale_speed=SCALE_SPEED, init_delta_time=INIT_DELTA_TIME)
game.setup()
arcade.run()
