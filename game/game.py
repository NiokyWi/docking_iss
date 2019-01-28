import arcade
from .atv import ATV
from .docking_system import DockingSystem
from game.visor import Visor

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = False,
                 resizable: bool = False):
        super().__init__(width, height, title, fullscreen, resizable)
        arcade.set_background_color(arcade.color.BLACK)
        self.atv = None
        self.docking_system = None
        self.visor = None
        self.debug = True

    def setup(self):
        # Set up your game here
        init_pos_x = self.width * 0.6
        init_pos_y = self.height * 0.6
        init_scale = 0.1
        self.atv = ATV(scale =init_scale, center_x=init_pos_x, center_y=init_pos_y)
        self.docking_system = DockingSystem(self, self.atv, init_scale, init_pos_x, init_pos_y)
        self.visor = Visor(self.width, self.height)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.docking_system.update()
        self.atv.update()

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.atv.draw()
        arcade.draw_point(self.atv.target_pos_x, self.atv.target_pos_y, arcade.color.BLUE, 10)
        self.visor.draw()
        self.drawDebug()
        self.drawState()

    def drawDebug(self):
        if self.debug:
            scale, position, velocity, is_initialised, is_initialising, is_dock, is_on_target = self.docking_system.get_properties()
            arcade.draw_text("On target: " + str(is_on_target), 50, 95, arcade.color.WHITE, 12)
            arcade.draw_text("Initialised: " + str(is_initialised), 50, 80, arcade.color.WHITE, 12)
            arcade.draw_text("Initialising: " + str(is_initialising), 50, 65, arcade.color.WHITE, 12)
            arcade.draw_text("Docked: " + str(is_dock), 50, 50, arcade.color.WHITE, 12)
            arcade.draw_text("Scale: " + str(scale), 50, 35, arcade.color.WHITE, 12)
            arcade.draw_text("Position: " + str(position), 50, 20, arcade.color.WHITE, 12)

    def drawState(self):
        _, _, _, _, is_initialising, is_dock, _ = self.docking_system.get_properties()
        if is_initialising:
            arcade.draw_text("INITIALIZING", self.width/2, self.height / 2,
                             arcade.color.RED, 50, align='center',
                             anchor_x='center', anchor_y='center', rotation=0)
        if is_dock:
            arcade.draw_text("DOCKING COMPLETE", self.width/2, self.height / 2,
                             arcade.color.GREEN, 50, align='center',
                             anchor_x='center', anchor_y='center', rotation=0)

    def on_key_press(self, key, modifiers):
        delta_speed = 0.05
        if key == arcade.key.UP:
            self.atv.change_y = self.atv.change_y + delta_speed
        elif key == arcade.key.DOWN:
            self.atv.change_y = self.atv.change_y - delta_speed
        elif key == arcade.key.LEFT:
            self.atv.change_x = self.atv.change_x - delta_speed
        elif key == arcade.key.RIGHT:
            self.atv.change_x = self.atv.change_x + delta_speed
        elif key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
