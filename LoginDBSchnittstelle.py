# Schnittstelle zur MySQL Datenbank
#
# Login:
# Die Funktion muss mit einem Username und einem Passwort aufgerufen werden.
# Sind die Login-Daten korrekt, so wird ein true zurückgegeben. Sind die Login Daten nicht korrekt, so wird ein
# False zurück gegeben. Eine genaue Definition, ob das Passwort oder der Nutzername falsch ist, gibt es (noch) nicht.
#
#

import mysql.connector

def login(username, passwort):
    connectiondb = mysql.connector.connect(
        host="192.168.178.42", #IP Adresse der DB. Genutzt wird der default Port 3306
        user="root", #Username der DB
        passwd="1jC:=s@ZFWWs", #Passwort im Klartext
        database="HPDB")#Name der Datenbank
    cursordb = connectiondb.cursor()
    username_verification = username
    password_verification = passwort
    sql = "select * from login where userid = %s and password = %s"
    cursordb.execute(sql,[(username_verification),(password_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            return True
    else:
        return False

def register(username,passwort)
    connectiondb = mysql.connector.connect(
        host="192.168.178.42",  # IP Adresse der DB. Genutzt wird der default Port 3306
        user="root",  # Username der DB
        passwd="1jC:=s@ZFWWs",  # Passwort im Klartext
        database="HPDB")  # Name der Datenbank
    cursordb = connectiondb.cursor()
    username_toCreate = username
    password_toCreate = passwort
    sql = "select * from login where userid = %s" # Prüfen, ob der Username bereits vergeben ist
    cursordb.execute(sql, [(username_toCreate)])
    results = cursordb.fetchall()
    if results: # Wurde der Username in der LoginDB gefunden, wird False zurückgegeben und es wird kein Account angelegt.
        for i in results:
            return False
    else: # Wurder der Username nicht in der LoginDB gefunden, so wird ein neuer Account angelegt und True zurückgegeben.
        sql = "insert into login (userid, password) values (%s,%s)"
        cursordb.execute(sql, [(username_toCreate), (password_toCreate)])
        connectiondb.commit()
        return True