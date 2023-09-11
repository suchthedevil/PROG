"""
Budeš vytvárať dlhý znakový reťazec podobne ako v 
predchádzajúcej úlohe. Namiesto úsekov hviezdičiek 
budeš do reťazca zapisovať čísla z nejakého intervalu 
(v tvare '<číslo>'). Schéma programu by mala byť podobná 
predchádzajúcej úlohe.
"""
od = 88
do = 100

retazec = ""

for i in range(od,do+1):
    retazec += "<" + str(i) + ">" + " "
print(retazec)

