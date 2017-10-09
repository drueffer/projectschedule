import sys
import os
import arrow
from datetime import timedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from calendar import Calendar


class Example(QtWidgets.QWidget):
    def __init__(self):
        self.t0 = arrow.now()
        self.dt = timedelta(days=12)
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.text = u'abc'
        self.setWindowTitle('Draw text')
        self.show()

    def wheelEvent(self, event):
        self.dt = self.dt * (1 + event.angleDelta().y()/1000.)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        qp.setRenderHint(qp.Antialiasing)
        qp.scale(self.width()/100.0, self.height()/100.0)
        self.drawText(event, qp)

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        pen.setCosmetic(True)
        qp.setPen(pen)
        for line in Calendar.get_lines(self.t0, self.dt):
            qp.drawLine(line*100, 0, line*100, 100)

        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
