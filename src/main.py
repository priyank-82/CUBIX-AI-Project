from .cube.cube import Cube
from .cube.gui import Gui
from .p2.Cubeai import Cubeai

if __name__ == "__main__":
    cube = Cube(3)
    cube2 = Cubeai(3)
    gui = Gui(cube,cube2)
    gui.run()