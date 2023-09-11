"""
Napíš program, ktorý bude podobný predchádzajúcej úlohe: 
program prečíta nejaké slovo a trojuholník bude skladať z 
písmen tohto slova: v 1. riadku je prvé písmeno, v 2. druhé 
písmeno ale dvakrát, v 3. tretia písmeno trikrát, …, v 
poslednom je posledné písmeno veľakrát podľa počtu znakov 
slova. Môžeš dostať takýto výstup:
"""

word = "PYTHON"
n = 1
for i in word:
    print(i*n)
    n+=1
