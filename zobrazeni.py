print("Vítejte v programu pro výpočet válcových tečných zobrazení!")
z = input("Zadejte zobrazení: ")
correct_z = ("L", "A", "B", "M")
while z not in correct_z:
    print("Chyba! Zadej znovu!")
    z = input("Zadejte zobrazení: ")
while True:
    try:
        m = int(input("Zadejte měřítko: "))
    except ValueError:
        print("Chyba! Zadej znovu!")
        continue
    else:
        break
while True:
    try:
        r = float(input("Zadejte poloměr Země (v km): "))
    except ValueError:
        print("Chyba! Zadej znovu!")
        continue
    else:
        break
import math
Poledniky = []
for i in range(37):
    u = int(-180 + i * 10)
    urad = math.radians(u)
    x = float(r * urad * 1000000 / m)
    xround = round(x, 1)
    if x > 100:
        xround = "-"
    tp = (u, xround)
    Poledniky.append(tp)
Rovnobezky = []
for j in range(19):
    v = int(-90 + j*10)
    vrad = math.radians(v)
    if z == "L" or z == "l":
        y = float(r * math.sin(vrad) * 1000000 / m)
    if z == "A" or z == "a":
        y = float(r * vrad * 1000000 / m)
    if z == "B" or z == "b":
        y = float(2 * r * math.tan(vrad / 2))
    if z == "M" or z == "m":
        y = float(r * math.log2( 1 / math.tg(vrad/2) ))
    yround = round(y,1)
    if y > 100:
        yround = "-"
    tr = (v,yround)
    Rovnobezky.append(tr)
print("Rovnobezky: ", Rovnobezky)
print("Poledniky: ", Poledniky)

