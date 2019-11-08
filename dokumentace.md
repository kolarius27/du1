# Domácí úkol 1 - zobrazení

## Zadání

Tento program pro zvolené zobrazení, měřítko a poloměr vypíše souřadnice rovnoběžek
a poledníků. Uvažují se pouze válcová tečná zobrazení, a to Marinovo, Lambertovo, 
Braunovo a Mercatorovo. Poté má uživatel možnost zjistit souřadnice konkrétních
bodů. Výstupem je výpis souřadnic poledníků/rovnoběžek na ose x/y, souřadnice
konkrétních bodů a vykreslení souřadnicové sítě želví grafikou.

************

## Jak program pracuje?

Program se uživatele nejdříve ptá na typ zobrazení. Při zadání jiného znaku (či
řetězci znaků) než "L" (Lambertovo zobrazení), "A" (Marinovo z.), "M" (Mercatorovo
z.) nebo "B" (Braunovo z.) je uživatel opět dotazován. Při korektním vstupu je 
ukončen "while cyklus" a program pokračuje dále.

Dále se vkládá měřítko. Když je vstupní hodnota v intervalu (-inf;0>, nebo je dokonce
vstup nečíselný, je uživatel dotazován znovu. Při korektním vstupu je 
ukončen "while cyklus" a program pokračuje dále.

Posledním vstupem je poloměr Země. Při zadání záporné hodnoty či nečíselného vstupu
je potřeba zadat vstup znovu. Při zadání hodnoty "0" se proměnné automaticky přidělí
hodnota "6371.11" a program pokračuje dále. Při zadání jiného korektního vstupu
program pokračuje taktéž.

Následně jsou vypsány dva seznamy: "Rovnobezky" a "Poledniky". Ty jsou tvořeny
uspořádanými dvojcemi zeměpisné šířky/délky a vypočtené souřadnice x/y. Pokud některá
souřadnice přesáhne hodnotu 100 (= 1 m), místo ní se zobrazí "-".

Uživatel má možnost také nechat vypsat souřadnice konkrétních bodů dle jeho libosti.
Pokud je zadaná hodnota nečíselná nebo mimo definiční obor (<-90;90> u zeměpisné šířky,
<-180;180> u zeměpisné délky), uživatel je opět dotazován. Při korektních vstupech
jsou zobrazeny souřadnice hledaného bodu a program se uživatele ptá, jaký bod chce
vypočítat tentokrát. Při zadání hodnot (0, 0) program vyskočí z "while cyklu".

Nakonec se uživateli vykreslí želví grafikou souřadnicová síť, kdy 1 mm = 1 px.
Pokud některá souřadnice má vyšší hodnotu než 1 m (tudíž se hodnota přepíše na "-"),
objeví se chybová hláška. Pokud uživatel vypočítal nějaké konkrétní body, budou
na výsledné souřadnicové síti vyznačeny modrou tečkou.

**********

## Úspěšný průběh programu

```
Vítejte v programu LAMB.exe!

Program umožňuje vypočítat souřadnice válcových tečných zobrazení.
Pro výpočet Lambertova zobrazení zadejte písmeno L.
Pro výpočet Marinova zobrazení zadejte písmeno A.
Pro výpočet Mercatorova zobrazení zadejte písmeno M.
Pro výpočet Braunova zobrazení zadejte písmeno B.


Zadejte zobrazení: M

Dále je potřeba zadat měřítko. Pokud chcete například měřítko 1:1000000000, stačí zadat do programu 1000000000.


Zadejte měřítko: 850000000

Nyní zadejte poloměr referenční koule, se kterým chcete počítat.
Pokud chcete počítat s poloměrem 6371,11 km, stačí zadat hodnotu 0.


Zadejte poloměr Země (v km): 0

Zde jsou vypsané souřadnice rovnoběžek a poledníků po 10°. 
V kulatých závorkách naleznete zeměpisnou šířku/délku a vypočtenou souřadnici zobrazení.

Rovnoběžky:  [(-90, -23.5), (-80, -18.3), (-70, -13.0), (-60, -9.9), (-50, -7.6), (-40, -5.7), (-30, -4.1), (-20, -2.7), (-10, -1.3), (0, 0.0), (10, 1.3), (20, 2.7), (30, 4.1), (40, 5.7), (50, 7.6), (60, 9.9), (70, 13.0), (80, 18.3), (90, 23.5)]
Poledníky:  [(-180, -23.5), (-170, -22.2), (-160, -20.9), (-150, -19.6), (-140, -18.3), (-130, -17.0), (-120, -15.7), (-110, -14.4), (-100, -13.1), (-90, -11.8), (-80, -10.5), (-70, -9.2), (-60, -7.8), (-50, -6.5), (-40, -5.2), (-30, -3.9), (-20, -2.6), (-10, -1.3), (0, 0.0), (10, 1.3), (20, 2.6), (30, 3.9), (40, 5.2), (50, 6.5), (60, 7.8), (70, 9.2), (80, 10.5), (90, 11.8), (100, 13.1), (110, 14.4), (120, 15.7), (130, 17.0), (140, 18.3), (150, 19.6), (160, 20.9), (170, 22.2), (180, 23.5)]


Pokud vám toto nestačí, nyní máte možnost vypočítat konkrétní body.
Při zadání bodu (0,0) program přejde na vykreslení souřadnicové sítě želví grafikou.

Vložte zeměpisnou šířku: 90
Vložte zeměpisnou délku: 180
Souřadnice hledaného bodu jsou: ( 23.5 , 23.5 )
Vložte zeměpisnou šířku: -90
Vložte zeměpisnou délku: -180
Souřadnice hledaného bodu jsou: ( -23.5 , -23.5 )
Vložte zeměpisnou šířku: -90
Vložte zeměpisnou délku: 180
Souřadnice hledaného bodu jsou: ( 23.5 , -23.5 )
Vložte zeměpisnou šířku: 90
Vložte zeměpisnou délku: -180
Souřadnice hledaného bodu jsou: ( -23.5 , 23.5 )
Vložte zeměpisnou šířku: 0
Vložte zeměpisnou délku: 0
Souřadnice hledaného bodu jsou: ( 0.0 , 0.0 )

Děkuji za použití programu LAMB.exe, brzy naviděnou!

Process finished with exit code 0
```

