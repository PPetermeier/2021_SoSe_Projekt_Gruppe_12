from loginframe import Ui_Login
from menuframe import Ui_Haushaltsplaner
from budgetplanerframe import Ui_Budgetplaner
from newtransactionframe import Ui_AddTransaction
from groceryitemframe import Ui_Groceryitemframe
from grocerymainframe import Ui_Grocerymainframe
from recipeframe import Ui_RecipeWindow
from instructionframe import Ui_Rezeptanleitung
import shutil
import os
from pathlib import Path

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import mysql.connector

import Logic

cnx = mysql.connector.connect(user="hproot@hplogin",
                              password="<Y#T<>1Ug`/q",
                              host="hplogin.mysql.database.azure.com",
                              port=3306,
                              database="hpdb");



filepath = "../save_data/admin_grocery.yaml"

# Controller initialisiert und die funktion einkaufslisten aufgerufen


Kontro = Logic.Controller()

instructionswidget = None
recipewidget = None



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
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if username == 'admin' and (password == 'admin' or password == ''):
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            username_verification = 'admin'
            qtw.QMessageBox.information(self, 'Erfolgreich angemeldet', 'Sie sind angemeldet')
            loginwidget.close()
            filepath = "../save_data/{}_grocery.yaml".format(username_verification.lower())
            filepathgrocery = "../save_data/{}_grocery.yaml".format(username_verification.lower())
            try:
                f = open(filepath)
            except IOError:
                shutil.copy('../save_data/grocery_list_template.yaml', filepath)
            try:
                f = open(filepathgrocery)
            except IOError:
                shutil.copy('../save_data/budget_list_template.yaml', filepathgrocery)

            #menuwidget = MenuWindow()
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
                        filepath = "../save_data/{}_grocery.yaml".format(username_verification.lower())
                        filepathgrocery = "../save_data/{}_budget.yaml".format(username_verification.lower())
                        try:
                            f = open(filepath)
                        except IOError:
                            shutil.copy('../save_data/grocery_list_template.yaml', filepath)
                        try:
                            f = open(filepathgrocery)
                        except IOError:
                            shutil.copy('../save_data/budget_list_template.yaml', filepathgrocery)

                        #menuwidget = MenuWindow()
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
        self.ui.b_grocery.clicked.connect(self.opengrocery)
        self.ui.b_budget.clicked.connect(self.openbudget)

    def opengrocery(self):
        # Controller schließt Fenster
        Kontro.fenster_zu(self)

        # Controller öffnet fenster
        Kontro.einkaufslisten(filepath, grocerymainwidget)

    def openbudget(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(budgetplanerwidget)

    def logout(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(loginwidget)


class GrocerymainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Grocerymainframe()
        self.ui.setupUi(self)
        self.ui.b_back.clicked.connect(self.back)
        self.ui.b_newlist.clicked.connect(self.newList)
        self.ui.b_openlist.clicked.connect(self.open_list)
        self.ui.b_recipe.clicked.connect(self.open_recipes)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(menuwidget)

    def newList(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(groceryitemwidget)

    def open_list(self):
        Kontro.fenster_zu(self)

        selected = self.ui.listofflist.currentItem().text()

        print("liste geöffnet")
        Kontro.liste_auf(groceryitemwidget, filepath, selected)

    def open_recipes(self):
        Kontro.fenster_zu(self)
        Kontro.rezepte_auf(recipewidget)


class GroceryitemWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Groceryitemframe()
        self.ui.setupUi(self)
        self.ui.b_back.clicked.connect(self.back)
        self.ui.b_add.clicked.connect(self.add)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(grocerymainwidget)

    def add(self):
        Kontro.artikel_hinzufuegen(self, filepath)


class BudgetplanerMainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Budgetplaner()
        self.ui.setupUi(self)
        self.ui.b_back.clicked.connect(self.back)
        self.ui.b_addtransaction.clicked.connect(self.addTransaction)

    def back(self):
        Kontro.fenster_zu(self)

        Kontro.fenster_auf(menuwidget)

    def addTransaction(self):
        addtransactionwidget.show()


class AddTransactionWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_AddTransaction()
        self.ui.setupUi(self)


class RecipeWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_RecipeWindow()
        self.ui.setupUi(self)
        self.ui.b_recipeview.clicked.connect(self.open_recipe)

    def open_recipe(self):
        Kontro.fenster_zu(self)

        selected = self.ui.t_recipelist.currentItem().text()

        print("rezept geöffnet")
        Kontro.rezept_anzeige(instructionswidget, filepath, selected)


class AnleitungsWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Rezeptanleitung()
        self.ui.setupUi(self)

        self.ui.b_addrecipe.clicked.connect(self.zutaten_hinzufuegen)
        self.ui.b_back.clicked.connect(self.back)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(recipewidget)

    def zutaten_hinzufuegen(self):

        liste = self.ui.d_list.currentText()

        zutaten = []

        print(liste)

        for reihe in range(self.ui.t_incredientlist.rowCount()):
            item = self.ui.t_incredientlist.item(reihe, 0)

            #print(item.text())

            if item.checkState():
                zutat = [str(self.ui.t_incredientlist.item(reihe, 0).text()) , str(self.ui.t_incredientlist.item(reihe, 1).text())]

                zutaten.append(zutat)


        print(zutaten)


        Kontro.zutaten_zu_einkaufsliste(liste, zutaten)


if __name__ == '__main__':

    app = qtw.QApplication([])

    loginwidget = LoginWindow()

    Kontro.fenster_auf(loginwidget)

    #menuwidget = 'None'

    menuwidget = MenuWindow()
    budgetplanerwidget = BudgetplanerMainWindow()
    addtransactionwidget = AddTransactionWindow()
    grocerymainwidget = GrocerymainWindow()
    groceryitemwidget = GroceryitemWindow()
    recipewidget = RecipeWindow()
    instructionswidget = AnleitungsWindow()

    #
    # loginwidget2 = LoginWindow()
    # menuwidget2 = MenuWindow()
    #
    # win = qtw.QStackedWidget()
    # win.addWidget(loginwidget2)
    # win.addWidget(menuwidget2)
    #
    # loginwidget2.ui.login_button.clicked.connect(lambda: win.setCurrentIndex(1))
    # win.resize(1200,1200)
    # win.show()



    app.exec_()
