import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import mouse
import pickle
import time


class Main(QWidget):
    def __init__(self):
        super().__init__()
        if not os.path.exists('log.csv'):
            with open('log.csv', 'w') as f:
                f.close()
        self.project_name = '1'
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Запись', self)
        self.btn.clicked.connect(self.record)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(5, 5)

        self.btn1 = QPushButton('Воспроизвести', self)
        self.btn1.clicked.connect(self.play)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(85, 5)

        self.btn2 = QPushButton('Помошь', self)
        self.btn2.clicked.connect(self.help)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(173, 5)

        self.name_label = QLabel(self)
        self.name_label.setText("Введите название:")
        self.name_label.move(5, 90)

        self.name_input = QLineEdit(self)
        self.name_input.move(105, 90)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('АВТОКЛИКЕР')
        self.show()

    def record(self):
        self.project_name = self.name_input.text()
        f = open(self.project_name + '.pkl', 'wb')
        s = mouse.record()
        mouse.unhook_all()
        pickle.dump(s, f)
        f.close()

    def play(self):
        try:
            self.project_name = self.name_input.text()
            with open('log.csv', 'a') as f:
                f.write(self.project_name + ' ' + str(time.time()) + '\n')
            f = open(self.project_name + '.pkl', 'rb')
            mouse.play(pickle.load(f))
            f.close()
        except:
            pass

    def help(self):
        self.second_form = SecondForm()
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Помощь')
        self.lbl = QLabel('''Введите в поле название для текущего сохранения. 

Нажав на кнопку запись, 
выполните необходимые действия для автоматизации.

После нажатия правой кнопкой мыши, запись прекратиться.

После нажатия на кнопку воспроизвести,
выбранная запись будет запущена.''', self)
        font = QFont()
        font.setPointSize(16)
        self.lbl.setFont(font)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
