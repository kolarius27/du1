from math import log, sin, radians, tan, inf
from turtle import speed, penup, pendown, setpos, seth, forward, dot, pencolor, screensize, exitonclick


def vypocet_souradnice_x(delka, meritko, polomer_zeme):
    # Prevod vstupu na radiany, vypocet souradnice_x a zaokrouhleni na jedno desetinne misto
    delka_rad = radians(delka)
    souradnice_x = float(polomer_zeme * delka_rad * 100000 / meritko)
    return round(souradnice_x, 1)


def vypocet_souradnice_y(sirka, zobrazeni, meritko, polomer_zeme):
    # Prevod vstupu na radiany a vytvoreni promenne souradnice_y
    sirka_rad = radians(sirka)
    souradnice_y = float()
    # Vypocet promenne souradnice_y v zavislosti na zadanem parametru zobrazeni
    if zobrazeni == "L":
        souradnice_y = float(polomer_zeme * sin(sirka_rad) * 100000 / meritko)
    elif zobrazeni == "A":
        souradnice_y = float(polomer_zeme * sirka_rad * 100000 / meritko)
    elif zobrazeni == "B":
        souradnice_y = float(2 * polomer_zeme * tan(sirka_rad / 2) * 100000 / meritko)
    elif zobrazeni == "M":
        doplnek = 90 - sirka
        doplnek_rad = radians(doplnek)
        if doplnek == 0:
            souradnice_y = inf
        elif doplnek == 180:
            souradnice_y = -inf
        else:
            souradnice_y = float(polomer_zeme * log(1 / tan(doplnek_rad / 2)) * 100000 / meritko)
    # Vystupem je zaokrouhlena hodnota na jedno desetinne misto
    return round(souradnice_y, 1)


def vykresleni_site(pzelva, rzelva, bodyX, bodyY, zobrazeni):
    speed(10)
    # Promenne delka_poledniku a delka_rovnobezky jsou samodefinujici
    delka_poledniku = abs(max(rzelva) - min(rzelva))
    delka_rovnobezky = abs(max(pzelva) - min(pzelva))
    # Pomoci screensize se vygeneruje dostatecne velke okno
    screensize(delka_rovnobezky + 100, delka_poledniku + 100)
    for i in range(37):
        penup()
        pencolor("black")
        if i == 18:
            # nulty polednik je zobrazen cervene
            pencolor("red")
        # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany poledniky
        setpos(pzelva[i], rzelva[0])
        seth(90)
        pendown()
        forward(delka_poledniku)
        penup()
    for j in range(19):
        # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany rovnobezky
        penup()
        pencolor("black")
        setpos(pzelva[0], rzelva[j])
        seth(0)
        if j == 9:
            # rovnik je zobrazen cervene
            pencolor("red")
        if zobrazeni == "M" and (j == 0 or j == 18):
            continue
        pendown()
        forward(delka_rovnobezky)
        penup()
    for k in range(len(bodyX)):
        # Zelva vyznaci konkretni body vyhledane uzivatelem modrou teckou
        speed(1)
        penup()
        setpos(bodyX[k], bodyY[k])
        pendown()
        dot(10, "blue")
        penup()
    exitonclick()


print("Vítejte v programu zobrazeni.py!\n\n"
      "Program umožňuje vypočítat souřadnice válcových tečných zobrazení.\n"
      "Pro výpočet Lambertova zobrazení zadejte písmeno L.\n"
      "Pro výpočet Marinova zobrazení zadejte písmeno A.\n"
      "Pro výpočet Mercatorova zobrazení zadejte písmeno M.\n"
      "Pro výpočet Braunova zobrazení zadejte písmeno B.\n\n")
zobrazeni = input("Zadejte zobrazení: ")
spravne_zobrazeni = ("L", "A", "B", "M")
while zobrazeni not in spravne_zobrazeni:
    # Pomoci promenne spravne_zobrazeni opakovane vyvola funkci input
    print("Chybný vstup! Zadej znovu!")
    zobrazeni = input("Zadejte zobrazení: ")


print("\nDále je potřeba zadat měřítko. Pokud chcete například měřítko 1:100000000, stačí zadat do programu 100000000.\n\n")
meritko = 0
while True:
    # opakovane vyvolava input, pokud je vstup neciselny nebo <= 0
    try:
        meritko = int(input("Zadejte měřítko: "))
        if meritko <= 0:
            print("Chybný vstup! Zadej znovu!")
            continue
        # pokud je vstup korektni, vyskakuje z cyklu
        break
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue


print("\nNyní zadejte poloměr referenční koule, se kterým chcete počítat.\n"
      "Pokud chcete počítat s poloměrem 6371,11 km, stačí zadat hodnotu 0.\n\n")
polomer_zeme = float()
while True:
    try:
        # Opakovane se vyvolava funkce input
        polomer_zeme = float(input("Zadejte poloměr Země (v km): "))
        if polomer_zeme < 0:
            # Pri vstupu r < 0 je opet vyvolana funkce input
            print("Chybný vstup! Zadej znovu!")
            continue
        elif polomer_zeme == 0:
            # Pri vstupu r = 0 je promenne prirazena konstanta
            polomer_zeme = 6371.11
        # Pri korektnim vstupu program ukonci while cycle
        break
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue


# Vytvari se list poledniky pro nasledny print a pzelva pro turtle graphics
poledniky = []
pzelva = []
for delka in range(-180, 190, 10):
    # Generuje poledniky po 10° a nasledne vypocte souradnice x pomoci funkce vypocet_souradnice_x
    xround = vypocet_souradnice_x(delka, meritko, polomer_zeme)
    # Prirazeni do listu pzelva
    pzelva.append(xround * 10)
    # Pokud je vzdalenost vetsi nez 1 m, prirazuje se promenne xround hodnota -
    if abs(xround) > 100:
        xround = "-"
    poledniky.append(xround)


# Vytvari se dva listy, rovnobezky pro nasledny print a rzelva pro turtle graphics
rovnobezky = []
rzelva = []
for sirka in range(-90, 100, 10):
    # Generuje rovnobezky po 10° a nasledne vypocte souradnice y pomoci funkce vypocet_souradnice_y
    yround = vypocet_souradnice_y(sirka, zobrazeni, meritko, polomer_zeme)
    # Prirazeni do listu pzelva, osetruji se nekonecna u Mercatorova zobrazeni
    if yround == inf:
        rzelva.append(vypocet_souradnice_y(85.051129, zobrazeni, meritko, polomer_zeme) * 10)
    elif yround == -inf:
        rzelva.append(vypocet_souradnice_y(-85.051129, zobrazeni, meritko, polomer_zeme) * 10)
    else:
        rzelva.append(yround * 10)
    if abs(yround) > 100:
        yround = "-"
    rovnobezky.append(yround)


print("\nZde jsou vypsané souřadnice rovnoběžek a poledníků po 10°. \n"
      "V kulatých závorkách naleznete zeměpisnou šířku/délku a vypočtenou souřadnici zobrazení.\n")
print("Rovnoběžky: ", rovnobezky)
print("Poledníky: ", poledniky)

print("\n\nPokud vám toto nestačí, nyní máte možnost vypočítat konkrétní body.\n"
      "Při zadání bodu (0,0) program přejde na vykreslení souřadnicové sítě želví grafikou.\n")
bodyY = []
bodyX = []
while True:
    try:
        # Vyvolava input pro zemepisnou sirku/delku, pri neexistujicich hodnotach vyvola input znovu
        yvstup = float(input("Vložte zeměpisnou šířku: "))
        while yvstup > 90 or yvstup < -90:
            print("Chybný vstup! Zadej znovu!")
            yvstup = float(input("Vložte zeměpisnou šířku: "))
        xvstup = float(input("Vložte zeměpisnou délku: "))
        while xvstup > 180 or xvstup < -180:
            print("Chybný vstup! Zadej znovu!")
            xvstup = float(input("Vložte zeměpisnou délku: "))
        # Do promenne souradnice se zapisuji vstupni hodnoty pro mozne skonceni while cycle
        souradnice_xy = (yvstup, xvstup)
        # Vypocet souradnic pomoci vyse vytvorenych funkci, osetruji se nekonecna u Mercatorova zobrazeni
        ybod = vypocet_souradnice_y(yvstup, zobrazeni, meritko, polomer_zeme)
        xbod = vypocet_souradnice_x(xvstup, meritko, polomer_zeme)
        print("Souřadnice hledaného bodu jsou: (", ybod, ",", xbod, ")")
        if abs(ybod) == inf:
            continue
        bodyY.append(ybod * 10)
        bodyX.append(xbod * 10)
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    if souradnice_xy == (0.0, 0.0):
        # While cycle je ukoncen vstupnimi hodnotami 0, 0
        break

# Nakonec je vykreslena souradnicova sit pomoci zelvi grafiky
vykresleni_site(pzelva, rzelva, bodyX, bodyY, zobrazeni)

print("\nDěkuji za použití programu zobrazeni.py, brzy naviděnou!")


