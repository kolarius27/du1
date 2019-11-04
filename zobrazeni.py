print("Vítejte v programu pro výpočet válcových tečných zobrazení!")
#z = float(input("Zadajte zobrazení: "))
m = int(input("Zadejte měřítko: "))
r = float(input("Zadejte poloměr Země (v km): "))
Rovnobezky = []
Poledniky = []

import math
for i in range(19):
    v = int(-90 + i*10)
    vrad = math.radians(v)
    y = float(r*vrad*1000000/m)
    yround = round(y,1)
    tr = (v,yround)
    Rovnobezky.append(tr)
for k in range(37):
    u = int(-180 + k*10)
    urad = math.radians(u)
    x = float(r*urad*1000000/m)
    xround = round(x,1)
    tp = (u,xround)
    Poledniky.append(tp)
print("Rovnobezky: ", Rovnobezky)
print("Poledniky: ", Poledniky)
