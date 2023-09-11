meno = "Tomas Lamlech"
adresa = "Kotesova 200"
mobil = "0948 719 691"
horne_oram = "+" + 23*"-" + "+"

print(horne_oram)
for i in meno, adresa, mobil:
    print("|" + " " + i + (22-len(i))*" " + "|")
print(horne_oram)

