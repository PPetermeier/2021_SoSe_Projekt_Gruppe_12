from loginframe import Ui_Login
from menuframe import Ui_Haushaltsplaner
from budgetplanerframe import Ui_Budgetplaner
from newtransactionframe import Ui_AddTransaction
from groceryitemframe import Ui_Groceryitemframe
from grocerymainframe import Ui_Grocerymainframe
from recipeframe import Ui_RecipeWindow
from instructionframe import Ui_Rezeptanleitung
from archiveframe import Ui_ArchivFrame
from archivelistframe import Ui_ArchivListFrame
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

##ES WIRD IMMER DIE ADMIN GROCERY ANGEZEIGT
filepath = "../save_data/admin_grocery.yaml"
filepathgrocery = "../save_data/admin_budget.yaml"

# Controller initialisiert und die funktion einkaufslisten aufgerufen
Kontro = Logic.Controller()
GroKontro = Logic.BudgetController()

instructionswidget = None
recipewidget = None
grocerymainwidget = None


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

            # menuwidget = MenuWindow()
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

                        # menuwidget = MenuWindow()
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
        Kontro.einkaufslisten(filepath, grocerymainwidget, False)

    def openbudget(self):
        Kontro.fenster_zu(self)
        GroKontro.budget_auf(budgetplanerwidget, filepathgrocery)

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
        self.ui.b_delete.clicked.connect(self.delete_list)
        self.ui.b_archiv.clicked.connect(self.open_archive)

    def open_archive(self):
        Kontro.einkaufslisten(filepath, archivewidget, True)
        Kontro.fenster_zu(self)

    def delete_list(self):
        selected = self.ui.listofflist.currentRow()
        Kontro.einkaufsliste_loeschen(self, selected)

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
        Kontro.liste_auf(groceryitemwidget, filepath, False, selected)

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
        self.ui.b_next.clicked.connect(self.next)
        self.ui.b_previous.clicked.connect(self.prev)
        self.ui.b_day.clicked.connect(self.tag)
        self.ui.pushButton_4.clicked.connect(self.monat)
        self.ui.b_year.clicked.connect(self.jahr)
        self.ui.b_deletetransaction.clicked.connect(self.delete)
        self.ui.b_edittransaction.clicked.connect(self.transaktion_bearbeiten)

    def transaktion_bearbeiten(self):
        GroKontro.edit_trans(self, addtransactionwidget)

    def delete(self):
        GroKontro.delete_transaction(self)

    def tag(self):
        GroKontro.modussetzer(0)

    def monat(self):
        GroKontro.modussetzer(1)

    def jahr(self):
        GroKontro.modussetzer(2)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(menuwidget)

    def addTransaction(self):
        addtransactionwidget.show()

    def next(self):
        GroKontro.weiter()

    def prev(self):
        GroKontro.zurueck()


class AddTransactionWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_AddTransaction()
        self.ui.setupUi(self)

        self.ui.b_safe.clicked.connect(self.speichern)

    def speichern(self):
        GroKontro.buchung_speichern(self)


class RecipeWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_RecipeWindow()
        self.ui.setupUi(self)
        self.ui.b_recipeview.clicked.connect(self.open_recipe)
        self.ui.b_back.clicked.connect(self.back)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(grocerymainwidget)

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

            # print(item.text())

            if item.checkState():
                zutat = [str(self.ui.t_incredientlist.item(reihe, 0).text()),
                         str(self.ui.t_incredientlist.item(reihe, 1).text())]

                zutaten.append(zutat)

        print(zutaten)
        Kontro.zutaten_zu_einkaufsliste(liste, zutaten)


class ArchiveWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ArchivFrame()
        self.ui.setupUi(self)

        self.ui.b_back.clicked.connect(self.back)
        self.ui.b_viewarchive.clicked.connect(self.viewarchivedlist)

    def viewarchivedlist(self):
        Kontro.fenster_zu(self)

        selected = self.ui.t_archivelist.currentItem().text()

        Kontro.liste_auf(archivelistwidget, filepath, True, selected)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.fenster_auf(grocerymainwidget)


class ArchiveListWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ArchivListFrame()
        self.ui.setupUi(self)

        self.ui.b_back.clicked.connect(self.back)

    def back(self):
        Kontro.fenster_zu(self)
        Kontro.einkaufslisten(filepath, archivewidget, True)


if __name__ == '__main__':
    app = qtw.QApplication([])

    loginwidget = LoginWindow()

    Kontro.fenster_auf(loginwidget)

    menuwidget = MenuWindow()
    budgetplanerwidget = BudgetplanerMainWindow()
    addtransactionwidget = AddTransactionWindow()
    grocerymainwidget = GrocerymainWindow()
    groceryitemwidget = GroceryitemWindow()
    recipewidget = RecipeWindow()
    instructionswidget = AnleitungsWindow()
    archivewidget = ArchiveWindow()
    archivelistwidget = ArchiveListWindow()

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
