from pathlib import Path
import json

username_verification = "Jonas" #Nutzereingabe wird ähnlich des Hauptprogrammes simuliert
filepath = "../JSON/{}_grocery.json".format(username_verification.lower()) #Der Pfad der JSON Datei wird festgelegt /JSON/nutzername_grocery.json
usergroceryjson = Path(filepath)  #Der Pfad wird zu verändert, dass er zum Windows Dateisystem passt.
usergroceryjson.touch(exist_ok=True) #falls die Datei nicht existiert, wird sie angelegt
#groceryjson = open(usergroceryjson)
filepath = "../JSON/{}_budget.json".format(username_verification.lower())
userbudgetjson = Path(filepath)
userbudgetjson.touch(exist_ok=True)
#budgetjson = open(userbudgetjson)

listoflists = []

with open(usergroceryjson, 'r') as file: #JSON wird eingelesen und zur Laufzeit abgespeichert
  json_data = json.load(file)

for key in json_data.keys(): #Die Namen der Einkaufslisten werden ausgelesen und in "listoflists" geschrieben
    listoflists.append(key)

print(listoflists)

chooselist = listoflists[0] #Die Liste "Birthday of Susan" wird in chooselist geschrieben

for i in json_data[chooselist]: #es werden alle Elemente ausgelesen, die sich unter dem Key von chooselist (Birthday of Susan) befinden
  print(i['item'])
  print(i['amount'])
  print(i['category'])
