import sys

from PyQt5 import uic
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.verticalSlider.valueChanged.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_sqr(qp)
        qp.end()

    def draw_sqr(self, qp):
        qp.setPen(QColor(255, 0, 0))
        size = self.verticalSlider.value() / 100
        qp.drawEllipse(0, 0, 400 * size, 400 * size)
        qp.drawEllipse(size * 100 - 30 * size, size * 100 - 20 * size, 100 * size, 100 * size)
        qp.drawEllipse(size * 100 + 130 * size, size * 100 - 20 * size, 100 * size, 100 * size)
        startAngle = -30 * 16
        spanAngle = -120 * 16
        rect = QRectF(size * 100, size * 100 + 100 * size, 100 * size + 100 * size, 100 * size)
        qp.drawArc(rect, startAngle, spanAngle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
