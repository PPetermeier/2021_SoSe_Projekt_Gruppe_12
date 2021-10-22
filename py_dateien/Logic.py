import interfaces.receipe_import as ri

import interfaces.yaml_connector as yc

import json

import calendar as c
import datetime

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore


class Controller:

    # erhält Liste der Einkaufslisten von jsonconnector und returnt diese
    def einkaufslisten(self, filepath, fenster, archiviert):
        print("Controller triggert")

        angezeigteListe = None

        if archiviert:
            print("archi")
            angezeigteListe = fenster.ui.t_archivelist
        else:
            angezeigteListe = fenster.ui.listofflist

        angezeigteListe.clear()

        for x in yc.einkaeufe(filepath, archiviert):
            print(x)
            item = qtw.QListWidgetItem(x)
            angezeigteListe.addItem(x)

        fenster.show()

    def einkaufsliste_loeschen(self, fenster, liste, filepath):

        fenster.ui.listofflist.takeItem(liste)

        yc.liste_entfernen(filepath, liste)

    def fenster_auf(self, neues_Fenster):

        print("fenster geöffnet")

        print(neues_Fenster)

        neues_Fenster.show()

    def liste_auf(self, neues_Fenster, filepath, archiviert, liste=None):

        print("flagge1")

        print(neues_Fenster)
        neues_Fenster.gezeigte_liste = liste

        print("->", neues_Fenster.gezeigte_liste)

        if archiviert:
            angezeigteListe = neues_Fenster.ui.t_archivelist
        else:
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
            tester[fenster.gezeigte_liste].append(
                {'amount': str(fenster.ui.i_amount.text()), 'category': str(fenster.ui.i_categorie.text()),
                 'item': str(fenster.ui.i_article.text())})

            print("neu ->", tester)

            yc.yaml_output(filepath, tester)

            print("ganz neu ->", yc.listenelemente(filepath))

    def rezepte_auf(self, fenster):

        print("rezepte geöffnet")

        liste = ri.get_all_receipes()

        angezeigteListe = fenster.ui.t_recipelist

        angezeigteListe.clear()

        for r in liste:
            item = qtw.QListWidgetItem(r)
            angezeigteListe.addItem(r)

        fenster.show()

    def rezept_anzeige(self, fenster, filepath, rezept=""):

        print("in der anzeige")

        fenster.ui.l_recipe.setText(rezept)


        zutaten, schritte = ri.readreceipe(rezept)

        print("zutaten ->", zutaten)
        print("schritte ->", schritte)

        fenster.ui.t_incredientlist.setRowCount(0)
        fenster.ui.list_instructions.clear()

        for z in zutaten:
            print(z)

            zeile = fenster.ui.t_incredientlist.rowCount()

            fenster.ui.t_incredientlist.insertRow(zeile)

            item = qtw.QTableWidgetItem(str(z[0]))
            item.setCheckState(False)

            fenster.ui.t_incredientlist.setItem(zeile, 0, item)
            fenster.ui.t_incredientlist.setItem(zeile, 1, qtw.QTableWidgetItem(str(z[1])))
            # fenster.ui.t_incredientlist.setItem(zeile, 2, qtw.QTableWidgetItem(str(z[1])))

        for s in schritte:
            print(s)

            item = qtw.QListWidgetItem(s)
            fenster.ui.list_instructions.addItem(s)

        fenster.ui.d_list.addItems(yc.einkaeufe(filepath, False))

        fenster.show()

    def zutaten_zu_einkaufsliste(self):

        ## REIN HIER

        pass


class BudgetController():
    modi = ["Tag", "Monat", "Jahr"]

    modus = modi[1]

    monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
              "Dezember"]

    monat = monate[datetime.datetime.now().month - 1]

    jahr = datetime.datetime.now().year

    tag = 1

    tage_im_monat = 0

    filepath = None

    fenster = None

    def modussetzer(self, index):
        self.modus = self.modi[index]

        if index == 2:
            self.fenster.ui.l_date.setText(str(self.jahr))
        elif index == 1:
            self.fenster.ui.l_date.setText(str(self.monat + str(self.jahr)))
        elif index == 0:
            self.fenster.ui.l_date.setText(str(str(self.tag) + self.monat + str(self.jahr)))

        self.liste_aktualisieren()

    def budget_auf(self, fenster, filepath):
        self.filepath = filepath
        self.fenster = fenster
        self.fenster.show()

    def liste_aktualisieren(self):

        self.fenster.ui.listofftransaction.setRowCount(0)

        eintraege = yc.budget_nach_zeit(self.filepath)

        for e in eintraege:

            if self.modus == self.modi[2]:
                if e['Jahr'] != self.jahr:
                    continue

            if self.modus == self.modi[1]:
                if e['Monat'] != self.monat or e['Jahr'] != self.jahr:
                    continue

            if self.modus == self.modi[0]:
                if e['Tag'] != self.tag or e['Monat'] != self.monat or e['Jahr'] != self.jahr:
                    continue

            datum = str(str(e['Tag']) + ". " + e['Monat'] + " " + str(e['Jahr']))

            zeile = self.fenster.ui.listofftransaction.rowCount()

            self.fenster.ui.listofftransaction.insertRow(zeile)

            self.fenster.ui.listofftransaction.setItem(zeile, 0, qtw.QTableWidgetItem(str(e['Details'])))
            self.fenster.ui.listofftransaction.setItem(zeile, 1, qtw.QTableWidgetItem(str(e['Summe'])))
            self.fenster.ui.listofftransaction.setItem(zeile, 2, qtw.QTableWidgetItem(datum))

    def weiter(self):
        if self.modus == self.modi[1]:
            self.monat_weiter(True)
        elif self.modus == self.modi[2]:
            self.jahr_weiter()

    def zurueck(self):
        if self.modus == self.modi[1]:
            self.monat_zurueck(True)
        elif self.modus == self.modi[2]:
            self.jahr_zurueck()

    def jahr_weiter(self):
        self.jahr += 1
        self.fenster.ui.l_date.setText(str(self.jahr))
        self.liste_aktualisieren()

    def jahr_zurueck(self):
        self.jahr -= 1
        self.fenster.ui.l_date.setText(str(self.jahr))
        self.liste_aktualisieren()

    def monat_weiter(self, zeigen):

        neuer_index = self.monate.index(self.monat) + 1

        if neuer_index == 12:
            neuer_index = 0
            self.jahr_weiter()

        self.monat = self.monate[neuer_index]

        self.fenster.ui.l_date.setText(str(self.monat + str(self.jahr)))

        if zeigen:
            self.liste_aktualisieren()

    def monat_zurueck(self, zeigen):

        neuer_index = self.monate.index(self.monat) - 1

        if neuer_index == -1:
            neuer_index = 11
            self.jahr_zurueck()

        self.monat = self.monate[neuer_index]

        self.fenster.ui.l_date.setText(str(self.monat + str(self.jahr)))

        if zeigen:
            self.liste_aktualisieren()

    def buchung_speichern(self, fenster):

        tag = fenster.ui.i_date.date().day()
        monat = fenster.ui.i_date.date().month() - 1
        jahr = fenster.ui.i_date.date().year()

        summe = str(fenster.ui.i_sum.text())

        details = str(fenster.ui.i_details.text())

        if fenster.ui.r_once.isChecked():
            self.buchung_into_yaml(tag, self.monate[monat], jahr, summe, details, "einmalig")
        if fenster.ui.r_weekly.isChecked():
            pass
        if fenster.ui.r_monthly.isChecked():
            self.buchung_into_yaml(tag, self.monate[monat], jahr, summe, details, "monatlich")

            while monat != 11:
                monat += 1
                self.buchung_into_yaml(tag, self.monate[monat], jahr, summe, details, "monatlich")

        if fenster.ui.r_yearly.isChecked():
            self.buchung_into_yaml(tag, self.monate[monat], jahr, summe, details, "jährlich")
            for x in range(11):
                jahr += 1
                self.buchung_into_yaml(tag, self.monate[monat], jahr, summe, details, "jährlich")

        self.liste_aktualisieren()

        fenster.close()

    def buchung_into_yaml(self, tag, monat, jahr, summe, details, rythmus):

        if tag < 10:
            tag = str(0) + str(tag)

        dicty = {'Details': details,
                 'Summe': str(summe),
                 'Jahr': jahr,
                 'Monat': monat,
                 'Tag': tag,
                 'Rythmus': rythmus}

        print("dicty -> ", dicty)

        yc.add_transaction(self.filepath, dicty)

    def delete_transaction(self, fenster):

        try:
            selected = fenster.ui.listofftransaction.selectionModel().selectedRows()
        except:
            return

        for x in selected:
            # erst in yaml löschen
            # print("->", fenster.ui.listofftransaction.item(x.Row(),0).text())

            details = fenster.ui.listofftransaction.item(x.row(), 0).text()
            summe = fenster.ui.listofftransaction.item(x.row(), 1).text()
            datum = fenster.ui.listofftransaction.item(x.row(), 2).text()

            tag = datum.split(" ")[0].replace(".", "")
            monat = datum.split(" ")[1]
            jahr = datum.split(" ")[2]

            yc.remove_trans(self.filepath, details, summe, tag, monat, jahr)

            print(details, summe, datum)

            self.liste_aktualisieren()

            return details, summe, datum, tag, self.monate.index(monat) + 1, jahr

            # dann
            # fenster.ui.listofftransaction.removeRow(x.row())

    def edit_trans(self, fenster, adder_fenster):

        details = None
        summe = None
        datum = None

        tag = None
        monat = None
        jahr = None


        try:
            details, summe, datum, tag, monat, jahr = self.delete_transaction(fenster)
        except:
            print("keine Zeile ausgewählt")
            return


        print("glagge1")

        adder_fenster.ui.i_date.setDateTime(
            QtCore.QDateTime(QtCore.QDate(int(jahr), int(monat), int(tag)), QtCore.QTime(0, 0, 0)))

        print("flagge 2")

        adder_fenster.ui.i_sum.setText(summe)
        adder_fenster.ui.i_details.setText(details)

        print("glagge 4")

        adder_fenster.show()

    def test(self):
        Kalender = c.Calendar()

        for i in Kalender.itermonthdays(2021, 10):
            self.tage_im_monat = i

        print("der", self.monate[datetime.datetime.now().month - 1], "hat", self.tage_im_monat, "Tage")
