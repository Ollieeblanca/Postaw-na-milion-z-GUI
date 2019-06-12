### poniżej zmontowany kod, powiedzmy, że całość, ale niektóre rzeczy trzeba dopracować, np funkcje nowe okno ###
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



### nie usuwałam tego poniżej, bo to kod z możliwością zapamiętania - może się przydać###
'''
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
root=Tk()
imie2 = Entry(root)
A = Entry(root)
B = Entry(root)
C = Entry(root)
D = Entry(root)
E = Entry(root)
F = Entry(root)

def zapamietaj():
    a = imie2.get()
    b = A.get()
    c = B.get()
    d = C.get()
    e = D.get()
    f = E.get()
    g = F.get()
    
    root.destroy()
    
    global par
    par=[a,b,c,d,e,f,g]

tk.mainloop()
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
