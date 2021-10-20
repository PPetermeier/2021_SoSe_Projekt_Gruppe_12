import database_prototype.jsonconnector as jc

import interfaces.receipe_import as ri

import interfaces.yaml_connector as yc

import json

import calendar as c
import datetime

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore


class Controller:

    #erhält Liste der Einkaufslisten von jsonconnector und returnt diese
    def einkaufslisten(self, filepath, fenster):
        print("Controller triggert")

        angezeigteListe = fenster.ui.listofflist

        angezeigteListe.clear()

        for x in yc.einkaeufe(filepath):
            print(x)
            item = qtw.QListWidgetItem(x)
            angezeigteListe.addItem(x)

        fenster.show()

    def fenster_auf(self, neues_Fenster):

        print("fenster geöffnet")

        print(neues_Fenster)

        neues_Fenster.show()

    def liste_auf(self, neues_Fenster, filepath, liste=None):

        neues_Fenster.gezeigte_liste = liste

        print("->",neues_Fenster.gezeigte_liste)

        angezeigteListe = neues_Fenster.ui.listofflist
        angezeigteListe.setRowCount(0)

        print("bis hier")

        for x in yc.listenelemente(filepath)[liste]:

            if 'archiviert' in x:
                continue

            zeile = angezeigteListe.rowCount()

            angezeigteListe.insertRow(zeile)

            angezeigteListe.setItem(zeile, 0, qtw.QTableWidgetItem(str(x['amount'])))
            angezeigteListe.setItem(zeile, 1, qtw.QTableWidgetItem(str(x['item'])))
            angezeigteListe.setItem(zeile, 2, qtw.QTableWidgetItem(str(x['category'])))

        neues_Fenster.show()

    def fenster_zu(self, altes_Fenster):

        altes_Fenster.close()

    def liste_hinzufuegen(self):
        pass

    def artikel_hinzufuegen(self, fenster, filepath):
        print("adder geklickt")

        if fenster.ui.i_amount.text() == '' or fenster.ui.i_article.text() == '' or fenster.ui.i_categorie.text() == '':
            print("eins der angaben ist leer")
        else:
            print(fenster.ui.i_amount.text(), fenster.ui.i_article.text(), fenster.ui.i_categorie.text())

            zeile = fenster.ui.listofflist.rowCount()

            fenster.ui.listofflist.insertRow(zeile)

            fenster.ui.listofflist.setItem(zeile, 0, qtw.QTableWidgetItem(str(fenster.ui.i_amount.text())))
            fenster.ui.listofflist.setItem(zeile, 1, qtw.QTableWidgetItem(str(fenster.ui.i_article.text())))
            fenster.ui.listofflist.setItem(zeile, 2, qtw.QTableWidgetItem(str(fenster.ui.i_categorie.text())))

            print(yc.listenelemente(filepath)[fenster.gezeigte_liste])

            tester = yc.listenelemente(filepath)
            tester[fenster.gezeigte_liste].append({'amount': str(fenster.ui.i_amount.text()), 'category': str(fenster.ui.i_categorie.text()), 'item': str(fenster.ui.i_article.text())})

            print("neu ->", tester)

            yc.yaml_output(filepath, tester)

            print("ganz neu ->", yc.listenelemente(filepath))

    def rezepte_auf(self, fenster):

        print("rezepte geöffnet")

        liste = ri.get_all_receipes()

        angezeigteListe = fenster.ui.t_recipelist

        for r in liste:
            item = qtw.QListWidgetItem(r)
            angezeigteListe.addItem(r)

        fenster.show()

    def rezept_anzeige(self, fenster, filepath, rezept = ""):

        print ("in der anzeige")

        zutaten, schritte = ri.readreceipe(rezept)

        #print("zutaten ->", zutaten)
        #print("schritte ->", schritte)

        # chkBox = qtw.QCheckBox()
        # chkBox.setChecked(False)

        for z in zutaten:

            zeile = fenster.ui.t_incredientlist.rowCount()

            fenster.ui.t_incredientlist.insertRow(zeile)

            item = qtw.QTableWidgetItem(str(z[0]))
            item.setCheckState(False)

            fenster.ui.t_incredientlist.setItem(zeile, 0, item)
            fenster.ui.t_incredientlist.setItem(zeile, 1, qtw.QTableWidgetItem(str(z[1])))
            #fenster.ui.t_incredientlist.setItem(zeile, 2, qtw.QTableWidgetItem(str(z[1])))

        for s in schritte:

            item = qtw.QListWidgetItem(s)
            fenster.ui.list_instructions.addItem(s)

        fenster.ui.d_list.addItems(yc.einkaeufe(filepath))


        fenster.show()

    def zutaten_zu_einkaufsliste(self):

        ## REIN HIER

        pass


class BudgetController():

    monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

    tage_im_monat = 0

    def test(self):
        Kalender = c.Calendar()

        for i in Kalender.itermonthdays(2021,10):
            self.tage_im_monat = i


        print("der", self.monate[datetime.datetime.now().month -1], "hat", self.tage_im_monat, "Tage")


bc = BudgetController()

bc.test()