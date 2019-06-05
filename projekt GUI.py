import random
import time
print("Witam serdecznie w programie Postaw na milion! Jest z nami uczestnik gry. Jak masz na imię?")
imie=input()
print("Witamy Cię," ,imie,". Przypominam, że masz możliwość wyboru jednorazowego koła ratunkowego, jakim jest dodatkowe 20 sekund na odpowiedź, a na każdą odpowiedź masz 60 sekund. \nMasz do dyspozycji cały milion złotych! Podzieliliśmy go na 40 paczek po 25000 złotych. W zależności od tego ile obstawisz na poprawną odpowiedź, z taką kwotą przechodzisz do następnego etapu. Czy możemy zaczynać grę?")
zaczynacczynie=input()
if zaczynacczynie=="Tak" or zaczynacczynie=="tak" or zaczynacczynie=="TAK":
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
