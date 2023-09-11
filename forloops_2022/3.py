"""
Aj nasledovný program bude podobný predchádzajúcemu: 
Program prečíta nejaké slovo a trojuholník sa bude skladať 
z písmen tohto slova: v 1. riadku je prvé písmeno, v 2. sú 
prvé dve, v 3. sú prvé tri, … v poslednom riadku je 
kompletné slovo. 
"""

w = "Python"
k = ""
for i in w:
    k += i
    print(k)

