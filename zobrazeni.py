from math import log, sin, radians, tan, inf
from turtle import speed, penup, pendown, setpos, seth, forward, dot, pencolor, screensize, exitonclick


def vypocet_souradnice_x(delka,meritko,polomer_zeme):
    # Prevod vstupu na radiany, vypocet souradnice x a zaokrouhleni na jedno desetinne misto
    delka_rad = radians(delka)
    souradnice_x = float(polomer_zeme * delka_rad * 1000000 / meritko)
    return round(souradnice_x, 1)

def vypocet_souradnice_y(sirka,zobrazeni,meritko,polomer_zeme):
    # Prevod vstupu na radiany a vytvoreni promenne y
    sirka_rad = radians(sirka)
    souradnice_y = float()
    # Vypocet promenne y v zavislosti na zadanem parametru z
    if zobrazeni == "L":
        souradnice_y = float(polomer_zeme * sin(sirka_rad) * 1000000 / meritko)
    elif zobrazeni == "A":
        souradnice_y = float(polomer_zeme * sirka_rad * 1000000 / meritko)
    elif zobrazeni == "B":
        souradnice_y = float(2 * polomer_zeme * tan(sirka_rad / 2) * 1000000 / meritko)
    elif zobrazeni == "M":
        doplnek = 90 - sirka
        doplnek_rad = radians(doplnek)
        if doplnek == 0:
            souradnice_y = inf
        elif doplnek == 180:
            souradnice_y = -inf
        else:
            souradnice_y = float(polomer_zeme * log(1 / tan(doplnek_rad / 2)) * 1000000 / meritko)
    # Vystupem je zaokrouhlena hodnota na jedno desetinne misto
    return round(souradnice_y, 1)

print("Vítejte v programu zobrazeni.py!\n\n"
      "Program umožňuje vypočítat souřadnice válcových tečných zobrazení.\n"
      "Pro výpočet Lambertova zobrazení zadejte písmeno L.\n"
      "Pro výpočet Marinova zobrazení zadejte písmeno A.\n"
      "Pro výpočet Mercatorova zobrazení zadejte písmeno M.\n"
      "Pro výpočet Braunova zobrazení zadejte písmeno B.\n\n")
zobrazeni = input("Zadejte zobrazení: ")
spravne_zobrazeni = ("L", "A", "B", "M")
while zobrazeni not in spravne_zobrazeni:
    # Pomoci promenne correct_z opakovane vyvola funkci input
    print("Chybný vstup! Zadej znovu!")
    zobrazeni = input("Zadejte zobrazení: ")

print("\nDále je potřeba zadat měřítko. Pokud chcete například měřítko 1:1000000000, stačí zadat do programu 1000000000.\n\n")
meritko = int()
while True:
    try:
        meritko = int(input("Zadejte měřítko: "))
        if meritko < 0 or meritko == 0:
            print("Chybný vstup! Zadej znovu!")
            continue
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
            polomer_zeme = float(input("Zadejte poloměr Země (v km): "))
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
for i in range(37):
    # Generuje poledniky po 10° a nasledne vypocte souradnice x pomoci funkce vypocet_souradnice_x
    delka = int(-180 + i * 10)
    xround = vypocet_souradnice_x(delka, meritko, polomer_zeme)
    # Prirazeni do listu pzelva

    # Pokud je vzdalenost vetsi nez 1 m, prirazuje se promenne hodnota -
    if xround > 100:
        pzelva.append(1000)
        xround = "-"
    elif xround < -100:
        pzelva.append(-1000)
        xround = "-"
    else:
        pzelva.append(xround * 10)
    # do tuple se ukladaji dvojice zemepisnych a vypoctenych souradnic
    poledniky.append(xround)


# Vytvari se dva listy, rovnobezky pro nasledny print a rzelva pro turtle graphics
rovnobezky = []
rzelva = []
for j in range(19):
    # Generuje rovnobezky po 10° a nasledne vypocte souradnice y pomoci funkce vypocet_souradnice_y
    sirka = int(-90 + j*10)
    yround = vypocet_souradnice_y(sirka,zobrazeni,meritko,polomer_zeme)
    if yround > 100:
        rzelva.append(1000)
        yround = "-"
    elif yround < -100:
        rzelva.append(-1000)
        yround = "-"
    else:
        rzelva.append(yround * 10)
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
        souradnice_xy = (yvstup,xvstup)
        # Vypocet souradnic pomoci vyse vytvorenych funkci
        ybod = vypocet_souradnice_y(yvstup,zobrazeni,meritko,polomer_zeme)
        if ybod == inf:
            bodyY.append(vypocet_souradnice_y(85.051129, zobrazeni, meritko, polomer_zeme)*10)
        elif ybod == -inf:
            bodyY.append(vypocet_souradnice_y(-85.051129, zobrazeni, meritko, polomer_zeme)*10)
        elif ybod > 100:
            bodyY.append(1000)
        elif ybod < -100:
            bodyY.append(-1000)
        else:
            bodyY.append(ybod * 10)
        xbod = vypocet_souradnice_x(xvstup,meritko,polomer_zeme)
        if xbod > 100:
            bodyX.append(1000)
        elif xbod < -100:
            bodyX.append(-1000)
        else:
            bodyX.append(xbod * 10)
        print("Souřadnice hledaného bodu jsou: (", xbod, ",", ybod, ")")
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    if souradnice_xy == (0.0, 0.0):
        # While cycle je ukoncen vstupnimi hodnotami 0, 0
        break

print(bodyX)
print(bodyY)


# Nakonec je vykreslena souradnicova sit pomoci zelvi grafiky
speed(10)
delka_poledniku = abs(max(rzelva) - min(rzelva))*10
if zobrazeni == "M":
    delka_poledniku = abs(vypocet_souradnice_y(-85.051129, zobrazeni, meritko, polomer_zeme)
                          - vypocet_souradnice_y(85.051129, zobrazeni, meritko, polomer_zeme)) * 10
delka_rovnobezky = abs(max(pzelva) - min(pzelva)) * 10
screensize(delka_poledniku + 100, delka_rovnobezky + 100)
for i in range(37):
    # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany poledniky
    penup()
    pencolor("black")
    delka_poledniku = abs(max(rzelva) - min(rzelva))
    if i == 18:
        pencolor("red")
    if zobrazeni == "M":
        setpos(pzelva[i], vypocet_souradnice_y(-85.051129, zobrazeni, meritko, polomer_zeme)*10)
    elif delka_poledniku > 1000:
        delka_poledniku = 1000
        setpos(pzelva[i], -500)
    else:
        setpos(pzelva[i], rzelva[0])
    seth(90)
    pendown()
    forward(delka_poledniku)
for j in range(19):
    # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany rovnobezky
    penup()
    pencolor("black")
    if j == 9:
        pencolor("red")
    if zobrazeni != "M" and j != 0 or j != 19:
        setpos(pzelva[0], rzelva[j])
        seth(0)
        pendown()
        forward(delka_rovnobezky)
for k in range(len(bodyX)):
    # Zelva vyznaci konkretni body vyhledane uzivatelem modrou teckou
    speed(1)
    penup()
    setpos(bodyX[k], bodyY[k])
    pendown()
    dot(10, "blue")
exitonclick()

print("\nDěkuji za použití programu zobrazeni.py, brzy naviděnou!")


