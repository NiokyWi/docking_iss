import arcade
from .docking_system import DockingSystem


class Instruments:
    """
    Class allow drawing the visor within the screen.

    draw method should be called before other sprite's draw methods in order to keep the visor above all.

    """

    def __init__(self, docking_system: DockingSystem) -> None:
        self.docking_system = docking_system
        self.color = (204, 85, 0)

    def update(self):
        pass

    def draw(self):
        self.draw_visor()

    def draw_visor(self):
        arcade.draw_line(self.docking_system.window.width / 2, 0,
                         self.docking_system.window.width / 2, self.docking_system.window.height,
                         self.color, 3)
        arcade.draw_line(0, self.docking_system.window.height / 2,
                         self.docking_system.window.width, self.docking_system.window.height/2,
                         self.color, 3)
