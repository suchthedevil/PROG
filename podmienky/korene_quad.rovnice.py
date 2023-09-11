from math import *
a, b, c = 1, 5, 2
d = b**2 - 4*a*c

if d>0:
    x1 = (-b+sqrt(d)/(2*a))
    x2 = (-b-sqrt(d)/(2*a))
    print(f"Riesenia rovnice su: {round(x1,2)} a {round(x2,2)}")
elif d<0:
    print("Rovnica nema riesenie")
elif d == 0:
    x1 = (-b/(2*a))
    print(f"Riesenie rovnice je: {round(x1,2)}")

