import arcade
from game.scaling_sprite import ScalingSprite
from game.visor import Visor

'''
TO DO list:
- set it fullscreen
- set a end game logig when the ATS is correctly docked
- set a reinitialisation when the ATS is crashed
- add perturbation in order to make sure the ATS doesn't go straight

BONUS:
- set difficulties levels
- 
'''

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.2

class DockingGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = False,
                 resizable: bool = False):
        super().__init__(width, height, title, fullscreen, resizable)
        arcade.set_background_color(arcade.color.AMAZON)
        self.ats = None
        self.visor = None

    def setup(self):
        # Set up your game here
        self.ats = ScalingSprite("../images/ats.png", SPRITE_SCALING,
                                 center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT/2)
        self.visor = Visor(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.ats.draw()
        self.visor.draw()

    def on_key_press(self, key, modifiers):
        delta_speed = 0.05
        v_x = self.ats._get_change_x()
        v_y = self.ats._get_change_y()
        if key == arcade.key.UP:
            self.ats.change_y = v_y + delta_speed
        elif key == arcade.key.DOWN:
            self.ats.change_y = v_y - delta_speed
        elif key == arcade.key.LEFT:
            self.ats.change_x = v_x - delta_speed
        elif key == arcade.key.RIGHT:
            self.ats.change_x = v_x + delta_speed
        elif key == arcade.key.A:
            self.ats.forward_push()
        elif key == arcade.key.Q:
            self.ats.backward_push()
        elif key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.ats.update()

def main():
    game = DockingGame(SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen=True)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()