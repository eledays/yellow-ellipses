import sys
import random
import io

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QComboBox, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 600, 600)

        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.click)

        self.ellipses = []

    def click(self):
        self.ellipses.append([random.randint(0, 600), random.randint(0, 600), random.randint(10, 100), random.randint(10, 100)])
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        while self.ellipses:
            args = self.ellipses.pop()
            qp.drawEllipse(*args)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
