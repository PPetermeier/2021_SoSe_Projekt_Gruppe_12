import json


def getreceipe():#Methode um Rezepte herunterzuladen
  return 0

def readreceipe(recipepath):
    with open(recipepath, 'r') as f:
        datastore = json.load(f)
    print(datastore)
    return datastore