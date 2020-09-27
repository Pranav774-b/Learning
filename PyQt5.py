# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:57:04 2020

@author: PranavM
"""

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("tech With Tim")
    
    label=QtWidgets.QLabel(win)
    label.setText("This is awesome")
    label.move(50,50)
    
    
    win.show()
    sys.exit(app.exec_())

window()