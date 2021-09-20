from loginframe import Ui_Login
from menuframe import Ui_Haushaltsplaner

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import mysql.connector

cnx = mysql.connector.connect(user="hproot@hplogin",
                              password="<Y#T<>1Ug`/q",
                              host="hplogin.mysql.database.azure.com",
                              port=3306,
                              database="hpdb");

class LoginWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.authenticate)
        self.ui.register_button.clicked.connect(self.register)


    def authenticate(self):

        username = self.ui.user_edit.text()
        password = self.ui.pass_edit.text()

        if username == 'admin' and password == 'admin':
            qtw.QMessageBox.information(self, 'Erfolgreich angemeldet', 'Sie sind angemeldet')
            loginwidget.close()
            menuwidget.show()
        else:
            try:
                cursordb = cnx.cursor()
                username_verification = self.ui.user_edit.text()
                password_verification = self.ui.pass_edit.text()
                sql = "select * from user_database_login where username = %s and userpassword = %s"
                cursordb.execute(sql, [(username_verification), (password_verification)])
                results = cursordb.fetchall()
                if results:
                    for i in results:
                        qtw.QMessageBox.information(self, 'Erfolgreich angemeldet', 'Sie sind angemeldet')
                        loginwidget.close()
                        menuwidget.show()
                else:
                    qtw.QMessageBox.critical(self, 'Fehler', 'Sie wurden nicht angemeldet')
            except Exception as err:
                qtw.QMessageBox.critical(self, 'Fehler', 'Keine Verbindung zum Login-Server möglich')

    def register(self):
        try:
            cursordb = cnx.cursor()
            username_toCreate = self.ui.user_edit.text()
            password_toCreate = self.ui.pass_edit.text()
            sql = "select * from user_database_login where username = %s"  # Prüfen, ob der Username bereits vergeben ist
            cursordb.execute(sql, [(username_toCreate)])
            results = cursordb.fetchall()
            if results:  # Wurde der Username in der LoginDB gefunden, wird False zurückgegeben und es wird kein Account angelegt.
                for i in results:
                    qtw.QMessageBox.critical(self, 'Fehler', 'Der Nutzername ist bereits vergeben')
            else:  # Wurde der Username nicht in der LoginDB gefunden, so wird ein neuer Account angelegt und True zurückgegeben.
                sql = "insert into user_database_login (username, userpassword) values (%s,%s)"
                cursordb.execute(sql, [(username_toCreate), (password_toCreate)])
                cnx.commit()
                qtw.QMessageBox.information(self, 'Erfolgreich Registriert', 'Ihr Account wurde erstellt.')
        except Exception as err:
                qtw.QMessageBox.critical(self, 'Fehler', 'Keine Verbindung zum Login-Server möglich')


class MenuWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Haushaltsplaner()
        self.ui.setupUi(self)
        self.ui.b_logout.clicked.connect(self.logout)

    def logout(self):
        menuwidget.close()
        loginwidget.show()


if __name__ == '__main__':
    app = qtw.QApplication([])

    loginwidget = LoginWindow()
    loginwidget.show()

    menuwidget = MenuWindow()


    app.exec_()

