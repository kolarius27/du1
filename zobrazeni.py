print("Vítejte v programu pro výpočet válcových tečných zobrazení!")
z = input("Zadejte zobrazení: ")
correct_z = ("L", "A", "B", "M")
while z not in correct_z:
    print("Chyba! Zadej znovu!")
    z = input("Zadejte zobrazení: ")
m = int()
while True:
    try:
        m = int(input("Zadejte měřítko: "))
        while m <= 0:
            print("Chyba! Zadej znovu!")
            m = int(input("Zadejte měřítko: "))
    except ValueError:
        print("Chyba! Zadej znovu!")
        continue
    else:
        break
r = float()
while True:
    try:
        r = float(input("Zadejte poloměr Země (v km): "))
        while r < 0:
            print("Chyba! Zadej znovu!")
            r = float(input("Zadejte poloměr Země (v km): "))
        while r == 0:
            r = 6371.11
    except ValueError:
        print("Chyba! Zadej znovu!")
        continue
    else:
        break
from math import log, sin, radians, tan
Poledniky = []
pzelva = []
for i in range(37):
    u = int(-180 + i * 10)
    urad = radians(u)
    x = float(r * urad * 1000000 / m)
    xround = round(x, 1)
    if abs(x) > 100:
        xround = "-"
    tp = (u, xround)
    Poledniky.append(tp)
    pzelva.append(xround*10)
Rovnobezky = []
rzelva = []
for j in range(19):
    v = int(-90 + j*10)
    vrad = radians(v)
    y = float()
    if z == "L":
        y = float(r * sin(vrad) * 1000000 / m)
    if z == "A":
        y = float(r * vrad * 1000000 / m)
    if z == "B":
        y = float(2 * r * tan(vrad / 2) * 1000000 / m)
    if z == "M":
        d = 90-v
        if d == 0:
            d = 4.948871
        if d == 180:
            d = 174.948871
        drad = radians(d)
        y = float(r * log(1/tan(drad/2)) * 1000000 / m)
    yround = round(y,1)
    if abs(y) > 100:
        yround = "-"
    tr = (v,yround)
    Rovnobezky.append(tr)
    rzelva.append(yround*10)
print("Rovnobezky: ", Rovnobezky)
print("Poledniky: ", Poledniky)
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



