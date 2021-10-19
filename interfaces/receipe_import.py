import json
import os


def getreceipe():#Methode um Rezepte herunterzuladen
  return 0

def readreceipe(rezept = ''):
    aktuell = os.getcwd()

    neu = os.path.relpath("..\\recipes\\recipe.json", aktuell)

    data = None

    with open(neu) as r:
        data = json.load(r)

        zutaten = []
        schritte = []

        # print(data['data']['ingredients'])
    for key in data:
        if key != 'status' and data[key]['recipe']['title'] == rezept:
            for i in data[key]['ingredients']:

                #print(i)
                try:
                    zutat = [str(i['quantity1']) + " " + str(i['unit_short']), str(i['product'])]
                    zutaten.append(zutat)
                except:
                    print("hier war das and more")

            for s in data[key]['steps']:

                try:
                    schritt = str(s['step_text'])

                    schritte.append(schritt)
                except:
                    print("hier war wieder das and more")

    return zutaten, schritte

def get_all_receipes():
    aktuell = os.getcwd()

    neu = os.path.relpath("..\\recipes\\recipe.json", aktuell)

    data = None

    list_of_receipes = []

    with open(neu) as r:
        data = json.load(r)

    for key in data:
        if key != 'status':
            rezept = data[key]['recipe']['title']
            list_of_receipes.append(rezept)

    #print(list_of_receipes)
    return list_of_receipes


readreceipe()