# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from oneplayer_pong import main as one_pong
from twoplayer_pong import main as two_pong
from onehand_pong import main as hand_pong
import sys

class ScreenWindow(QtWidgets.QMainWindow):
    def __init__(self, screen, width, height):
        super().__init__()
        self.width = width
        self.height = height
        loadUi(screen, self)

        
    def set_dimensions(self):
        ScreenManager.widget.setFixedHeight(self.width)
        ScreenManager.widget.setFixedWidth(self.height)
        

class Screen1(ScreenWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__("/Users/kaustubhkarthik/Programs/pyqt_testing/screen_1.ui", 600, 800)
        self.button_setup()
    
    def button_setup(self):
        self.pushButton.clicked.connect(lambda: ScreenManager.change_screen("screen2"))



class Screen2(ScreenWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__("/Users/kaustubhkarthik/Programs/pyqt_testing/screen_2.ui", 247, 483)
        self.button_setup()
        
    def button_setup(self):
        self.back_button.clicked.connect(Screen2.go_back)
        self.play_button.clicked.connect(Screen2.play)
        self.settings_button.clicked.connect(Screen2.load_settings)
        
    def play():
        current_text = ScreenManager.screens["screen2"].select_mode.currentText()
        if current_text == "Classic - 1p":
            Screen2.load_game(one_pong)
        elif current_text == "Classic - 2p":
            Screen2.load_game(two_pong)
        elif current_text == "Hand Pong - 1p":
            Screen2.load_game(hand_pong)
        else:
            print("NOT WORKING")
        
    def load_game(game_folder):
        ScreenManager.get_screen().hide()
        game_folder.run()
        
    def go_back():
        ScreenManager.change_screen("screen1")
    
    def load_settings():
        ScreenManager.change_screen("screen3")
        
class Screen2_Settings(ScreenWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__("/Users/kaustubhkarthik/Programs/pyqt_testing/screen_2_settings.ui", 361, 569)
        self.button_setup()
        
    def button_setup(self):
        self.sliders = [self.ball_speed_slider, self.player_speed_slider, self.ball_size_slider, self.player_size_slider, self.rebound_y_slider,  self.bounce_acceleration_slider]
        self.back_button.clicked.connect(Screen2_Settings.go_back)
        self.save_button.clicked.connect(Screen2_Settings.save)
        
    def go_back():
        ScreenManager.change_screen("screen2")
    
    def save():
        pass
        
    
    

    

class ScreenManager(QtWidgets.QMainWindow):
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    screens = {}

    def setup(*all_screens):
        for i, screen in enumerate(all_screens):
            ScreenManager.screens.update({"screen" + str(i+1):screen})
            ScreenManager.widget.addWidget(screen)
            
    def get_screen():
        return ScreenManager.widget.currentWidget()

    def update_screen():
        current_screen = ScreenManager.get_screen()
        current_screen.set_dimensions()
        
    
    def show_screen():
        ScreenManager.update_screen()
        ScreenManager.widget.show()
        sys.exit(ScreenManager.app.exec_())
        
    def change_screen(screen_str):
        screen = ScreenManager.screens[screen_str]
        ScreenManager.widget.setCurrentWidget(screen)
        ScreenManager.update_screen()
        

if __name__ == "__main__":
    screen1 = Screen1()
    screen2 = Screen2()
    screen3 = Screen2_Settings()
    
    ScreenManager.setup(screen1, screen2, screen3)
    ScreenManager.show_screen()
    
