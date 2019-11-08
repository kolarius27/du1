from math import log, sin, radians, tan
from turtle import speed, penup, pendown, setpos, seth, forward, exitonclick


def vypocet_souradnice_x(u,m,r):
    # Prevod vstupu na radiany, vypocet souradnice x a zaokrouhleni na jedno desetinne misto
    urad = radians(u)
    x = float(r * urad * 1000000 / m)
    return round(x, 1)

def vypocet_souradnice_y(v,z,m,r):
    # Prevod vstupu na radiany a vytvoreni promenne y
    vrad = radians(v)
    y = float()
    # Vypocet promenne y v zavislosti na zadanem parametru z
    if z == "L":
        y = float(r * sin(vrad) * 1000000 / m)
    if z == "A":
        y = float(r * vrad * 1000000 / m)
    if z == "B":
        y = float(2 * r * tan(vrad / 2) * 1000000 / m)
    if z == "M":
        d = 90 - v
        if d < 4.948871:
            d = 4.948871
        if d > 175.051129:
            d = 175.051129
        drad = radians(d)
        y = float(r * log(1 / tan(drad / 2)) * 1000000 / m)
    # Vystupem je zaokrouhlena hodnota na jedno desetinne misto
    return round(y, 1)

print("Vítejte v programu LAMB.exe!\n\n"
      "Program umožňuje vypočítat souřadnice válcových tečných zobrazení.\n"
      "Pro výpočet Lambertova zobrazení zadejte písmeno L.\n"
      "Pro výpočet Marinova zobrazení zadejte písmeno A.\n"
      "Pro výpočet Mercatorova zobrazení zadejte písmeno M.\n"
      "Pro výpočet Braunova zobrazení zadejte písmeno B.\n\n")
z = input("Zadejte zobrazení: ")
correct_z = ("L", "A", "B", "M")
while z not in correct_z:
    # Pomoci promenne correct_z opakovane vyvola funkci input
    print("Chybný vstup! Zadej znovu!")
    z = input("Zadejte zobrazení: ")

print("\nDále je potřeba zadat měřítko. Pokud chcete například měřítko 1:1000000000, stačí zadat do programu 1000000000.\n\n")
m = int()
while True:
    try:
        # Opakovane se vyvolava funkce input
        m = int(input("Zadejte měřítko: "))
        while m < 0 or m == 0:
            # Pri vstupu m <= 0 je opet vyvolana funkce input
            print("Chybný vstup! Zadej znovu!")
            m = int(input("Zadejte měřítko: "))
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    else:
        # Pri korektnim vstupu program ukonci while cycle
        break

print("\nNyní zadejte poloměr referenční koule, se kterým chcete počítat.\n"
      "Pokud chcete počítat s poloměrem 6371,11 km, stačí zadat hodnotu 0.\n\n")
r = float()
while True:
    try:
        # Opakovane se vyvolava funkce input
        r = float(input("Zadejte poloměr Země (v km): "))
        while r < 0:
            # Pri vstupu r < 0 je opet vyvolana funkce input
            print("Chybný vstup! Zadej znovu!")
            r = float(input("Zadejte poloměr Země (v km): "))
        while r == 0:
            # Pri vstupu r = 0 je promenne prirazena konstanta
            r = 6371.11
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    else:
        # Pri korektnim vstupu program ukonci while cycle
        break

# Vytvari se dva listy, Poledniky pro nasledny print a pzelva pro turtle graphics
Poledniky = []
pzelva = []

for i in range(37):
    # Generuje poledniky po 10° a nasledne vypocte souradnice x pomoci funkce vypocet_souradnice_x
    u = int(-180 + i * 10)
    xround = vypocet_souradnice_x(u, m, r)
    # Pokud je vzdalenost vetsi nez 1 m, prirazuje se promenne hodnota -
    # Prirazeni do listu pzelva
    if abs(xround) > 100:
        xround = "-"
    # do tuple se ukladaji dvojice zemepisnych a vypoctenych souradnic
    tp = (u, xround)
    Poledniky.append(tp)
    if xround == '-':
        pzelva.append(xround)
    else:
        pzelva.append(xround*10)


# Vytvari se dva listy, Rovnobezky pro nasledny print a rzelva pro turtle graphics
Rovnobezky = []
rzelva = []

for j in range(19):
    # Generuje rovnobezky po 10° a nasledne vypocte souradnice y pomoci funkce vypocet_souradnice_y
    v = int(-90 + j*10)
    yround = vypocet_souradnice_y(v,z,m,r)
    if abs(yround) > 100:
        yround = "-"
    tr = (v,yround)
    Rovnobezky.append(tr)
    if yround == '-':
        rzelva.append(yround)
    else:
        rzelva.append(yround*10)

print("\nZde jsou vypsané souřadnice rovnoběžek a poledníků po 10°. \n"
      "V kulatých závorkách naleznete zeměpisnou šířku/délku a vypočtenou souřadnici zobrazení.\n")
print("Rovnoběžky: ", Rovnobezky)
print("Poledníky: ", Poledniky)

print("\n\nPokud vám toto nestačí, nyní máte možnost vypočítat konkrétní body.\n"
      "Při zadání bodu (0,0) program přejde na vykreslení souřadnicové sítě želví grafikou.\n")
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
        souradnice = (yvstup,xvstup)
        # Vypocet souradnic pomoci vyse vytvorenych funkci
        ybod = vypocet_souradnice_y(yvstup,z,m,r)
        xbod = vypocet_souradnice_x(xvstup,m,r)
        print("Souřadnice hledaného bodu jsou: (", xbod, ",", ybod, ")")
    except ValueError:
        # Pri neciselnem vstupu je opet vyvolana funkce input
        print("Chybný vstup! Zadej znovu!")
        continue
    if souradnice == (0.0, 0.0):
        # While cycle je ukoncen vstupnimi hodnotami 0, 0
        break

if '-' in rzelva or '-' in pzelva:
    # Kdyz list obsahuje i neciselne hodnoty, turtle graphics neprobehne
    print("Vzdálenosti jsou příliš velké, želvička by to neušla!")
else:
    # Pokud list obsahuje pouze ciselne hodnoty, souradnicova sit je vykreslena
    speed(10)
    for k in range(37):
        # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany poledniky
        penup()
        setpos(pzelva[k], rzelva[0])
        seth(90)
        pendown()
        forward(abs(max(rzelva)-min(rzelva)))
    for l in range(19):
        # Zelva je umistena do bodu s nejnizsimi hodnotami souradnic a jsou vygenerovany rovnobezky
        penup()
        setpos(pzelva[0], rzelva[l])
        seth(0)
        pendown()
        forward(abs(max(pzelva) - min(pzelva)))

    exitonclick()

print("\nDěkuji za použití programu LAMB.exe, brzy naviděnou!")


