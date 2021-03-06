# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grocerylistoverview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Groceryitemframe(object):

    gezeigte_liste = ""

    def setupUi(self, Einkaufsplaner):
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
        self.b_archive = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_archive.setStyleSheet("background-color: orange;\n"
"color: white;")
        self.b_archive.setObjectName("b_archive")
        self.horizontalLayout.addWidget(self.b_archive)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.l_app = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_app.setStyleSheet("font-size: 15pt;")
        self.l_app.setAlignment(QtCore.Qt.AlignCenter)
        self.l_app.setObjectName("l_app")
        self.horizontalLayout.addWidget(self.l_app)
        spacerItem1 = QtWidgets.QSpacerItem(60, 60, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.l_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_icon.setStyleSheet("image: url(:/Images/logo_small_icon_only_inverted.png);")
        self.l_icon.setText("")
        self.l_icon.setObjectName("l_icon")
        self.horizontalLayout.addWidget(self.l_icon)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.i_listname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.i_listname.setObjectName("i_listname")
        self.horizontalLayout_5.addWidget(self.i_listname)
        self.b_rename = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_rename.setObjectName("b_rename")
        self.horizontalLayout_5.addWidget(self.b_rename)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)

        #Wird nicht mehr ben??tigt

        # self.l_mount = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.l_mount.setStyleSheet("color: green;")
        # self.l_mount.setAlignment(QtCore.Qt.AlignCenter)
        # self.l_mount.setObjectName("l_mount")
        # self.horizontalLayout_6.addWidget(self.l_mount)
        # self.l_article = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.l_article.setStyleSheet("color: green;")
        # self.l_article.setAlignment(QtCore.Qt.AlignCenter)
        # self.l_article.setObjectName("l_article")
        # self.horizontalLayout_6.addWidget(self.l_article)
        # self.l_categorie = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.l_categorie.setStyleSheet("color: green;")
        # self.l_categorie.setAlignment(QtCore.Qt.AlignCenter)
        # self.l_categorie.setObjectName("l_categorie")
        # self.horizontalLayout_6.addWidget(self.l_categorie)


        spacerItem7 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)

        # ListWidget zu TableWidget ge??ndert
        self.listofflist = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.listofflist.setStyleSheet("font-size:12pt;")
        self.listofflist.setObjectName("listofflist")
        self.horizontalLayout_2.addWidget(self.listofflist)

        # Drei Spalten erstellt
        self.listofflist.setColumnCount(3)
        # Spalten f??llen Tabellen aus
        header = self.listofflist.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # Labels der Tabelle
        self.listofflist.setHorizontalHeaderLabels(["Menge", "Artikel", "Kategorie"])



        spacerItem9 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.i_amount = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.i_amount.setObjectName("i_amount")
        self.horizontalLayout_3.addWidget(self.i_amount)
        self.i_article = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.i_article.setObjectName("i_article")
        self.horizontalLayout_3.addWidget(self.i_article)
        self.i_categorie = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.i_categorie.setObjectName("i_categorie")
        self.horizontalLayout_3.addWidget(self.i_categorie)
        self.b_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_add.setObjectName("b_add")
        self.horizontalLayout_3.addWidget(self.b_add)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.b_itemdelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_itemdelete.setStyleSheet("background-color: grey;")
        self.b_itemdelete.setObjectName("b_itemdelete")
        self.horizontalLayout_7.addWidget(self.b_itemdelete)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Einkaufsplaner)
        QtCore.QMetaObject.connectSlotsByName(Einkaufsplaner)

    def retranslateUi(self, Einkaufsplaner):
        _translate = QtCore.QCoreApplication.translate
        Einkaufsplaner.setWindowTitle(_translate("Einkaufsplaner", "Haushaltsplaner"))
        self.b_back.setText(_translate("Einkaufsplaner", "Zur??ck"))
        self.b_archive.setText(_translate("Einkaufsplaner", "Archivieren"))
        self.l_app.setText(_translate("Einkaufsplaner", "Einkaufsplaner"))
        self.b_rename.setText(_translate("Einkaufsplaner", "umbenennen"))

        # wird nicht mehr ben??tigt

        # self.l_mount.setText(_translate("Einkaufsplaner", "Menge"))
        # self.l_article.setText(_translate("Einkaufsplaner", "Artikel"))
        # self.l_categorie.setText(_translate("Einkaufsplaner", "Kategorie"))


        self.b_add.setText(_translate("Einkaufsplaner", "+"))
        self.b_itemdelete.setText(_translate("Einkaufsplaner", "Element l??schen"))
import menu_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Einkaufsplaner = QtWidgets.QWidget()
    ui = Ui_Groceryitemframe()
    ui.setupUi(Einkaufsplaner)
    Einkaufsplaner.show()
    sys.exit(app.exec_())
