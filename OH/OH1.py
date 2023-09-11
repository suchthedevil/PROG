t = 5 #s
c = 3*10**8 #m/s

s1 = (4.54*(10**-4)*c)/2
s2 = (4.48*(10**-4)*c)/2
delta_s = s1-s2

v = delta_s/t #m/s
v_kmh = v*3.6 #km/h

print("The plane is approaching with velocity:", v, "m/s\n", v_kmh, "km/h")

#DRUHY SPOSOB:

print("\nDruhy sposob: ")
t = 5 #s
c = 3*10**8 #m/s
delta_t = 4.54*(10**-4)-4.48*(10**-4)

s = (delta_t*c)/2 #m
v = s/t #m/s
v_kmh = v*3.6 #km/h

print("The plane is approaching with velocity:", v, "m/s\n", v_kmh, "km/h")


