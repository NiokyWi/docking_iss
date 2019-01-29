import arcade


class Visor:
    """
    Class allow drawing the visor within the screen.

    draw method should be called before other sprite's draw methods in order to keep the visor above all.

    """

    def __init__(self, screen_width, screen_height) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (204, 85, 0)

    def draw(self):
        arcade.draw_line(self.screen_width / 2, 0,
                         self.screen_width / 2, self.screen_height,
                         self.color, 3)
        arcade.draw_line(0, self.screen_height / 2,
                         self.screen_width, self.screen_height/ 2,
                         self.color, 3)
