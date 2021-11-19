from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint
from UI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.setGeometry(400, 400, 400, 400)
        self.draw_now = False

        self.circles_button.clicked.connect(self.redraw)

    def redraw(self):
        self.draw_now = True
        self.repaint()

    def paintEvent(self, e):
        if self.draw_now:
            painter = QPainter()
            painter.begin(self)
            self.draw_circles(painter)
            self.draw_now = False
            painter.end()

    def draw_circles(self, painter):
        x, y = self.size().width(), self.size().height()
        for _ in range(randint(5, 15)):
            painter.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
            new_x, new_y = randint(0, x - 30), randint(0, y - 30)
            size = randint(1, 30)
            painter.drawEllipse(new_x, new_y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
