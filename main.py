import arcade
from game.game import Game

'''
TO DO list:
- push key -> jet (not only one)
- set a end game logic when the ATS is correctly docked
- set a reinitialisation when the ATS is crashed
- add perturbation in order to make sure the ATS doesn't go straight

BONUS:
- set difficulties levels
- 
'''


game = Game(fullscreen=False)
game.setup()
arcade.run()