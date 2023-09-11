"""
Napíš program, ktorý vytvorí takúto tabuľku: pre všetky 
uhly (v stupňoch) z nejakého daného intervalu a kroku 
vypíše druhé mocniny príslušných sínusov a kosínusov a 
aj ich súčet. Druhé mocniny vypíše na šírku 6 a 4 desatinné 
miesta, súčet bez udania šírky a počtu desatinných miest. 

"""
import math

od = 0
do = 90
krok = 10

for i in range(od,do+1,10):
    sin = (math.sin(i))**2
    cos = (math.cos(i))**2
    sucet = sin+cos
    print(f"{i} sin**2={round(sin,6)} cos**2={round(cos,6)} sucet={sucet}")

