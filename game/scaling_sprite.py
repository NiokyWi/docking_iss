from arcade.sprite import Sprite


class ScalingSprite(Sprite):
    """
    Class extends Sprite class.

    This extend allows a scale control acting as a motion forward / backward along a 3rd dimension.

    """

    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0,
                 image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0,
                 repeat_count_x=1, repeat_count_y=1):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y,
                         repeat_count_x, repeat_count_y)
        self.velocity = [0, 0, 0]

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
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.scale += self.change_z
        self.angle += self.change_angle
        self.update_scale()
