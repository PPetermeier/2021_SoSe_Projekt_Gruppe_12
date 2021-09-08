from loginframe import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class LoginWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()

