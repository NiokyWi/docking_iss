import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        SPRITE_SCALING_COIN = 1
        self.iss = arcade.Sprite("images/iss2.jpg", SPRITE_SCALING_COIN)
        self.iss.center_x = 300 # Starting position
        self.iss.center_y = 300

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.iss.draw()

        # Finish drawing and display the result
        arcade.finish_render()

    def on_key_press(self, key, modifiers):
        SPEED = 1
        v_x = self.iss._get_change_x()
        v_y = self.iss._get_change_y()
        x, y = self.iss.get_position()
        if key == arcade.key.UP:
            self.iss.change_y = v_y + SPEED
        elif key == arcade.key.DOWN:
            self.iss.change_y = v_y - SPEED
        elif key == arcade.key.LEFT:
            self.iss.change_x = v_x - SPEED
        elif key == arcade.key.RIGHT:
            self.iss.change_x = v_x + SPEED

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.iss.update()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()