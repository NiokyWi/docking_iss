from arcade.sprite import Sprite

ATV_IMG_WIDTH = 8822
ATV_IMG_HEIGHT = 5881
TARGET_IMG_POS_X = 4832
TARGET_IMG_POS_Y = 2391
XY_TOL = 10
SCALE_TOL = 0.01
DOCKING_SCALE = 1
LIMIT_POS_X = 0
LIMIT_POS_Y = 0
INIT_DELTA_TIME = 200

class ScalingSprite(Sprite):
    """
    Class extends Sprite class.

    This extend allows a scale control acting as a motion forward / backward along a 3rd dimension.

    """

    def __init__(self, arcade_window, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0,
                 image_width: float = 0, image_height: float = 0, repeat_count_x=1, repeat_count_y=1):
        self.arcade_window = arcade_window
        self.init_pos_x = self.arcade_window.width * 0.5
        self.init_pos_y = self.arcade_window.height * 0.5
        self.docking_pos_x = self.arcade_window.width / 2
        self.docking_pos_y = self.arcade_window.height / 2
        self.init_scale = scale
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, self.init_pos_x, self.init_pos_y,
                         repeat_count_x, repeat_count_y)
        self.initialized = True
        self.velocity = [0, 0, 0]
        self.isInitialising = False
        self.isDock = False

    def _get_change_z(self) -> float:
        """ Get the velocity in the for-aft axis of the sprite. """
        return self.velocity[2]

    def _set_change_z(self, new_value: float):
        """ Set the velocity in the for-aft axis of the sprite. """
        self.velocity[2] = new_value

    change_z = property(_get_change_z, _set_change_z)

    def update_scale(self):
        """
        Change sprite scale acting as a 3rd dimension motion.
        """
        self.width = self.texture.width * self.scale
        self.height = self.texture.height * self.scale

    def update(self):
        """
        Update the sprite.
        """
        self.checkPosition()
        self.update_forward_motion()
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.scale += self.change_z
        self.angle += self.change_angle
        self.update_scale()

    def update_forward_motion(self):
        if self.initialized and (self.change_x != 0 or self.change_y != 0):
            self.initialized = False
            self.change_z = 0.0001

    def checkPosition(self):
        if self.isInitialising:
            if ((self.center_x < self.init_pos_x + XY_TOL) and (self.center_x > self.init_pos_x - XY_TOL)
                    and (self.center_y < self.init_pos_y + XY_TOL) and (self.center_y > self.init_pos_y - XY_TOL)
                    and (self.scale < self.init_scale + SCALE_TOL)):
                self.isInitialising = False
                self.initialized = True
                self.stop()
        if ((self.center_x < self.docking_pos_x + XY_TOL) and (self.center_x > self.docking_pos_x - XY_TOL)
                and (self.center_y < self.docking_pos_y + XY_TOL) and (self.center_y > self.docking_pos_y - XY_TOL)
                and (self.scale > DOCKING_SCALE)):
            self.isDock = True
        elif (self.center_x < 0) or (self.center_x > self.width) \
                or (self.center_y < 0) or (self.center_y > self.height) \
                or (self.scale > DOCKING_SCALE):
            self.reinitialisation()
        if self.isDock:
            self.stop()

    def stop(self):
        self.change_x, self.change_y, self.change_z = 0, 0, 0

    def reinitialisation(self):
        self.isInitialising = True
        self.change_x = (self.init_pos_x - self.center_x) / INIT_DELTA_TIME
        self.change_y = (self.init_pos_y - self.center_y) / INIT_DELTA_TIME
        self.change_z = (self.init_scale - self.scale) / INIT_DELTA_TIME

    def getProperties(self):
        return self.scale, self.position, self.velocity, self.isInitialising, self.isDock
