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


game = Game(fullscreen=False, debug_mode=True)
game.setup()
arcade.run()
