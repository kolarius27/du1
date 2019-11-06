def vypocet_souradnice_x(u,m,r):
    from math import radians
    urad = radians(u)
    x = float(r * urad * 1000000 / m)
    return round(x, 1)

def vypocet_souradnice_y(v,z,m,r):
    vrad = radians(v)
    y = float()
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
        if d > 174.948871:
            d = 174.948871
        drad = radians(d)
        y = float(r * log(1 / tan(drad / 2)) * 1000000 / m)
    return round(y, 1)

print("Vítejte v programu pro výpočet válcových tečných zobrazení!")
correct_z = ("L", "A", "B", "M")
z = input("Zadejte zobrazení: ")
while z not in correct_z:
    print("Chybný vstup! Zadej znovu!")
    z = input("Zadejte zobrazení: ")
m = int()
while True:
    try:
        m = int(input("Zadejte měřítko: "))
        if m <= 0:
            print("Chybný vstup! Zadej znovu!")
            m = int(input("Zadejte měřítko: "))
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue
    else:
        break
r = float()
while True:
    try:
        r = float(input("Zadejte poloměr Země (v km): "))
        if r < 0:
            print("Chybný vstup! Zadej znovu!")
            r = float(input("Zadejte poloměr Země (v km): "))
        if r == 0:
            r = 6371.11
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue
    else:
        break

from math import log, sin, radians, tan

Poledniky = []
pzelva = []

for i in range(37):
    u = int(-180 + i * 10)
    xround = vypocet_souradnice_x(u, m, r)
    if abs(xround) > 100:
        xround = "-"
    tp = (u, xround)
    Poledniky.append(tp)
    pzelva.append(xround*10)

Rovnobezky = []
rzelva = []

for j in range(19):
    v = int(-90 + j*10)
    yround = vypocet_souradnice_y(v,z,m,r)
    if abs(yround) > 100:
        yround = "-"
    tr = (v,yround)
    Rovnobezky.append(tr)
    rzelva.append(yround*10)

print("Rovnobezky: ", Rovnobezky)
print("Poledniky: ", Poledniky)

while True:
    try:
        yvstup = float(input("Vložte zeměpisnou šířku: "))
        if yvstup > 90 or yvstup < -90:
            print("Chybný vstup! Zadej znovu!")
            yvstup = float(input("Vložte zeměpisnou šířku: "))
        xvstup = float(input("Vložte zeměpisnou délku: "))
        if xvstup > 180 or xvstup < -180:
            print("Chybný vstup! Zadej znovu!")
            xvstup = float(input("Vložte zeměpisnou délku: "))
        souradnice = (yvstup,xvstup)
        ybod = vypocet_souradnice_y(yvstup,z,m,r)
        xbod = vypocet_souradnice_x(xvstup,m,r)
        print("Souřadnice hledaného bodu jsou: (", xbod, ",", ybod, ")")
    except ValueError:
        print("Chybný vstup! Zadej znovu!")
        continue
    if souradnice == (0.0, 0.0):
        break

if '----------' in rzelva or '----------' in pzelva:
    print("Vzdálenosti jsou příliš velké, želvička by to neušla!")
else:
    from turtle import speed, penup, pendown, setpos, seth, forward, exitonclick
    speed(10)
    for k in range(37):
        penup()
        setpos(pzelva[k], rzelva[0])
        seth(90)
        pendown()
        forward(abs(max(rzelva)-min(rzelva)))
    for l in range(19):
        penup()
        setpos(pzelva[0], rzelva[l])
        seth(0)
        pendown()
        forward(abs(max(pzelva) - min(pzelva)))
    exitonclick()



