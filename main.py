#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

app = QApplication(sys.argv)

class main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('interfaz/mainwindow.ui', self)

main = main()
main.show()

app.exec_()
