# zobrazení.py

## Co program dělá?

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
dotazování ukončeno.

Dále se vkládá měřítko. Když je vstupní hodnota v intervalu (-inf;0>, nebo je dokonce
vstup nečíselný, je uživatel dotazován znovu. Při korektním vstupu je 
dotazování ukončeno a program pokračuje dále.

Posledním vstupem je poloměr Země. Při zadání záporné hodnoty či nečíselného vstupu
je potřeba zadat vstup znovu. Při zadání hodnoty "0" se proměnné automaticky přidělí
hodnota "6371.11" a program pokračuje dále. Při zadání jiného korektního vstupu
program pokračuje taktéž.

Následně jsou vypsány dva seznamy: "rovnobezky" a "poledniky". Ty čítají vypočtené 
souřadnice x/y. Pokud některá souřadnice přesáhne hodnotu 100 (= 1 m), místo ní se 
zobrazí "-".

Uživatel má možnost také nechat vypsat souřadnice konkrétních bodů dle jeho libosti.
Pokud je zadaná hodnota nečíselná nebo mimo definiční obor (<-90;90> u zeměpisné šířky,
<-180;180> u zeměpisné délky), uživatel je opět dotazován. Při korektních vstupech
jsou zobrazeny souřadnice hledaného bodu a program se uživatele ptá, jaký bod chce
vypočítat tentokrát. Při zadání hodnot (0, 0) je dotazování ukončeno.

Nakonec se uživateli vykreslí želví grafikou souřadnicová síť, kdy 1 mm = 1 px.
Pokud uživatel vypočítal nějaké konkrétní body, budou na výsledné souřadnicové síti 
vyznačeny modrou tečkou.

**********

## Úspěšný průběh programu

```
Vítejte v programu zobrazeni.py!

Program umožňuje vypočítat souřadnice válcových tečných zobrazení.
Pro výpočet Lambertova zobrazení zadejte písmeno L.
Pro výpočet Marinova zobrazení zadejte písmeno A.
Pro výpočet Mercatorova zobrazení zadejte písmeno M.
Pro výpočet Braunova zobrazení zadejte písmeno B.


Zadejte zobrazení: L

Dále je potřeba zadat měřítko. Pokud chcete například měřítko 1:1000000000, stačí zadat do programu 1000000000.


Zadejte měřítko: 1000000000

Nyní zadejte poloměr referenční koule, se kterým chcete počítat.
Pokud chcete počítat s poloměrem 6371,11 km, stačí zadat hodnotu 0.


Zadejte poloměr Země (v km): 0

Zde jsou vypsané souřadnice rovnoběžek a poledníků po 10°. 
V kulatých závorkách naleznete zeměpisnou šířku/délku a vypočtenou souřadnici zobrazení.

Rovnoběžky:  [-6.4, -6.3, -6.0, -5.5, -4.9, -4.1, -3.2, -2.2, -1.1, 0.0, 1.1, 2.2, 3.2, 4.1, 4.9, 5.5, 6.0, 6.3, 6.4]
Poledníky:  [-20.0, -18.9, -17.8, -16.7, -15.6, -14.5, -13.3, -12.2, -11.1, -10.0, -8.9, -7.8, -6.7, -5.6, -4.4, -3.3, -2.2, -1.1, 0.0, 1.1, 2.2, 3.3, 4.4, 5.6, 6.7, 7.8, 8.9, 10.0, 11.1, 12.2, 13.3, 14.5, 15.6, 16.7, 17.8, 18.9, 20.0]


Pokud vám toto nestačí, nyní máte možnost vypočítat konkrétní body.
Při zadání bodu (0,0) program přejde na vykreslení souřadnicové sítě želví grafikou.

Vložte zeměpisnou šířku: 90
Vložte zeměpisnou délku: 180
Souřadnice hledaného bodu jsou: ( 20.0 , 6.4 )
Vložte zeměpisnou šířku: 90
Vložte zeměpisnou délku: -180
Souřadnice hledaného bodu jsou: ( -20.0 , 6.4 )
Vložte zeměpisnou šířku: -90
Vložte zeměpisnou délku: 180
Souřadnice hledaného bodu jsou: ( 20.0 , -6.4 )
Vložte zeměpisnou šířku: -90
Vložte zeměpisnou délku: -180
Souřadnice hledaného bodu jsou: ( -20.0 , -6.4 )
Vložte zeměpisnou šířku: 0
Vložte zeměpisnou délku: 0
Souřadnice hledaného bodu jsou: ( 0.0 , 0.0 )

Děkuji za použití programu zobrazeni.py, brzy naviděnou!

Process finished with exit code 0
```

