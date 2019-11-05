def mercator(v)
    v = int(-90 + j * 10)
    if v < 0:
        



    if v == -90:
        v = -85.05133
        vrad = radians(v)
        print(vrad)
    if v == 90:
        v = 85.05133
        vrad = radians(v)
        print(vrad)
    y = float(r * log(cos(vrad / 2) / sin(vrad / 2)) * 1000000 / m)

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
from math import pi, log, cos, sin, radians, tan
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
    pzelva.append(xround)
Rovnobezky = []
rzelva = []
yround = ()
for j in range(18):
    v = int(-90 + j*10)
    vrad = radians(v)
    y = ()
    if z == "L" or z == "l":
        y = float(r * sin(vrad) * 1000000 / m)
    if z == "A" or z == "a":
        y = float(r * vrad * 1000000 / m)
    if z == "B" or z == "b":
        y = float(2 * r * tan(vrad / 2))
    if z == "M" or z == "m":
        v = int(-90 + j * 10)
        if v == -90:
            v = -85.05133
            vrad = radians(v)
            print(vrad)
        if v == 90:
            v = 85.05133
            vrad = radians(v)
            print(vrad)
        y = float(r * log(cos(vrad/2)/sin(vrad/2) ) * 1000000 /m)
    yround = round(y,1)
    if abs(y) > 100:
        yround = "-"
    tr = (v,yround)
    Rovnobezky.append(tr)
    rzelva.append(yround)
print("Rovnobezky: ", Rovnobezky)
print("Poledniky: ", Poledniky)
print(pzelva)
print(rzelva)
import turtle
turtle.speed(10)
for k in range(18):
    yd = abs(rzelva[k] - rzelva[k+1])*10
    for l in range(36):
        xd = abs(pzelva[l] - pzelva[l+1])*10
        for m in range(2):
            turtle.forward(xd)
            turtle.right(90)
            turtle.forward(yd)
            turtle.right(90)
        turtle.forward(xd)
    turtle.right(90)
    turtle.forward(yd)
    turtle.right(90)
    turtle.forward(abs(max(pzelva)-min(pzelva))*10)
    turtle.right(180)
turtle.exitonclick()



