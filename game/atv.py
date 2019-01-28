from .scaling_sprite import ScalingSprite

ATV_IMG_WIDTH = 8822
ATV_IMG_HEIGHT = 5881
TARGET_IMG_POS_X = 4832
TARGET_IMG_POS_Y = 2391


class ATV(ScalingSprite):

    def __init__(self, scale: float = 1, center_x: float = 0, center_y: float = 0):
        filename="./game/images/ats.png"
        super().__init__(filename, scale, center_x, center_y)

    @property
    def target_pos_x(self):
        return self.center_x

    @property
    def target_pos_y(self):
        return self.center_y

    @property
    def target_radius(self):
        return 80 * self.scale

    def stop(self):
        self.change_x, self.change_y, self.change_z = 0, 0, 0

    def reinitialisation(self, scale, x, y, time):
        self.change_x = (x - self.center_x) / time
        self.change_y = (y - self.center_y) / time
        self.change_z = (scale - self.scale) / time
