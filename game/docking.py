import arcade
from game.scaling_sprite import ScalingSprite
from game.visor import Visor

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.1


class DockingGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = False,
                 resizable: bool = False):
        super().__init__(width, height, title, fullscreen, resizable)
        arcade.set_background_color(arcade.color.AMAZON)
        self.atv = None
        self.visor = None
        self.debug = True

    def setup(self):
        # Set up your game here
        self.atv = ScalingSprite(self, "./game/images/ats.png", scale=SPRITE_SCALING)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.atv.draw()
        self.visor.draw()
        self.drawDebug()
        self.drawState()

    def drawDebug(self):
        if self.debug:
            scale, position, velocity, initialising, dock = self.atv.getProperties()
            arcade.draw_text(str(position), 50, 50, arcade.color.WHITE, 12)
            arcade.draw_text(str(initialising), 50, 35, arcade.color.WHITE, 12)
            arcade.draw_text(str(dock), 50, 20, arcade.color.WHITE, 12)

    def drawState(self):
        _, _, _, initialising, dock = self.atv.getProperties()
        if initialising:
            arcade.draw_text("INITIALIZING", self.width/2, self.height / 2,
                             arcade.color.RED, 50, align='center',
                             anchor_x='center', anchor_y='center', rotation=0)
        if dock:
            arcade.draw_text("DOCKING COMPLETE", self.width/2, self.height / 2,
                             arcade.color.GREEN, 50, align='center',
                             anchor_x='center', anchor_y='center', rotation=0)

    def on_key_press(self, key, modifiers):
        xy_delta_speed = 0.05
        z_delta_speed = 0.00005

        if key == arcade.key.UP:
            self.atv.change_y = self.atv.change_y + xy_delta_speed
        elif key == arcade.key.DOWN:
            self.atv.change_y = self.atv.change_y - xy_delta_speed
        elif key == arcade.key.LEFT:
            self.atv.change_x = self.atv.change_x - xy_delta_speed
        elif key == arcade.key.RIGHT:
            self.atv.change_x = self.atv.change_x + xy_delta_speed
        # elif key == arcade.key.A:
        #     self.atv.change_z = self.atv.change_z + z_delta_speed
        # elif key == arcade.key.Q:
        #     self.atv.change_z = self.atv.change_z - z_delta_speed
        elif key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)
            # self.set_fullscreen(not self.fullscreen, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            # width, height = self.get_size()
            # self.set_viewport(0, width, 0, height)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.atv.update()
        self.visor = Visor(self.width, self.height)
