# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archivelistframe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ArchivelistFrame(object):
    def setupUi(self, ArchivelistFrame):
        ArchivelistFrame.setObjectName("ArchivelistFrame")
        ArchivelistFrame.resize(965, 482)
        self.verticalLayoutWidget = QtWidgets.QWidget(ArchivelistFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 921, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.l_app = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_app.setStyleSheet("font-size: 15pt;")
        self.l_app.setAlignment(QtCore.Qt.AlignCenter)
        self.l_app.setObjectName("l_app")
        self.horizontalLayout.addWidget(self.l_app)
        spacerItem2 = QtWidgets.QSpacerItem(40, 60, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.l_icon = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_icon.setStyleSheet("image: url(:/Images/logo_small_icon_only_inverted.png);")
        self.l_icon.setText("")
        self.l_icon.setObjectName("l_icon")
        self.horizontalLayout.addWidget(self.l_icon)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.l_archivedname = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_archivedname.setObjectName("l_archivedname")
        self.horizontalLayout_5.addWidget(self.l_archivedname)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.l_amount = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_amount.setStyleSheet("color: orange;")
        self.l_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.l_amount.setObjectName("l_amount")
        self.horizontalLayout_6.addWidget(self.l_amount)
        self.l_article = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_article.setStyleSheet("color: orange;")
        self.l_article.setAlignment(QtCore.Qt.AlignCenter)
        self.l_article.setObjectName("l_article")
        self.horizontalLayout_6.addWidget(self.l_article)
        self.l_categorie = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_categorie.setStyleSheet("color: orange;")
        self.l_categorie.setAlignment(QtCore.Qt.AlignCenter)
        self.l_categorie.setObjectName("l_categorie")
        self.horizontalLayout_6.addWidget(self.l_categorie)
        spacerItem9 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.listofflist = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listofflist.setStyleSheet("font-size:12pt;")
        self.listofflist.setObjectName("listofflist")
        self.horizontalLayout_2.addWidget(self.listofflist)
        spacerItem11 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.d_list = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.d_list.setObjectName("d_list")
        self.horizontalLayout_3.addWidget(self.d_list)
        spacerItem14 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem16 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.b_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_back.setStyleSheet("background-color: grey;\n"
"color: white;")
        self.b_back.setObjectName("b_back")
        self.horizontalLayout_7.addWidget(self.b_back)
        self.b_reuse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_reuse.setStyleSheet("background-color: orange;")
        self.b_reuse.setObjectName("b_reuse")
        self.horizontalLayout_7.addWidget(self.b_reuse)
        spacerItem17 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(ArchivelistFrame)
        QtCore.QMetaObject.connectSlotsByName(ArchivelistFrame)

    def retranslateUi(self, ArchivelistFrame):
        _translate = QtCore.QCoreApplication.translate
        ArchivelistFrame.setWindowTitle(_translate("ArchivelistFrame", "Haushaltsplaner"))
        self.l_app.setText(_translate("ArchivelistFrame", "Archiv"))
        self.l_archivedname.setText(_translate("ArchivelistFrame", "\"Name der archivierten Liste\""))
        self.l_amount.setText(_translate("ArchivelistFrame", "Menge"))
        self.l_article.setText(_translate("ArchivelistFrame", "Artikel"))
        self.l_categorie.setText(_translate("ArchivelistFrame", "Kategorie"))
        self.b_back.setText(_translate("ArchivelistFrame", "Zurück"))
        self.b_reuse.setText(_translate("ArchivelistFrame", "Artikel verwenden"))
import menu_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ArchivelistFrame = QtWidgets.QWidget()
    ui = Ui_ArchivelistFrame()
    ui.setupUi(ArchivelistFrame)
    ArchivelistFrame.show()
    sys.exit(app.exec_())
