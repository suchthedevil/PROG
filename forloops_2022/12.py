"""
Asi poznáš pesničku 'Sedí mucha na stene, sedí a spí.'. 
Napíš program, ktorý si najprv vypýta zoznam nejakých 
samohlások a potom pre každú z nich vypíše túto vetu tak, 
že v nej všetky samohlásky nahradí touto konkrétnou. 
Zrejme využiješ for-cyklus a formátovací reťazec 
f'S{i}d{i} m{i}ch{i} ...'.
"""

samohlasky = "aeiouyôúéíóä"

for i in samohlasky:
    print(f"S{i}d{i} m{i}ch{i} n{i} st{i}n{i}")

