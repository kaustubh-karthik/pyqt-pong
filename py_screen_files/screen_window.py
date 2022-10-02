from PyQt5 import QtWidgets
from py_screen_files.screen_manager import ScreenManager
from PyQt5.uic import loadUi


class ScreenWindow(QtWidgets.QMainWindow):
    def __init__(self, screen, width, height):
        super().__init__()
        self.width = width
        self.height = height
        loadUi(screen, self)

        
    def set_dimensions(self):
        ScreenManager.widget.setFixedHeight(self.width)
        ScreenManager.widget.setFixedWidth(self.height)
        