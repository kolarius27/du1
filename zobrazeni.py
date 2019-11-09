from math import log, sin, radians, tan
from turtle import speed, penup, pendown, setpos, seth, forward, dot, stamp, color, exitonclick


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
    if zobrazeni == "A":
        souradnice_y = float(polomer_zeme * sirka_rad * 1000000 / meritko)
    if zobrazeni == "B":
        souradnice_y = float(2 * polomer_zeme * tan(sirka_rad / 2) * 1000000 / meritko)
    if zobrazeni == "M":
        doplnek = 90 - sirka_rad
        if doplnek < 4.948871:
            doplnek = 4.948871
        if doplnek > 175.051129:
            doplnek = 175.051129
        doplneka_rad = radians(doplnek)
        souradnice_y = float(polomer_zeme * log(1 / tan(drad / 2)) * 1000000 / meritko)
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
        # Opakovane se vyvolava funkce input
        meritko = int(input("Zadejte měřítko: "))
        while meritko < 0 or meritko == 0:
            # Pri vstupu m <= 0 je opet vyvolana funkce input
            print("Chybný vstup! Zadej znovu!")
            meritko = int(input("Zadejte měřítko: "))
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    else:
        # Pri korektnim vstupu program ukonci while cycle
        break

print("\nNyní zadejte poloměr referenční koule, se kterým chcete počítat.\n"
      "Pokud chcete počítat s poloměrem 6371,11 km, stačí zadat hodnotu 0.\n\n")
polomer_zeme = float()
while True:
    try:
        # Opakovane se vyvolava funkce input
        polomer_zeme = float(input("Zadejte poloměr Země (v km): "))
        while polomer_zeme < 0:
            # Pri vstupu r < 0 je opet vyvolana funkce input
            print("Chybný vstup! Zadej znovu!")
            polomer_zeme = float(input("Zadejte poloměr Země (v km): "))
        while polomer_zeme == 0:
            # Pri vstupu r = 0 je promenne prirazena konstanta
            polomer_zeme = 6371.11
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    else:
        # Pri korektnim vstupu program ukonci while cycle
        break

# Vytvari se dva listy, poledniky pro nasledny print a pzelva pro turtle graphics
poledniky = []
pzelva = []

for i in range(37):
    # Generuje poledniky po 10° a nasledne vypocte souradnice x pomoci funkce vypocet_souradnice_x
    delka = int(-180 + i * 10)
    xround = vypocet_souradnice_x(delka, meritko, polomer_zeme)
    # Pokud je vzdalenost vetsi nez 1 m, prirazuje se promenne hodnota -
    # Prirazeni do listu pzelva
    if abs(xround) > 100:
        xround = "-"
    # do tuple se ukladaji dvojice zemepisnych a vypoctenych souradnic
    poledniky.append(xround)
    if xround == '-':
        pzelva.append(xround)
    else:
        pzelva.append(xround*10)


# Vytvari se dva listy, rovnobezky pro nasledny print a rzelva pro turtle graphics
rovnobezky = []
rzelva = []

for j in range(19):
    # Generuje rovnobezky po 10° a nasledne vypocte souradnice y pomoci funkce vypocet_souradnice_y
    sirka = int(-90 + j*10)
    yround = vypocet_souradnice_y(sirka,zobrazeni,meritko,polomer_zeme)
    if abs(yround) > 100:
        yround = "-"
    rovnobezky.append(yround)
    if yround == '-':
        rzelva.append(yround)
    else:
        rzelva.append(yround*10)

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
        bodyY.append(ybod*10)
        xbod = vypocet_souradnice_x(xvstup,meritko,polomer_zeme)
        bodyX.append(xbod*10)
        print("Souřadnice hledaného bodu jsou: (", xbod, ",", ybod, ")")
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    if souradnice_xy == (0.0, 0.0):
        # While cycle je ukoncen vstupnimi hodnotami 0, 0
        break

if '-' in rzelva or '-' in pzelva:
    # Kdyz list obsahuje i neciselne hodnoty, turtle graphics neprobehne
    print("Vzdálenosti jsou příliš velké, želvička by to neušla!")
else:
    # Pokud list obsahuje pouze ciselne hodnoty, souradnicova sit je vykreslena
    speed(10)
    for i in range(37):
        # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany poledniky
        penup()
        setpos(pzelva[i], rzelva[0])
        seth(90)
        pendown()
        forward(abs(max(rzelva)-min(rzelva)))
    for j in range(19):
        # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany rovnobezky
        penup()
        setpos(pzelva[0], rzelva[j])
        seth(0)
        pendown()
        forward(abs(max(pzelva) - min(pzelva)))
    for k in range(len(bodyX)):
        # Zelva vyznaci konkretni body vyhledane uzivatelem modrou teckou
        speed(1)
        penup()
        setpos(bodyX[k], bodyY[k])
        pendown()
        dot(10, "blue")
    exitonclick()

print("\nDěkuji za použití programu zobrazeni.py, brzy naviděnou!")


