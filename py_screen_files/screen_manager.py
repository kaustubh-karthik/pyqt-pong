from PyQt5 import QtWidgets
import sys


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
        
