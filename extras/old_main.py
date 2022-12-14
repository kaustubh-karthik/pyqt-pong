from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from game_modes import oneplayer, twoplayer, onehand
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
        super().__init__("/Users/kaustubhkarthik/Programs/pyqt_testing/ui_files/screen_1.ui", 600, 800)
        self.button_setup()
    
    def button_setup(self):
        self.pushButton.clicked.connect(lambda: ScreenManager.change_screen("screen2"))



class Screen2(ScreenWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__("/Users/kaustubhkarthik/Programs/pyqt_testing/ui_files/screen_2.ui", 247, 483)
        self.button_setup()
        
    def button_setup(self):
        self.back_button.clicked.connect(Screen2.go_back)
        self.play_button.clicked.connect(Screen2.play)
        self.settings_button.clicked.connect(Screen2.load_settings_screen)
    
    def load_game(games, game_values):
        current_text = ScreenManager.screens["screen2"].select_mode.currentText()
        slider_variables = game_values['slider_values']
        spin_box_variables = game_values['spin_box_values']
        
        if current_text == "Classic - 1p":
            games[0].run(slider_variables, spin_box_variables)
        elif current_text == "Classic - 2p":
            games[1].run(slider_variables, spin_box_variables)
        elif current_text == "Hand Pong - 1p":
            games[2].run(slider_variables, spin_box_variables)
        else:
            print("NOT WORKING")
            return
        
        ScreenManager.get_screen().hide()
        
    def play():
        game_values = ScreenManager.screens["screen3"].get_values()
        games = [oneplayer, twoplayer, onehand]

        Screen2.load_game(games, game_values)
        
    def go_back():
        ScreenManager.change_screen("screen1")
    
    def load_settings_screen():
        ScreenManager.change_screen("screen3")
        
class Screen3(ScreenWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__("/Users/kaustubhkarthik/Programs/pyqt_testing/ui_files/screen_3.ui", 361, 569)
        self.key_values = Screen3.read_text_values()
        self.button_setup()
        self.slider_setup()
        self.spin_box_setup()
        
    def read_text_values():
        with open("game_settings.txt", "r") as settings:
            values = settings.readlines()
        return {line.split('=')[0]:[int(x) for x in eval(line.split('=')[1])] for line in values}
    
    def set_values(self, object_list, values):
        for i, value in enumerate(values):
            object_list[i].setValue(value)
            
    def get_values(self):
        return self.key_values
                   
    def slider_setup(self):
        self.sliders = [self.ball_speed_slider, self.player_speed_slider, self.ball_size_slider, self.player_size_slider, self.rebound_y_slider,  self.bounce_acceleration_slider]
        self.slider_connection_setup()
        self.set_values(self.sliders, self.key_values['slider_values'])
    
    def slider_connection_setup(self):
        self.sliders[0].valueChanged.connect(lambda: self.update_lcd(self.sliders[0], 0))
        self.sliders[1].valueChanged.connect(lambda: self.update_lcd(self.sliders[1], 1))
        self.sliders[2].valueChanged.connect(lambda: self.update_lcd(self.sliders[2], 2))
        self.sliders[3].valueChanged.connect(lambda: self.update_lcd(self.sliders[3], 3))
        self.sliders[4].valueChanged.connect(lambda: self.update_lcd(self.sliders[4], 4))
        self.sliders[5].valueChanged.connect(lambda: self.update_lcd(self.sliders[5], 5))
            
    def update_lcd(self, slider, lcd_index):
        lcds = [self.ball_speed_lcd, self.player_speed_lcd, self.ball_size_lcd, self.player_size_lcd, self.rebound_y_lcd, self.bounce_acceleration_lcd]
        lcds[lcd_index].display(slider.value())
        
        
    def spin_box_setup(self):
        self.spin_boxes = [self.player1_points_to_win, self.player2_points_to_win, self.player1_starting_points, self.player2_starting_points]
        self.set_values(self.spin_boxes, self.key_values['spin_box_values'])
        
    def button_setup(self):
        self.back_button.clicked.connect(self.go_back)
        self.save_button.clicked.connect(self.save)
        self.default_button.clicked.connect(self.reset_defaults)
        
    def reset_defaults(self):
        self.key_values['slider_values'] = [3, 5, 30, 140, 40, 0]
        self.key_values['spin_box_values'] = [7, 7, 0, 0]
        
        self.save_to_file()
        self.slider_setup()
        self.spin_box_setup()

    def go_back(self):
        ScreenManager.change_screen("screen2")
        
    def save(self):
        self.key_values['slider_values'] = [slider.value() for slider in self.sliders]
        self.key_values['spin_box_values'] = [spin_box.value() for spin_box in self.spin_boxes]
        
        self.save_to_file()
    
    def save_to_file(self):
        with open("game_settings.txt", "w") as settings:
            settings.write('slider_values=' + str(self.key_values['slider_values']))
            settings.write('\nspin_box_values=' + str(self.key_values['spin_box_values']))
    
    

    

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
    screen3 = Screen3()
    
    ScreenManager.setup(screen1, screen2, screen3)
    ScreenManager.show_screen()
    
