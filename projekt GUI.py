
import tkinter as glowne
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import random


lista=["Ile to jest 2 razy 2? A:4, B:1, C:500","Jak nazywa się znany skoczek narciarski? A:Małysz, B:Żak, C:Kowalski", "Żółta łódź podwodna to statek: A:Beatlesów B:Doorsów C:Pearl Jamu", "Kim była Ariel z filmu Disneya? A:Syrenką B:Elfem  C:Indianką ", "Gdyby całe wydobyte w historii złoto przetopić w jeden sześcian, to miałby bok o długości: A:20,5 m  B:205 m, C: 5m "]
dlugosc=len(lista)
czyuzytokola= False
suma_paczek = 40

def zamknij_okno1():
    messagebox.showinfo("Zaczynamy", name.get())
    glowneOkno.destroy()


def nowe_okno():
    if len(lista) > 0:
        wylosowana=random.choice(lista)
        suma_paczek=40
        def zamknij():
            if dlugosc >0:
                if A.get() !="0":
                    lista.remove(wylosowana)
                    messagebox.showinfo(A.get(), "A to poprawna odpowiedź! Masz teraz tyle paczek, ile wyświetla się nad tym napisem.")
                    okno_pytan.destroy()
                    nowe_okno()
                else:
                    messagebox.showinfo("Przegrałeś!","A to poprawna odpowiedź. Przykro mi.")
                    okno_pytan.destroy()

            else:
                messagebox.showinfo(suma_paczek,"To koniec gry! Wygrałeś tyle paczek.")
                okno_pytan.destroy()


    def koloR():
        global czyuzytokola
        czyuzytokola= True
        messagebox.showinfo("Koło ratunkowe"," Masz 20 dodatkowych sekund. Poinformujemy Cię, gdy czas minie.")
        time.sleep(20)
        messagebox.showinfo("Koło ratunkowe","Koniec czasu!")
        przycisk_kolo_ratunkowe.destroy()

    def koniec_gry():
        messagebox.showinfo("Koniec","Zakończyłeś grę!")
        okno_pytan.destroy()

    okno_pytan=glowne.Tk()
    okno_pytan.title( "Pytanie" )

    if czyuzytokola==False:
        przycisk_kolo_ratunkowe=Button(okno_pytan, text="Koło ratunkowe", command=koloR)
        przycisk_kolo_ratunkowe.pack()

    przycisk_koniec_gry=Button(okno_pytan, text="Koniec gry", command=koniec_gry)
    przycisk_koniec_gry.pack()


    text = glowne.StringVar()
    etykieta = Label(okno_pytan, text=wylosowana)
    etykieta.pack()
    description = glowne.Label(okno_pytan, text="Ile paczek obstawiasz na:").pack()
    description = glowne.Label(okno_pytan, text="A").pack()
    A = Spinbox(okno_pytan, from_=0, to=40)
    A.pack()
    description = glowne.Label(okno_pytan, text="B").pack()
    B = Spinbox(okno_pytan, from_=0, to=40)
    B.pack()
    description = glowne.Label(okno_pytan, text="C").pack()
    C = Spinbox(okno_pytan, from_=0, to=40)
    C.pack()
    
    messagebox.showinfo("Czas start!", "Masz 60 sekund na zastanowienie się")
    time.sleep(60)
    messagebox.showinfo("Koniec czasu!", "Odpowiedz lub użyj koła ratunkowego")

    przycisk_dalej = Button(okno_pytan, text = "Dalej", command = zamknij)
    przycisk_dalej.pack()


    okno_pytan.mainloop()

###poczatek###
glowneOkno=glowne.Tk()
text=glowne.StringVar()

plotno=Canvas(glowneOkno, width=400, height=400)
plotno.pack()
zdjecie= Image.open("a.jpg")
zdjecietk=ImageTk.PhotoImage(zdjecie)
plotno.create_image(200,200, image=zdjecietk)

glowneOkno.title("Postaw na milion")
przywitanie = glowne.Label(glowneOkno, text = "Witam serdecznie w programie Postaw na milion!\nPrzypominam, że masz możliwość wyboru jednorazowego koła ratunkowego, jakim jest dodatkowe 20 sekund na odpowiedź. \nMasz do dyspozycji cały milion złotych! \nPodzieliliśmy go na 40 paczek po 25000 złotych. W zależności od tego ile obstawisz na poprawną odpowiedź, z taką kwotą przechodzisz do następnego etapu.\n Jest z nami uczestnik gry. Jak masz na imię?").pack()
name = glowne.Entry(glowneOkno, width = 50)
name.pack()
przycisk_dalej = glowne.Button(glowneOkno, text = "Dalej", width=50, command= zamknij_okno1)
przycisk_dalej.pack()

glowneOkno.mainloop()
nowe_okno()
