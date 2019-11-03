import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(900, 900, 900, 900)
        self.setWindowTitle('Калькулятор')

        self.label = QLabel(self)
        self.label.setText('Введи знак операции(*, **,  /, //, %, %%, +, -)')

        self.label.move(365, 30)
        self.label2 = QLabel(self)
        self.label2.setText('Ниже знака введи два числа')
        self.label2.move(365, 50)

        self.sign = QLabel(self)
        self.sign.setText('Твой знак: ')
        self.sign.move(60, 170)

        self.name = QLineEdit(self)
        self.name.move(130, 170)

        self.label4 = QLabel(self)
        self.label4.setText('Число 1: ')
        self.label4.move(60, 220)

        self.name2 = QLineEdit(self)
        self.name2.move(130, 220)

        self.label5 = QLabel(self)
        self.label5.setText('Число 2: ')
        self.label5.move(60, 270)
        
        self.name3 = QLineEdit(self)
        self.name3.move(130, 270)
        
        self.label6 = QLabel(self)
        self.label6.setText('Справка:')
        self.label6.move(60, 325)

        self.label7 = QLabel(self)
        self.label7.setText('*  умножение')
        self.label7.move(60, 345)

        self.label7 = QLabel(self)
        self.label7.setText('**  возвести в степень')
        self.label7.move(60, 365)

        self.label8 = QLabel(self)
        self.label8.setText('/  деление')
        self.label8.move(60, 385)

        self.label9 = QLabel(self)
        self.label9.setText('//  деление нацело(отбрасывается дробная часть)')
        self.label9.move(60, 405)
        
        self.label8 = QLabel(self)
        self.label8.setText('%  деление c остатком')
        self.label8.move(60, 425)

        self.label9 = QLabel(self)
        self.label9.setText('%%  Процент от числа (Число 1 - Общее кол-во учеников; Число 2 - Выявление % успеваемости по кол-ву учеников)')
        self.label9.move(60, 450)
        

        self.button = QPushButton(self)
        self.button.resize(300, 150)
        self.button.move(300, 165)
        self.button.setText('OK')
        self.button.clicked.connect(self.calc)

        self.answd = QLabel(self)
        self.answd.move(365, 325)
        self.answd.setText('                                                                                                                                                       ')

    def calc(self):
        sing = self.name.text()
        number1 = self.name2.text()
        number2 = self.name3.text()
        if sing == '*':
            summ = float(number1) * float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '**':
            summ = float(number1) ** float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '/':
            summ = float(number1) / float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '//':
            summ = float(number1) // float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '%':
            summ = float(number1) % float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '+':
            summ = float(number1) + float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '-':
            summ = float(number1) - float(number2)
            self.answd.setText('Ответ: {}'.format(summ))
        elif sing == '%%':
            summ = (float(number2) * 100) / float(number1)
            self.answd.setText('Процент успеваемости : {} %'.format(summ))
        self.show()
        

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())
