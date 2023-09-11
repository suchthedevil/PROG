"""
a = int(input("Zadaj od: "))
b = int(input("Zadaj do: "))

for i in range(a,b+1):
    print(i, i**2, i**3)
"""
"""

a = input("Zadaj cislo: ")

cifry = 0
cif_sucet = 0

for i in a:
    cifry += 1
    cif_sucet += int(i)
print(cifry)
print(cif_sucet)

"""
"""
a = input("Zadaj cislo: ")

rest = 0
num = 0
intermediate = 0

for i in range(1,len(a)):
    rest = int(a)%10
    num = int(a)//10
    a = num
    print(num, rest)
"""

pocet = int(input("Zadajte pocet clenov postupnosti: "))

pi = 4

for i in range(1, pocet*4, 4):
    pi = pi + (-4/(i+2) + 4/(i+4))
    print(i)
print(pi)


"""
#jablko to 1j2a3b4l.....

word = input("Slovo: ")
new_word = ""

for i in range(1,len(word)+1):
    number = i
    letter = word[i-1]
    print(str(number)+letter, end="")
"""

