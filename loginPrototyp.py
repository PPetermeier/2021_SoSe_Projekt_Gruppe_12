from tkinter import *
import mysql.connector

# connecting to the database
connectiondb = mysql.connector.connect(
    host="192.168.178.42",
    user="root",
    passwd="1jC:=s@ZFWWs",
    database="HPDB")
cursordb = connectiondb.cursor()

global username_verification
global password_verification


def buttonEinloggenClick():
    username_verification = int(entryUserid.get())
    password_verification = (entryPassword.get())
    sql = "select * from login where userid = %s and password = %s"
    cursordb.execute(sql,[(username_verification),(password_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            print("Eingeloggt")
            labeleingeloggt = Label(master=tkFenster, text='eingeloggt')
            labeleingeloggt.place(x=54, y=200, width=100, height=27)
            break
    else:
        print("Fehler beim Einloggen")

def buttonRegisterClick():
    username_verification = int(entryUserid.get())
    password_verification = (entryPassword.get())
    sql = "insert into login (userid, password) values (%s,%s)"
    cursordb.execute(sql, [(username_verification), (password_verification)])
    connectiondb.commit()
    print("Registriert")

tkFenster = Tk()
tkFenster.title('Haushaltsplaner Login')
tkFenster.geometry('350x250')
# Label mit Aufschrift Userid
labelUserid = Label(master=tkFenster, text='Username:')
labelUserid.place(x=54, y=24, width=100, height=27)
# Entry für die Userid
entryUserid = Entry(master=tkFenster, bg='white')
entryUserid.place(x=164, y=24, width=100, height=27)
# Label mit Aufschrift Passwort
labelPassword = Label(master=tkFenster, text='Password:')
labelPassword.place(x=54, y=64, width=100, height=27)
# Entry für das Passwort
entryPassword = Entry(master=tkFenster, bg='white')
entryPassword.place(x=164, y=64, width=100, height=27)
#Button Einloggen
buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='Einloggen', command=buttonEinloggenClick)
buttonBerechnen.place(x=54, y=104, width=100, height=27)
#Button Registrieren
buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='Registrieren', command=buttonRegisterClick)
buttonBerechnen.place(x=54, y=154, width=100, height=27)

tkFenster.mainloop()




