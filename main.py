import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)

        self.db = sqlite3.connect('coffee.sqlite')
        self.cursor = self.db.cursor()

        result = self.cursor.execute(""" SELECT * FROM coffee_information """).fetchall()
        self.coffee_information.setColumnCount(len(result[0][1:]))
        self.coffee_information.setRowCount(len(result))
        for i, element in enumerate(result):
            for j, value in enumerate(element[1:]):
                self.coffee_information.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
