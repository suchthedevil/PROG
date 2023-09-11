"""
Napíš program, ktorý n-krát vypíše zadané slovo takto: 
v 1. riadku bez odsadenia, v 2. s 1 odsadením (4 medzery), 
v 3. s 2 odsadeniami (8 medzier), v 4. s 3 odsadeniami 
(12 medzier), pre ďalšie riadky sa to opakuje od začiatku. 
V programe využi zvyšok po delení, napríklad i%4*4.
"""
w = "Python"
n = 9

for k in range(n//4):
    for i in range(4):
        print(" "*4*i + w)
for i in range(n%4):
    print(" "*4*i + w)