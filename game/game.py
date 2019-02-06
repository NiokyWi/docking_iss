import arcade
from .atv import ATV
from .docking_system import DockingSystem
from .instruments import Instruments
import timeit

DELTA_SPEED = 0.05
INIT_SCALE = 0.05

MOVEMENT_MULTIPLIER = 0.05
DEAD_ZONE = 0.05


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = False,
                 resizable: bool = False, debug_mode=False, scale_speed=0.001, init_delta_time=10):
        super().__init__(width, height, title, fullscreen, resizable)
        arcade.set_background_color(arcade.color.BLACK)
        self.scale_speed = scale_speed
        self.init_delta_time = init_delta_time
        self.atv = None
        self.docking_system = None
        self.instruments = None
        self.debug = debug_mode
        self.time = timeit.default_timer()
        self.fps = None

        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no Joysticks")
            self.joystick = None

    def setup(self):
        # Set up your game here
        init_pos_x = self.width * 0.6
        init_pos_y = self.height * 0.6
        init_scale = INIT_SCALE
        self.atv = ATV(scale=init_scale, center_x=init_pos_x, center_y=init_pos_y)
        self.docking_system = DockingSystem(self, self.atv, init_scale, init_pos_x, init_pos_y, self.scale_speed,
                                            self.init_delta_time)
        self.instruments = Instruments(self.docking_system)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.update_fps()
        self.update_joystick()
        self.docking_system.update()
        self.atv.update()
        self.instruments.update()

    def update_fps(self):
        new_time = timeit.default_timer()
        self.fps = 1 / (new_time - self.time)
        self.time = new_time

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.atv.draw()
        self.instruments.draw()

    def update_joystick(self):
        if self.joystick:
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) > DEAD_ZONE:
                self.atv.acc_x = self.joystick.x * MOVEMENT_MULTIPLIER
            if abs(self.joystick.y) > DEAD_ZONE:
                self.atv.acc_y = - self.joystick.y * MOVEMENT_MULTIPLIER

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.atv.acc_y = DELTA_SPEED
        elif key == arcade.key.DOWN:
            self.atv.acc_y = - DELTA_SPEED
        elif key == arcade.key.LEFT:
            self.atv.acc_x = - DELTA_SPEED
        elif key == arcade.key.RIGHT:
            self.atv.acc_x = DELTA_SPEED
        elif key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
