print("Vítejte v programu pro výpočet válcových tečných zobrazení!")
z = float(input("Zadajte zobrazení: "))
m = int(input("Zadejte měřítko: "))
r = input("Zadejte poloměr Země (v km): ")
Rovnobezky = []
for i in range(19):
    v = int(-90 + i*10)
    x = r*v

