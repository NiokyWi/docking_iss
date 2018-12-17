import arcade
arcade.open_window(800,600,"Drawing Example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

color = (127, 0, 127, 127)
point_list = ((100, 100), \
              (200, 550),
              (400, 450),
              (500, 50))
arcade.draw_line(point_list, color, 3)
arcade.finish_render()
arcade.run()