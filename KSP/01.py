n = input("")
cisla_lava = []
cisla_prava = []
lava = 0
prava = 0

for i in range(int(n)):
    c1, c2 = map(int, input().split())
    cisla_lava.append(int(c1))
    cisla_prava.append(int(c2)) 

cisla_prava.extend([0,0])
cisla_lava.extend([0,0])

for num in range(0,len(cisla_lava)-1,2):
    lava += cisla_lava[num] + cisla_prava[num+1]
    prava += cisla_prava[num] + cisla_lava[num+1]

if lava < prava:
    print("lava")
elif lava > prava:
    print("prava")
else:
    print("je to jedno")
