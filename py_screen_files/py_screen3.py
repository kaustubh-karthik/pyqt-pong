from PyQt5 import QtCore, QtWidgets
from py_screen_files.screen_manager import ScreenManager
from py_screen_files.screen_window import ScreenWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ball_speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.ball_speed_slider.setGeometry(QtCore.QRect(150, 100, 351, 25))
        self.ball_speed_slider.setMinimum(1)
        self.ball_speed_slider.setMaximum(30)
        self.ball_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ball_speed_slider.setObjectName("ball_speed_slider")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.back_button.setObjectName("back_button")
        self.ball_speed = QtWidgets.QLabel(self.centralwidget)
        self.ball_speed.setGeometry(QtCore.QRect(40, 100, 71, 16))
        self.ball_speed.setObjectName("ball_speed")
        self.player_speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.player_speed_slider.setGeometry(QtCore.QRect(150, 140, 351, 25))
        self.player_speed_slider.setMaximum(30)
        self.player_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.player_speed_slider.setObjectName("player_speed_slider")
        self.player_speed = QtWidgets.QLabel(self.centralwidget)
        self.player_speed.setGeometry(QtCore.QRect(40, 140, 81, 20))
        self.player_speed.setObjectName("player_speed")
        self.bounce_acceleration_slider = QtWidgets.QSlider(self.centralwidget)
        self.bounce_acceleration_slider.setGeometry(QtCore.QRect(150, 300, 351, 25))
        self.bounce_acceleration_slider.setMinimum(0)
        self.bounce_acceleration_slider.setMaximum(50)
        self.bounce_acceleration_slider.setSingleStep(1)
        self.bounce_acceleration_slider.setProperty("value", 0)
        self.bounce_acceleration_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bounce_acceleration_slider.setObjectName("bounce_acceleration_slider")
        self.ball_size_slider = QtWidgets.QSlider(self.centralwidget)
        self.ball_size_slider.setGeometry(QtCore.QRect(150, 180, 351, 25))
        self.ball_size_slider.setMinimum(0)
        self.ball_size_slider.setMaximum(150)
        self.ball_size_slider.setProperty("value", 0)
        self.ball_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ball_size_slider.setObjectName("ball_size_slider")
        self.player_size_slider = QtWidgets.QSlider(self.centralwidget)
        self.player_size_slider.setGeometry(QtCore.QRect(150, 220, 351, 25))
        self.player_size_slider.setMaximum(500)
        self.player_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.player_size_slider.setObjectName("player_size_slider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(165, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.player1_points_to_win = QtWidgets.QSpinBox(self.centralwidget)
        self.player1_points_to_win.setGeometry(QtCore.QRect(140, 60, 51, 21))
        self.player1_points_to_win.setObjectName("player1_points_to_win")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 40, 61, 16))
        self.label_3.setStyleSheet("color: rgb(0, 15, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 40, 61, 16))
        self.label_4.setStyleSheet("color: rgb(255, 0, 4);")
        self.label_4.setObjectName("label_4")
        self.player2_points_to_win = QtWidgets.QSpinBox(self.centralwidget)
        self.player2_points_to_win.setGeometry(QtCore.QRect(230, 60, 42, 22))
        self.player2_points_to_win.setObjectName("player2_points_to_win")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 20, 101, 16))
        self.label_5.setObjectName("label_5")
        self.player2_starting_points = QtWidgets.QSpinBox(self.centralwidget)
        self.player2_starting_points.setGeometry(QtCore.QRect(410, 60, 42, 22))
        self.player2_starting_points.setObjectName("player2_starting_points")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 40, 61, 16))
        self.label_6.setStyleSheet("color: rgb(0, 15, 255);")
        self.label_6.setObjectName("label_6")
        self.player1_starting_points = QtWidgets.QSpinBox(self.centralwidget)
        self.player1_starting_points.setGeometry(QtCore.QRect(320, 60, 51, 21))
        self.player1_starting_points.setObjectName("player1_starting_points")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 40, 61, 16))
        self.label_7.setStyleSheet("color: rgb(255, 0, 4);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 180, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 220, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 300, 81, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 300, 131, 16))
        self.label_11.setObjectName("label_11")
        self.rebound_y_slider = QtWidgets.QSlider(self.centralwidget)
        self.rebound_y_slider.setGeometry(QtCore.QRect(150, 260, 351, 25))
        self.rebound_y_slider.setMinimum(0)
        self.rebound_y_slider.setMaximum(150)
        self.rebound_y_slider.setProperty("value", 0)
        self.rebound_y_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rebound_y_slider.setObjectName("rebound_y_slider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 121, 16))
        self.label.setObjectName("label")
        self.ball_speed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.ball_speed_lcd.setGeometry(QtCore.QRect(510, 95, 41, 31))
        self.ball_speed_lcd.setDigitCount(3)
        self.ball_speed_lcd.setObjectName("ball_speed_lcd")
        self.player_speed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.player_speed_lcd.setGeometry(QtCore.QRect(510, 135, 41, 31))
        self.player_speed_lcd.setDigitCount(3)
        self.player_speed_lcd.setObjectName("player_speed_lcd")
        self.ball_size_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.ball_size_lcd.setGeometry(QtCore.QRect(510, 175, 41, 31))
        self.ball_size_lcd.setDigitCount(3)
        self.ball_size_lcd.setObjectName("ball_size_lcd")
        self.player_size_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.player_size_lcd.setGeometry(QtCore.QRect(510, 215, 41, 31))
        self.player_size_lcd.setDigitCount(3)
        self.player_size_lcd.setObjectName("player_size_lcd")
        self.rebound_y_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.rebound_y_lcd.setGeometry(QtCore.QRect(510, 255, 41, 31))
        self.rebound_y_lcd.setDigitCount(3)
        self.rebound_y_lcd.setObjectName("rebound_y_lcd")
        self.bounce_acceleration_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.bounce_acceleration_lcd.setGeometry(QtCore.QRect(510, 295, 41, 31))
        self.bounce_acceleration_lcd.setDigitCount(3)
        self.bounce_acceleration_lcd.setObjectName("bounce_acceleration_lcd")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(495, 10, 61, 31))
        self.save_button.setObjectName("save_button")
        self.default_button = QtWidgets.QPushButton(self.centralwidget)
        self.default_button.setGeometry(QtCore.QRect(10, 40, 71, 41))
        self.default_button.setObjectName("default_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_button.setText(_translate("MainWindow", "BACK"))
        self.ball_speed.setText(_translate("MainWindow", "Ball Speed"))
        self.player_speed.setText(_translate("MainWindow", "Player Speed"))
        self.label_2.setText(_translate("MainWindow", "Points To Win"))
        self.label_3.setText(_translate("MainWindow", "Player 1"))
        self.label_4.setText(_translate("MainWindow", "Player 2"))
        self.label_5.setText(_translate("MainWindow", "Starting Points"))
        self.label_6.setText(_translate("MainWindow", "Player 1"))
        self.label_7.setText(_translate("MainWindow", "Player 2"))
        self.label_8.setText(_translate("MainWindow", "Ball Size"))
        self.label_9.setText(_translate("MainWindow", "Player Size"))
        self.label_11.setText(_translate("MainWindow", "Bounce Acceleration"))
        self.label.setText(_translate("MainWindow", "Rebound Y Factor"))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.default_button.setText(_translate("MainWindow", "Default"))


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
