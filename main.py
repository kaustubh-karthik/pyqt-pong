from py_screen_files import py_screen1, py_screen2, py_screen3, screen_manager
if __name__ == "__main__":
    screenManager = screen_manager.ScreenManager
    screen1 = py_screen1.Screen1()
    screen2 = py_screen2.Screen2()
    screen3 = py_screen3.Screen3()
    
    screenManager.setup(screen1, screen2, screen3)
    screenManager.show_screen()