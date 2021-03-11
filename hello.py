import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(12,0,66))
        p.drawPolygon([QPoint(100,50),QPoint(100,100), QPoint(40,100),])

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(220,10,6))
        p.drawPolygon([QPoint(50,200),QPoint(100,100),QPoint(100,330),])

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())