from pathlib import Path
import json
import pandas as pd
import yaml

import recipes
import os

# _________________________INITIALE DEKLARATION DER INDIVIDUELLEN DATEINAMEN SOWIE DATENANLAGE FÜR JSON_________________

username_verification = "Jonas"  # Nutzereingabe wird ähnlich des Hauptprogrammes simuliert
filepathgroc = "../save_data/{}_grocery.json".format(
    username_verification.lower())  # Der Pfad der save_data Datei wird festgelegt /save_data/nutzername_grocery.json
usergroceryjson = Path(filepathgroc)  # Der Pfad wird zu verändert, dass er zum Windows Dateisystem passt.
usergroceryjson.touch(exist_ok=True)  # falls die Datei nicht existiert, wird sie angelegt
filepathbud = "../save_data/{}_budget.json".format(username_verification.lower())
userbudgetjson = Path(filepathbud)
userbudgetjson.touch(exist_ok=True)


# ______________________________________________________________________________________________________________________

#                                                  save_data

# ____________________________________LISTE DER EINKAUFSLISTEN ERSTELLEN________________________________________________

def jsontester():
    listOfLists = []
    with open(usergroceryjson, 'r') as file:  # save_data wird eingelesen und zur Laufzeit abgespeichert
        json_data = json.load(file)
    for key in json_data.keys():  # Die Namen der Einkaufslisten werden ausgelesen und in "listoflists" geschrieben
        listOfLists.append(key)
    print("Liste der Listen aus save_data:")
    print()
    print(listOfLists)
    print()
    print()
    # ______________________________________________________________________________________________________________________

    # _________________________________________EINKAUFSLISTE AUSLESEN_______________________________________________________

    chooseList = listOfLists[0]  # Welche Liste (index) soll ausgelesen werden?
    df = pd.read_json(filepathgroc)
    df[chooseList].apply(pd.Series)

    with open(filepathgroc, 'w') as file:
        json.dump(json_data, file)
    print("Listeninhalte aus save_data (einzel per Index erreichbar):")
    print()
    for i in range(len(json_data[chooseList])):
        print(json_data[chooseList][i]['item'])
        print(json_data[chooseList][i]['amount'])
        print(json_data[chooseList][i]['category'])
    print()
    print()

    with open(filepathgroc) as fh:
        dictionary_data = json.load(fh)


# ______________________________________________________________________________________________________________________

#                                                  YAML

# _________________________INITIALE DEKLARATION DER INDIVIDUELLEN DATEINAMEN SOWIE DATENANLAGE FÜR JSON_________________

username_verification = "Jonas"  # Nutzereingabe wird ähnlich des Hauptprogrammes simuliert
filepathgroc = "../save_data/{}_grocery.yaml".format(
    username_verification.lower())  # Der Pfad der save_data Datei wird festgelegt /save_data/nutzername_grocery.json
usergroceryjson = Path(filepathgroc)  # Der Pfad wird zu verändert, dass er zum Windows Dateisystem passt.
usergroceryjson.touch(exist_ok=True)  # falls die Datei nicht existiert, wird sie angelegt
filepathbud = "../save_data/{}_budget.yaml".format(username_verification.lower())
userbudgetjson = Path(filepathbud)
userbudgetjson.touch(exist_ok=True)

# _________________________________________LISTE DER LISTEN AUSGEBEN____________________________________________________

#######################################################
#                                                     #
# HIER STEHT EIN ABSOLUTER PFAD !!!                   #
#                                                     #
#######################################################


filepathgroc = "S:\PythonProgramme\SoSe_Projekt_Gruppe_12\database_prototype\grocery_list_template.yaml"


def einkaeufe():
    with open(filepathgroc) as file:
        yamlFile = yaml.load(file, Loader=yaml.FullLoader)
    listOfLists = []
    for key in yamlFile.keys():
        listOfLists.append(key)
    # print("Liste der Listen aus YAML:")
    # print()
    print(listOfLists)
    # print()
    # print()

    return listOfLists


# ___________________________________________EINKAUFSLISTE AUSGEBEN_____________________________________________________
def yamltester2(listenname):
    with open(filepathgroc) as fh:
        dictionary_data = yaml.safe_load(fh)
    print("Dictionary aus YAML:")
    print()

    # dictionary_data['Tante Emmas Geburtstag'][0]['item'] = 'Torte'

    print(dictionary_data[listenname])
    print()
    print()

    return dictionary_data[listenname]

    # del dictionary_data['Tante Emmas Geburtstag'][x] #Element an Stelle x löschen

    # print(len(dictionary_data['Tante Emmas Geburtstag'])) #Länge des Dictonarys

    with open(filepathgroc, 'w') as outfile:  # Dictionary zurück in YAML schreiben
        yaml.dump(dictionary_data, outfile, default_flow_style=False)


# _______________________________________________________________________________________________________________________

# ____________________________________________REZEPTE AUSLESEN___________________________________________


def rezeptleser():
    aktuell = os.getcwd()

    neu = os.path.relpath("..\\recipes\\recipe.json", aktuell)

    # print("->", neu)

    # if os.path.exists(neu):
    #     print("gefunden")
    # else:
    #     print("huen")

    with open(neu) as r:
        data = json.load(r)

        print("->", [data['data']['recipe']['title']])

        return [data['data']['recipe']['title']]


def rezeptoeffner():
    aktuell = os.getcwd()

    neu = os.path.relpath("..\\recipes\\recipe.json", aktuell)

    with open(neu) as r:
        data = json.load(r)

        zutaten = []
        schritte = []

        #print(data['data']['ingredients'])

        for i in data['data']['ingredients']:

            try:
                # print(str(i['quantity1']))
                #
                # print(str(i['unit_short']))
                #
                # print(str(i['product']))

                zutat = [str(i['quantity1']) +" "+ str(i['unit_short']) , str(i['product'])]

                print(zutat)

                zutaten.append(zutat)

            except:
                print("hier war das and more")

        print("zutaten", zutaten)

        for s in data['data']['steps']:

            try:
                schritt = str(s['step_text'])

                schritte.append(schritt)
            except:
                print("hier war wieder das and more")

        return zutaten, schritte

# rezeptleser()
