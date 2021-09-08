from loginframe import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import mysql.connector


class LoginWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.login.clicked.connect(self.authenticate)
        self.ui.register.clicked.connect(self.register)

    def authenticate(self):

        username = self.ui.user_edit.text()
        password = self.ui.pass_edit.text()

        if username == 'admin' and password == 'admin':
            qtw.QMessageBox.information(self, 'Erfolreich angemeldet', 'Sie sind angemeldet')
        else:
            try:
                connectiondb = mysql.connector.connect(
                    host="192.168.178.42",  # IP Adresse der DB. Genutzt wird der default Port 3306
                    user="root",  # Username der DB
                    passwd="1jC:=s@ZFWWs",  # Passwort im Klartext
                    database="HPDB")  # Name der Datenbank
                cursordb = connectiondb.cursor()
                username_verification = self.ui.user_edit.text()
                password_verification = self.ui.pass_edit.text()
                sql = "select * from login where userid = %s and password = %s"
                cursordb.execute(sql, [(username_verification), (password_verification)])
                results = cursordb.fetchall()
                if results:
                    for i in results:
                        qtw.QMessageBox.information(self, 'Erfolreich angemeldet', 'Sie sind angemeldet')
                else:
                    qtw.QMessageBox.critical(self, 'Fehler', 'Sie wurden nicht angemeldet')
            except mysql.Error:
                qtw.QMessageBox.critical(self, 'Fehler', 'Keine Verbindung zur Datenbank möglich')


    def register(self):

        connectiondb = mysql.connector.connect(
            host="192.168.178.42",  # IP Adresse der DB. Genutzt wird der default Port 3306
            user="root",  # Username der DB
            passwd="1jC:=s@ZFWWs",  # Passwort im Klartext
            database="HPDB")  # Name der Datenbank
        cursordb = connectiondb.cursor()
        username_toCreate = self.ui.user_edit.text()
        password_toCreate = self.ui.pass_edit.text()
        sql = "select * from login where userid = %s"  # Prüfen, ob der Username bereits vergeben ist
        cursordb.execute(sql, [(username_toCreate)])
        results = cursordb.fetchall()
        if results:  # Wurde der Username in der LoginDB gefunden, wird False zurückgegeben und es wird kein Account angelegt.
            for i in results:
                qtw.QMessageBox.critical(self, 'Fehler', 'Der Nutzername ist bereits vergeben')
        else:  # Wurde der Username nicht in der LoginDB gefunden, so wird ein neuer Account angelegt und True zurückgegeben.
            sql = "insert into login (userid, password) values (%s,%s)"
            cursordb.execute(sql, [(username_toCreate), (password_toCreate)])
            connectiondb.commit()
            qtw.QMessageBox.information(self, 'Erfolreich Registriert', 'Ihr Account wurde erstellt.')

if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()

