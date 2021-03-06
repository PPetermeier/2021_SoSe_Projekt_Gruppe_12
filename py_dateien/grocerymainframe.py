# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groceryoverview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Logic


class Ui_Grocerymainframe(object):
    # Einkaufslisten wird in der main übergeben
    def setupUi(self, Einkaufsplaner):

        #print("frame triggert", Einkaufslisten)

        Einkaufsplaner.setObjectName("Einkaufsplaner")
        Einkaufsplaner.resize(965, 553)
        self.verticalLayoutWidget = QtWidgets.QWidget(Einkaufsplaner)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 921, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_back.setStyleSheet("background-color: grey;\n"
"color: white;")
        self.b_back.setObjectName("b_back")
        self.horizontalLayout.addWidget(self.b_back)
        self.b_archiv = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_archiv.setStyleSheet("background-color: orange;\n"
"color: white;")
        self.b_archiv.setObjectName("b_archiv")
        self.horizontalLayout.addWidget(self.b_archiv)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.l_app = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_app.setStyleSheet("font-size: 15pt;")
        self.l_app.setAlignment(QtCore.Qt.AlignCenter)
        self.l_app.setObjectName("l_app")
        self.horizontalLayout.addWidget(self.l_app)
        spacerItem1 = QtWidgets.QSpacerItem(60, 60, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.b_recipe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_recipe.setStyleSheet("background-color: orange;\n"
"color: white;")
        self.b_recipe.setObjectName("b_recipe")
        self.horizontalLayout.addWidget(self.b_recipe)
        self.l_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_icon.setStyleSheet("image: url(:/Images/logo_small_icon_only_inverted.png);")
        self.l_icon.setText("")
        self.l_icon.setObjectName("l_icon")
        self.horizontalLayout.addWidget(self.l_icon)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.l_function = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_function.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_function.setAlignment(QtCore.Qt.AlignCenter)
        self.l_function.setObjectName("l_function")
        self.verticalLayout.addWidget(self.l_function)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)


        self.listofflist = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listofflist.setStyleSheet("font-size:12pt;")
        self.listofflist.setObjectName("listofflist")

        self.horizontalLayout_2.addWidget(self.listofflist)
        spacerItem5 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)


        self.b_openlist = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_openlist.setStyleSheet("background-color: grey;\n"
"color: white;")
        self.b_openlist.setObjectName("b_openlist")
        self.horizontalLayout_3.addWidget(self.b_openlist)
        self.b_newlist = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_newlist.setStyleSheet("background-color: orange;\n"
"color: white;")
        self.b_newlist.setObjectName("b_newlist")
        self.horizontalLayout_3.addWidget(self.b_newlist)
        self.b_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_delete.setStyleSheet("background-color: grey;\n"
"color: white;")
        self.b_delete.setObjectName("b_delete")
        self.horizontalLayout_3.addWidget(self.b_delete)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Einkaufsplaner)
        QtCore.QMetaObject.connectSlotsByName(Einkaufsplaner)

    def retranslateUi(self, Einkaufsplaner):
        _translate = QtCore.QCoreApplication.translate
        Einkaufsplaner.setWindowTitle(_translate("Einkaufsplaner", "Haushaltsplaner"))
        self.b_back.setText(_translate("Einkaufsplaner", "Zurück"))
        self.b_archiv.setText(_translate("Einkaufsplaner", "Archiv"))
        self.l_app.setText(_translate("Einkaufsplaner", "Einkaufsplaner"))
        self.b_recipe.setText(_translate("Einkaufsplaner", "Rezepte"))
        self.l_function.setText(_translate("Einkaufsplaner", "Aktive Einkaufslisten"))
        __sortingEnabled = self.listofflist.isSortingEnabled()
        self.listofflist.setSortingEnabled(False)


        self.listofflist.setSortingEnabled(__sortingEnabled)
        self.b_openlist.setText(_translate("Einkaufsplaner", "Liste ansehen"))
        self.b_newlist.setText(_translate("Einkaufsplaner", "Neue Liste"))
        self.b_delete.setText(_translate("Einkaufsplaner", "Liste entfernen"))

import menu_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Einkaufsplaner = QtWidgets.QWidget()
    ui = Ui_Grocerymainframe()
    ui.setupUi(Einkaufsplaner)
    Einkaufsplaner.show()
    sys.exit(app.exec_())
