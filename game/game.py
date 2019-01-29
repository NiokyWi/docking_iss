import arcade
from .atv import ATV
from .docking_system import DockingSystem
from .visor import Visor

DELTA_SPEED = 0.05
INIT_SCALE = 0.1

MOVEMENT_MULTIPLIER = 0.1
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
        self.visor = None
        self.debug = debug_mode

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
        self.visor = Visor(self.width, self.height)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.update_joystick()
        self.docking_system.update()
        self.atv.update()

    def update_joystick(self):
        if self.joystick:
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) > DEAD_ZONE:
                self.atv.change_x += self.joystick.x * MOVEMENT_MULTIPLIER
            if abs(self.joystick.y) > DEAD_ZONE:
                self.atv.change_y += self.joystick.y * MOVEMENT_MULTIPLIER

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.atv.draw()
        self.visor.draw()
        self.drawState()
        if self.debug:
            self.drawDebug()

    def drawDebug(self):
        arcade.draw_point(self.atv.target_pos_x, self.atv.target_pos_y, arcade.color.BLUE, 10)
        arcade.draw_circle_outline(self.atv.target_pos_x, self.atv.target_pos_y, self.atv.target_radius,
                                   arcade.color.BLUE, 5)
        scale, position, velocity, is_initialised, is_initialising, is_docking_complete, is_on_target = \
            self.docking_system.get_properties()
        arcade.draw_text("On target: " + str(is_on_target), 50, 95, arcade.color.WHITE, 12)
        arcade.draw_text("Initialised: " + str(is_initialised), 50, 80, arcade.color.WHITE, 12)
        arcade.draw_text("Initialising: " + str(is_initialising), 50, 65, arcade.color.WHITE, 12)
        arcade.draw_text("Docked: " + str(is_docking_complete), 50, 50, arcade.color.WHITE, 12)
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
        if key == arcade.key.UP:
            self.atv.change_y = self.atv.change_y + DELTA_SPEED
        elif key == arcade.key.DOWN:
            self.atv.change_y = self.atv.change_y - DELTA_SPEED
        elif key == arcade.key.LEFT:
            self.atv.change_x = self.atv.change_x - DELTA_SPEED
        elif key == arcade.key.RIGHT:
            self.atv.change_x = self.atv.change_x + DELTA_SPEED
        elif key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
