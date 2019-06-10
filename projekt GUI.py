### przyciski ( z funkcjami) koła ratunkowego i zakończenia gry (powinny być na każdym slajdzie oprócz pierwszego)###

from tkinter import *
from tkinter import messagebox
import time
from PIL import Image,ImageTk

def kolo_ratunkowe():
    messagebox.showinfo("Koło ratunkowe", "Masz 20 dodatkowych sekund! Poinformujemy Cię, gdy czas minie")
    time.sleep(20)
    messagebox.showinfo("Koło ratunkowe","Koniec czasu! Odpowiedz na pytania")

def koniec_gry():
    messagebox.showinfo("Koniec","Zakończyłeś grę!")
    glowneOkno.destroy()

glowneOkno=Tk()
glowneOkno.title("Postaw na milion")
glowneOkno.geometry("400x400")


przycisk_kolo_ratunkowe=Button(glowneOkno, text="Koło ratunkowe", command=kolo_ratunkowe)
przycisk_koniec_gry=Button(glowneOkno, text="Koniec gry", command=koniec_gry)



przycisk_kolo_ratunkowe.grid()
przycisk_koniec_gry.grid()
glowneOkno.mainloop()

#### a tutaj slajd nr 1- powitalny ###

from tkinter import *
from PIL import Image,ImageTk
glowneOkno=Tk()
glowneOkno.title("Postaw na milion")
glowneOkno.geometry("400x400")

plotno=Canvas(glowneOkno,width=400, height=400)
plotno.pack()
obraz= Image.open("1.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200, image=obrazTk)


glowneOkno.mainloop()


### tu jest "slajd" nr 2 ( zdj nr 2) i możliwość wpisania imienia, ALE program nie zapamietuje JESZCZE tego imienia###

import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk


glowneOkno=tk.Tk()
glowneOkno.title( "Postaw na milion" )
text = tk.StringVar()


plotno=Canvas(glowneOkno,width=400, height=400)
plotno.pack()
obraz= Image.open("2.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200, image=obrazTk)

description = tk.Label(glowneOkno, text="Wpisz imię:").pack()
name = tk.Entry(glowneOkno,width=40)
name.pack()
def imie():
    text.set("Witaj".format(name.get()))
okno_prosi_o_imie = tk.Button(glowneOkno, text="OK", width=20, command=imie)
okno_prosi_o_imie.pack()
imie2 = Entry(root)
def zapamietaj():
    a = imie2.get()
    root.destroy()
    
    global name
    name=[a]

tk.mainloop()

### wstawiam całość z tego 1 pytania pierwszego, potem się to zmontuje
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

glowneOkno=tk.Tk()
glowneOkno.title( "Postaw na milion" )
text = tk.StringVar()
# te 3 poniżej wypadną, jesli zmienimy kocepcję okien do odpowiedzi (są do koncepcji z osobnym oknem pytań)
'''
okno_pytan=tk.Tk()
okno_pytan.title( "Pytanie" )
text = tk.StringVar()
'''

plotno=Canvas(glowneOkno,width=400, height=400)
plotno.pack()
obraz= Image.open("2.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200, image=obrazTk)

description = tk.Label(glowneOkno, text="Wpisz imię:").pack()
name = tk.Entry(glowneOkno,width=40)
name.pack()
def imie():
    messagebox.showinfo("Witaj", name.get())
okno_prosi_o_imie = tk.Button(glowneOkno, text="OK", width=20, command=imie)
okno_prosi_o_imie.pack()
imie2 = Entry(root)
def zapamietaj():
    a = imie2.get()
    root.destroy()
    
    global name
    name=[a]
#etykieta = Label(male_okno, text=name)
#etykieta.pack()

etykieta = Label(glowneOkno, text="Ile to jest 2 razy 2?")
etykieta.pack()
description = tk.Label(glowneOkno, text="Ile paczek obstawiasz?:").pack()
description = tk.Label(glowneOkno, text="A:1").pack()
A = tk.Entry(glowneOkno,width=40)
A.pack()
description = tk.Label(glowneOkno, text="B:4").pack()
B = tk.Entry(glowneOkno,width=40,text="B")
B.pack()
description = tk.Label(glowneOkno, text="C:500").pack()
C = tk.Entry(glowneOkno,width=40)
C.pack()
'''
description = tk.Label(glowneOkno, text="D:2").pack()
D = tk.Entry(glowneOkno,width=40)
D.pack()
description = tk.Label(glowneOkno, text="E:5").pack()
E = tk.Entry(glowneOkno,width=40)
E.pack()
description = tk.Label(glowneOkno, text="F:7").pack()
F = tk.Entry(glowneOkno,width=40)
F.pack()
'''
def odp():
    if A:
        print("To jest tylko przykład")#Dokładnie, dziewczyny, to tylko przykład, a "if A" nie będzie działać, nad tym trzeba pomyśleć
    #tu wpiszemy co się dzieje jeśli się ileś tam obstawi na jakąś odpowiedź
okno_do_odp = tk.Button(glowneOkno, text="OK", width=20, command=odp)
okno_do_odp.pack()
###
'''
#to jest tylko początek do koncepcji z oknem z pytaniami osobno
#tu zaczyna się usuwanie poprzedniego okna z pytaniem, by wyświetlić kolejne
okno_pytan2=tk.Tk()
okno_pytan2.title( "Pytanie" )
text = tk.StringVar()
def nastepne():
    okno_pytan.destroy()
    noweokno()
def noweokno():
    global dalej
    dalej = Button(okno_pytan, text="dalej",command = nastepne)
noweokno()
'''
tk.mainloop()
#######
'''
#######
    while dlugosc>0:
        wylosowana=random.choice(lista)
        if wylosowana== lista[0]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            print("Ile paczek obstawiasz na odpowiedź E?")
            e=int(input())
            print("Ile paczek obstawiasz na odpowiedź F?")
            f=int(input())
            while a+b+c+d+e+f< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
                print("Ile paczek obstawiasz na odpowiedź E?")
                e=int(input())
                print("Ile paczek obstawiasz na odpowiedź F?")
                f=int(input())
            if a+b+c+d+e+f== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if  b!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="Nie"and b!=0 or kolo_ratunkowe=="NIE" and b!=0:
                    suma_paczek=suma_paczek-a-c-d-e-f
                    print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    suma_paczek=suma_paczek-a-c-d-e-f
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif b==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="Nie"and b==0 or kolo_ratunkowe=="NIE" and b==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        print("Ile paczek obstawiasz na odpowiedź D?")
                        d=int(input())
                        print("Ile paczek obstawiasz na odpowiedź E?")
                        e=int(input())
                        print("Ile paczek obstawiasz na odpowiedź F?")
                        f=int(input())
                        while a+b+c+d+e+f< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                            print("Ile paczek obstawiasz na odpowiedź D?")
                            d=int(input())
                            print("Ile paczek obstawiasz na odpowiedź E?")
                            e=int(input())
                            print("Ile paczek obstawiasz na odpowiedź F?")
                            f=int(input())
                        if b!=0:
                            suma_paczek=suma_paczek-a-c-d-e-f
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif b==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d,"E:", e, "F:",f)
                        if b!=0:
                            suma_paczek=suma_paczek-a-c-d-e-f
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif b==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")

        elif wylosowana== lista[1]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            print("Ile paczek obstawiasz na odpowiedź E?")
            e=int(input())
            while a+b+c+d+e< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
                print("Ile paczek obstawiasz na odpowiedź E?")
                e=int(input())
            if a+b+c+d+e== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b-c-d-e
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        print("Ile paczek obstawiasz na odpowiedź D?")
                        d=int(input())
                        print("Ile paczek obstawiasz na odpowiedź E?")
                        e=int(input())
                        while a+b+c+d+e< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                            print("Ile paczek obstawiasz na odpowiedź D?")
                            d=int(input())
                            print("Ile paczek obstawiasz na odpowiedź E?")
                            e=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d-e
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d,"E:", e)
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d-e
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")
        elif wylosowana==lista[2]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            while a+b+c+d<suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
            if a+b+c+d== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b-c-d
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        print("Ile paczek obstawiasz na odpowiedź D?")
                        d=int(input())
                        while a+b+c+d< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                            print("Ile paczek obstawiasz na odpowiedź D?")
                            d=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d)
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")
        elif wylosowana==lista[3]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            while a+b+c< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
            if a+b+c== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b-c
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        while a+b+c< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b-c
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c)
                        if a!=0:
                            suma_paczek=suma_paczek-b-c
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("NIe masz tyle paczek. Losujemy jeszcze raz.")
        elif wylosowana==lista[4]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            while a+b< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
            if a+b== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        while a+b< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b)
                        if a!=0:
                            suma_paczek=suma_paczek-b
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")

else:
    print("W takim razie czy chcesz przerwać grę?")
    przerwac=input()
    if przerwac=="Nie" or przerwac=="nie" or przerwac=="NIE":
        print("Kontynuujemy grę!")
        lista=["Ile to jest 2 razy 2? A:1, B:4, C:500, D:2, E:5, F:7","Jak nazywa się znany skoczek narciarski? A:Małysz, B:Żak, C:Kowalski, D:Mickiewicz, E:Stachurski", "Żółta łódź podwodna to statek: A:Beatlesów B:Doorsów C:Pearl Jamu D:Joy Division?", "Kim była Ariel z filmu Disneya? A:Syrenką B:Elfem  C:Indianką ", "Gdyby całe wydobyte w historii złoto przetopić w jeden sześcian, to miałby bok o długości: A:20,5 m  B:205 m ? "]
        koloR=["kolo_R"]
        suma_pieniędzy=1000000
        suma_paczek=40
        dlugosc=len(lista)
    while dlugosc>0:
        wylosowana=random.choice(lista)
        if wylosowana== lista[0]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            print("Ile paczek obstawiasz na odpowiedź E?")
            e=int(input())
            print("Ile paczek obstawiasz na odpowiedź F?")
            f=int(input())
            while a+b+c+d+e+f< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
                print("Ile paczek obstawiasz na odpowiedź E?")
                e=int(input())
                print("Ile paczek obstawiasz na odpowiedź F?")
                f=int(input())
            if a+b+c+d+e+f== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if  b!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="Nie"and b!=0 or kolo_ratunkowe=="NIE" and b!=0:
                    suma_paczek=suma_paczek-a-c-d-e-f
                    print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    suma_paczek=suma_paczek-a-c-d-e-f
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif b==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="Nie"and b==0 or kolo_ratunkowe=="NIE" and b==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        print("Ile paczek obstawiasz na odpowiedź D?")
                        d=int(input())
                        print("Ile paczek obstawiasz na odpowiedź E?")
                        e=int(input())
                        print("Ile paczek obstawiasz na odpowiedź F?")
                        f=int(input())
                        while a+b+c+d+e+f< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                            print("Ile paczek obstawiasz na odpowiedź D?")
                            d=int(input())
                            print("Ile paczek obstawiasz na odpowiedź E?")
                            e=int(input())
                            print("Ile paczek obstawiasz na odpowiedź F?")
                            f=int(input())
                        if b!=0:
                            suma_paczek=suma_paczek-a-c-d-e-f
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif b==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d,"E:", e, "F:",f)
                        if b!=0:
                            suma_paczek=suma_paczek-a-c-d-e-f
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif b==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")

        elif wylosowana== lista[1]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            print("Ile paczek obstawiasz na odpowiedź E?")
            e=int(input())
            while a+b+c+d+e< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
                print("Ile paczek obstawiasz na odpowiedź E?")
                e=int(input())
            if a+b+c+d+e== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b-c-d-e
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        print("Ile paczek obstawiasz na odpowiedź D?")
                        d=int(input())
                        print("Ile paczek obstawiasz na odpowiedź E?")
                        e=int(input())
                        while a+b+c+d+e< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                            print("Ile paczek obstawiasz na odpowiedź D?")
                            d=int(input())
                            print("Ile paczek obstawiasz na odpowiedź E?")
                            e=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d-e
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d,"E:", e)
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d-e
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")
        elif wylosowana==lista[2]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            while a+b+c+d<suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
            if a+b+c+d== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b-c-d
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        print("Ile paczek obstawiasz na odpowiedź D?")
                        d=int(input())
                        while a+b+c+d< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                            print("Ile paczek obstawiasz na odpowiedź D?")
                            d=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d)
                        if a!=0:
                            suma_paczek=suma_paczek-b-c-d
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")
        elif wylosowana==lista[3]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            while a+b+c< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
            if a+b+c== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b-c
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        print("Ile paczek obstawiasz na odpowiedź C?")
                        c=int(input())
                        while a+b+c< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                            print("Ile paczek obstawiasz na odpowiedź C?")
                            c=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b-c
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b,"C:", c)
                        if a!=0:
                            suma_paczek=suma_paczek-b-c
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("NIe masz tyle paczek. Losujemy jeszcze raz.")
        elif wylosowana==lista[4]:
            print(wylosowana)
            print("Czas start!")
            for k in range(1,61):
                print(k)
                time.sleep(1)
                if k == 30:
                    print("Minęła połowa czasu")
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            while a+b< suma_paczek:
                print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
            if a+b== suma_paczek:
                print("Czy chcesz skorzystać z koła ratunkowego?")
                kolo_ratunkowe=input()
                if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                    suma_paczek=suma_paczek-b
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
                else:
                    if koloR!=[]:
                        print("Skorzystajmy zatem z koła ratunkowego!")
                        print("Czas start!")
                        for k in range(1,21):
                            print(k)
                            time.sleep(1)
                            if k == 10:
                                print("Minęła połowa czasu")
                        print("Koniec czasu.")
                        print("Ile paczek obstawiasz na odpowiedź A?")
                        a=int(input())
                        print("Ile paczek obstawiasz na odpowiedź B?")
                        b=int(input())
                        while a+b< suma_paczek:
                            print("Nie skorzystałeś ze wszystkich paczek, ułóż paczki ponownie.")
                            print("Ile paczek obstawiasz na odpowiedź A?")
                            a=int(input())
                            print("Ile paczek obstawiasz na odpowiedź B?")
                            b=int(input())
                        if a!=0:
                            suma_paczek=suma_paczek-b
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            koloR.remove(koloR[0])
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                            break
                    else:
                        print("Wykorzystałeś już koło ratunkowe")
                        print("Obstawiłeś: A:", a, "B:", b)
                        if a!=0:
                            suma_paczek=suma_paczek-b
                            dlugosc=dlugosc-1
                            lista.remove(wylosowana)
                            print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
                        elif a==0:
                            print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
            else:
                print("Nie masz tyle paczek. Losujemy jeszcze raz.")

        suma_pieniędzy=suma_paczek*2500
        print("To koniec gry! Udało Ci się wygrać", suma_pieniędzy, "złotych!")
    else:
        print("W takim razie żegnamy Cię", imie)
'''
