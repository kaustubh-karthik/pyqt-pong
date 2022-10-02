from PyQt5 import QtCore, QtWidgets
from py_screen_files.screen_manager import ScreenManager
from py_screen_files.screen_window import ScreenWindow
from game_modes import oneplayer, twoplayer, onehand


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 243)
        MainWindow.setStyleSheet("background-image:url(/Users/kaustubhkarthik/Programs/pyqt_testing/bg_images/pong_play.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select_mode = QtWidgets.QComboBox(self.centralwidget)
        self.select_mode.setGeometry(QtCore.QRect(180, 170, 121, 31))
        self.select_mode.setStyleSheet("background-color: rgb(255, 12, 0);\n"
"color: rgb(0, 26, 255);")
        self.select_mode.setEditable(False)
        self.select_mode.setIconSize(QtCore.QSize(16, 16))
        self.select_mode.setObjectName("select_mode")
        self.select_mode.addItem("")
        self.select_mode.addItem("")
        self.select_mode.addItem("")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.back_button.setStyleSheet("background-color: rgb(1, 50, 255);\n"
"color: rgb(255, 16, 0);")
        self.back_button.setObjectName("back_button")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(175, 110, 127, 32))
        self.play_button.setStyleSheet("background-color: rgb(0, 255, 11);\n"
"color: rgb(227, 255, 251);\n"
"")
        self.play_button.setObjectName("play_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 150, 81, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.settings_button = QtWidgets.QToolButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(420, 10, 34, 34))
        self.settings_button.setStyleSheet("background-image:url(/Users/kaustubhkarthik/Programs/pyqt_testing/bg_images/cog_wheel.png)")
        self.settings_button.setObjectName("settings_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_mode.setPlaceholderText(_translate("MainWindow", "Select Mode"))
        self.select_mode.setItemText(0, _translate("MainWindow", "Classic - 1p"))
        self.select_mode.setItemText(1, _translate("MainWindow", "Classic - 2p"))
        self.select_mode.setItemText(2, _translate("MainWindow", "Hand Pong - 1p"))
        self.back_button.setText(_translate("MainWindow", "BACK"))
        self.play_button.setText(_translate("MainWindow", "PLAY!"))
        self.label.setText(_translate("MainWindow", "Select Mode"))
        self.settings_button.setText(_translate("MainWindow", "..."))


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
        