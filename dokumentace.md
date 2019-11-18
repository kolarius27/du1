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

Dále je potřeba zadat měřítko. Pokud chcete například měřítko 1:100000000, stačí zadat do programu 100000000.


Zadejte měřítko: 50000000

Nyní zadejte poloměr referenční koule, se kterým chcete počítat.
Pokud chcete počítat s poloměrem 6371,11 km, stačí zadat hodnotu 0.


Zadejte poloměr Země (v km): 0

Zde jsou vypsané souřadnice rovnoběžek a poledníků po 10°. 
V kulatých závorkách naleznete zeměpisnou šířku/délku a vypočtenou souřadnici zobrazení.

Rovnoběžky:  [-12.7, -12.5, -12.0, -11.0, -9.8, -8.2, -6.4, -4.4, -2.2, 0.0, 2.2, 4.4, 6.4, 8.2, 9.8, 11.0, 12.0, 12.5, 12.7]
Poledníky:  [-40.0, -37.8, -35.6, -33.4, -31.1, -28.9, -26.7, -24.5, -22.2, -20.0, -17.8, -15.6, -13.3, -11.1, -8.9, -6.7, -4.4, -2.2, 0.0, 2.2, 4.4, 6.7, 8.9, 11.1, 13.3, 15.6, 17.8, 20.0, 22.2, 24.5, 26.7, 28.9, 31.1, 33.4, 35.6, 37.8, 40.0]


Pokud vám toto nestačí, nyní máte možnost vypočítat konkrétní body.
Při zadání bodu (0,0) program přejde na vykreslení souřadnicové sítě želví grafikou.

Vložte zeměpisnou šířku: 0
Vložte zeměpisnou délku: 0
Souřadnice hledaného bodu jsou: ( 0.0 , 0.0 )

Děkuji za použití programu zobrazeni.py, brzy naviděnou!

Process finished with exit code 0
```

