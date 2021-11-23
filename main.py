import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.update)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def draw(self):
        try:
            print('Принт')
            r = random.randrange(10, 20)

            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(self.x - r // 2, self.y - r // 2, r, r)


        except Exception as e:
            print(e)

    def paintEvent(self, event):
        try:
            self.x, self.y = random.randrange(200, 300), random.randrange(200, 300)
            print('paintEvent')
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
