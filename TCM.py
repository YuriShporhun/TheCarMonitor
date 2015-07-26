#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Yuri Shporhun'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.PyUi.MainWindow import Ui_MainWindow
from gui.Handlers.MainWindowHandlers import MainWindowHandler


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_handlers(MainWindowHandler.get_handler())

    def set_handlers(self, handler):
        self.ui.actionPobedaauto_ru.triggered.connect(handler['pobeda_auto_clicked'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
