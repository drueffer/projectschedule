import sys
import os
import arrow
from datetime import timedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from mycalendar import Calendar


class Example(QtWidgets.QWidget):
    def __init__(self):
        self.t0 = arrow.now()
        self.dt = timedelta(days=5)
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Draw text')
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)
        self.show()

    def wheelEvent(self, event):
        self.dt = self.dt * (1 + event.angleDelta().y()/1000.)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        qp.setRenderHint(qp.Antialiasing)
        font = QtGui.QFont('Decorative', 30)
        font.setPixelSize(20)
        qp.setFont(font)
        w = self.width()
        h = self.height()

        pen1 = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        pen1.setCosmetic(True)
        pen2 = QtGui.QPen(QtCore.Qt.gray, 1, QtCore.Qt.SolidLine)
        pen2.setCosmetic(True)
        lines = Calendar.get_lines(self.t0, self.dt)
        qp.setPen(pen1)
        for line in lines[0]:
            qp.drawLine(line[1]*w, 0., line[1]*w, h)
            qp.drawText(line[1]*w, 20., str(line[0]))
        qp.setPen(pen2)
        try:
            for line in lines[1]:
                qp.drawLine(line[1]*w, 0., line[1]*w, h)
                qp.drawText(line[1]*w, 40., str(line[0]))
        except IndexError:
            pass
        qp.end()



def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
