# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 243)
        MainWindow.setStyleSheet("background-color: rgb(0, 197, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select_mode = QtWidgets.QComboBox(self.centralwidget)
        self.select_mode.setGeometry(QtCore.QRect(70, 100, 121, 31))
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
        self.play_button.setGeometry(QtCore.QRect(290, 100, 100, 32))
        self.play_button.setStyleSheet("background-color: rgb(0, 255, 11);\n"
"color: rgb(86, 1, 255);")
        self.play_button.setObjectName("play_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 81, 16))
        self.label.setStyleSheet("color: rgb(0, 35, 255);")
        self.label.setObjectName("label")
        self.settings_button = QtWidgets.QToolButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(420, 10, 34, 34))
        self.settings_button.setStyleSheet("background-image:url(/Users/kaustubhkarthik/Programs/pyqt_testing/cog_wheel.png)")
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
import cog_wheel_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
