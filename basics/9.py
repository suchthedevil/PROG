n = int(input("Zadajte n: "))

for i in range(n):
    if i%2 == 0:
        print("cervena")
    else:
        print("modra")

#better
f1 = "modra"
f2 = "cervena"
for i in range(n):
    print(f1)
    f1, f2 = f2, f1     
     
        
