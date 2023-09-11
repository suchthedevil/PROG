suma = 124

for i in 100, 50, 20, 10, 5, 2, 1:
    if suma >= i:
        pocet = suma // i
        suma = suma % i
        print(f"{pocet} krat hodnota {i}")
    else:
        pass

