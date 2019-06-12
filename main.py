from window import Window
from Automat import Automat

controller = Automat()
view = Window(controller)

view.start()
