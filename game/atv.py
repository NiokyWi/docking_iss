from .scaling_sprite import ScalingSprite

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


class ATV(ScalingSprite):

    def __init__(self, arcade_window, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0,
                 image_width: float = 0, image_height: float = 0, repeat_count_x=1, repeat_count_y=1):
        super().__init__(arcade_window, filename, scale, image_x, image_y, image_width, image_height, repeat_count_x,
                         repeat_count_y)

    def checkPosition(self):
        if self.isDocked():
            self.dock()
        elif self.isInitialising:
            if self.isInitialized():
                self.isInitialising = False
                self.initialized = True
                self.stop()
        elif self.requiresReinitialisation():
            self.reinitialisation()

    def isInitialized(self):
        return ((self.center_x < self.docking_pos_x + XY_TOL) and (self.center_x > self.docking_pos_x - XY_TOL)
                and (self.center_y < self.docking_pos_y + XY_TOL) and (self.center_y > self.docking_pos_y - XY_TOL)
                and (self.scale > DOCKING_SCALE))

    def isDocked(self):
        return ((self.center_x < self.docking_pos_x + XY_TOL) and (self.center_x > self.docking_pos_x - XY_TOL)
                and (self.center_y < self.docking_pos_y + XY_TOL) and (self.center_y > self.docking_pos_y - XY_TOL)
                and (self.scale > DOCKING_SCALE))

    def requiresReinitialisation(self):
        return (self.center_x < 0) or (self.center_x > self.arcade_window.width) \
               or (self.center_y < 0) or (self.center_y > self.arcade_window.height) \
               or (self.scale > DOCKING_SCALE)

    def dock(self):
        self.stop()
        self.isDock = True

    def stop(self):
        self.change_x, self.change_y, self.change_z = 0, 0, 0

    def reinitialisation(self):
        self.isInitialising = True
        self.change_x = (self.init_pos_x - self.center_x) / INIT_DELTA_TIME
        self.change_y = (self.init_pos_y - self.center_y) / INIT_DELTA_TIME
        self.change_z = (self.init_scale - self.scale) / INIT_DELTA_TIME

    def getProperties(self):
        return self.scale, self.position, self.velocity, self.isInitialising, self.isDock
