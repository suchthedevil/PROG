n = 5847
n_str = str(n)

for i in n_str:
    print(n%10)
    n = n//10
#alternativa 1:
while n != 0:
    print(n%10)
    n = n//10
#alternativa 2
while n:
    print(n%10)
    n = n//10