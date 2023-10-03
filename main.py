
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from operator import add, sub, mul, truediv
from typing import Union, Optional
from design import Ui_MainWindow

operations = {
    '+': add,
    '-': sub,
    'x': mul,
    '/': truediv

}

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Цифри
        self.ui.button_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.button_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.button_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.button_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.button_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.button_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.button_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.button_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.button_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.button_9.clicked.connect(lambda: self.add_digit('9'))
        #Дії
        self.ui.button_clear.clicked.connect(lambda: self.clear_all())
        self.ui.button_CE.clicked.connect(lambda: self.clear_edit())
        self.ui.button_point.clicked.connect(lambda: self.add_point())
        self.ui.button_neg.clicked.connect(lambda: self.negate())
        self.ui.button_erase.clicked.connect(lambda: self.backspace())
        #Математика
        self.ui.button_calc.clicked.connect(lambda: self.calculate())
        self.ui.button_add.clicked.connect(lambda: self.math_operation(' + '))
        self.ui.button_sub.clicked.connect(lambda: self.math_operation(' - '))
        self.ui.button_mul.clicked.connect(lambda: self.math_operation(' x '))
        self.ui.button_div.clicked.connect(lambda: self.math_operation(' / '))

    def add_digit(self,btn_text: str) -> None:
        if self.ui.Edit_entry.text() == '0':
            self.ui.Edit_entry.setText(btn_text)
        else:
            self.ui.Edit_entry.setText(self.ui.Edit_entry.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.Edit_entry.setText('0')
        self.ui.label_temp.clear()
    def clear_edit(self) -> None:
        self.ui.Edit_entry.setText('0')

    def add_point(self) -> None:
        if '.' not in self.ui.Edit_entry.text():
            self.ui.Edit_entry.setText(self.ui.Edit_entry.text() + '.')



    def add_temp(self, math_sign: str):
        if not self.ui.label_temp.text() and self.ui.Edit_entry.text() != '0' or self.get_math_sign() == "=":
            self.ui.label_temp.setText(self.remove_trailing_zeros(self.ui.Edit_entry.text()) + f'{math_sign}')
            self.ui.Edit_entry.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def get_entry_num(self) -> Union[int,float]:
       entry = self.ui.Edit_entry.text().strip('.')
       return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.label_temp.text():
            temp = self.ui.label_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)
    def get_math_sign(self) -> Optional[str]:
        if self.ui.label_temp.text():
            return self.ui.label_temp.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.Edit_entry.text()
        temp = self.ui.label_temp.text()

        if temp and entry != '0':
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
            )
            self.ui.label_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
            self.ui.Edit_entry.setText(result)

            return result

    def math_operation(self, math_sign: str):
        temp = self.ui.label_temp.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.label_temp.setText(temp[:-3] + f'{math_sign}')
            else:
                self.ui.label_temp.setText(self.calculate() + f'{math_sign}')

    def negate(self):
        entry = self.ui.Edit_entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        self.ui.Edit_entry.setText(entry)

    def backspace(self) -> None:
        entry = self.ui.Edit_entry.text()
        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.Edit_entry.setText('0')
            else:
                self.ui.Edit_entry.setText(entry[:-1])
        else:
            self.ui.Edit_entry.setText('0')

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Calculator()
    window.show()
    sys.exit(app.exec())

