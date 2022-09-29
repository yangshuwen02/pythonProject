from Pyqt5.Qtgui import *
from Pyqt5.QtCore import *
from Pyqt5.QtWidgets import *

class MyButton(QLabel):
    click_signal=pyqtSignal()#定义一个信号
