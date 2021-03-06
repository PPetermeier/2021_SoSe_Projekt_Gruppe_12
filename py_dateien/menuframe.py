# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Haushaltsplaner(object):
    def setupUi(self, Haushaltsplaner):
        Haushaltsplaner.setObjectName("Haushaltsplaner")
        Haushaltsplaner.resize(993, 617)
        Haushaltsplaner.setStyleSheet("background-color: white;")
        self.b_grocery = QtWidgets.QPushButton(Haushaltsplaner)
        self.b_grocery.setGeometry(QtCore.QRect(90, 120, 391, 221))
        self.b_grocery.setStyleSheet("background-image: url(:/Images/supermarket.jpg);\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"border-width: 1px;\n"
"border-color: black;")
        self.b_grocery.setText("")
        self.b_grocery.setObjectName("b_grocery")
        self.b_budget = QtWidgets.QPushButton(Haushaltsplaner)
        self.b_budget.setGeometry(QtCore.QRect(510, 120, 391, 221))
        self.b_budget.setAutoFillBackground(False)
        self.b_budget.setStyleSheet("background-image: url(:/Images/calculator.jpg);\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"border-width: 1px;\n"
"border-color: black;")
        self.b_budget.setText("")
        self.b_budget.setObjectName("b_budget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Haushaltsplaner)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 349, 811, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.l_einkaufsplaner = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_einkaufsplaner.setObjectName("l_einkaufsplaner")
        self.horizontalLayout.addWidget(self.l_einkaufsplaner)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.l_budgetplaner = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_budgetplaner.setObjectName("l_budgetplaner")
        self.horizontalLayout.addWidget(self.l_budgetplaner)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayoutWidget = QtWidgets.QWidget(Haushaltsplaner)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 30, 581, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_welcome = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.l_welcome.setObjectName("l_welcome")
        self.verticalLayout.addWidget(self.l_welcome)
        self.l_welcome2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_welcome2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_welcome2.setObjectName("l_welcome2")
        self.verticalLayout.addWidget(self.l_welcome2)
        self.l_icon = QtWidgets.QLabel(Haushaltsplaner)
        self.l_icon.setGeometry(QtCore.QRect(810, 40, 101, 61))
        self.l_icon.setStyleSheet("image: url(:/Images/logo_small_icon_only_inverted.png);")
        self.l_icon.setText("")
        self.l_icon.setObjectName("l_icon")
        self.b_logout = QtWidgets.QPushButton(Haushaltsplaner)
        self.b_logout.setGeometry(QtCore.QRect(440, 420, 111, 31))
        self.b_logout.setStyleSheet("background-color: red;\n"
"color: white;\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"border-width: 1px;\n"
"border-color: black;")
        self.b_logout.setObjectName("b_logout")

        self.retranslateUi(Haushaltsplaner)
        QtCore.QMetaObject.connectSlotsByName(Haushaltsplaner)

    def retranslateUi(self, Haushaltsplaner):
        _translate = QtCore.QCoreApplication.translate
        Haushaltsplaner.setWindowTitle(_translate("Haushaltsplaner", "Haushaltsplaner"))
        self.l_einkaufsplaner.setText(_translate("Haushaltsplaner", "Einkaufsplaner"))
        self.l_budgetplaner.setText(_translate("Haushaltsplaner", "Budgetplaner"))
        self.l_welcome.setText(_translate("Haushaltsplaner", "Herzlich Willkommen"))
        self.l_welcome2.setText(_translate("Haushaltsplaner", "Bitte w??hlen Sie eine Funktion"))
        self.b_logout.setText(_translate("Haushaltsplaner", "Logout"))
import menu_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Haushaltsplaner = QtWidgets.QWidget()
    ui = Ui_Haushaltsplaner()
    ui.setupUi(Haushaltsplaner)
    Haushaltsplaner.show()
    sys.exit(app.exec_())
