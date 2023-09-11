first = "biela"
second = "modra"
third = "cervena"

print(first, second, third)
print(first, third, second)
first, second, third = second, first, third
print(first, second, third)
print(first, third, second)
first, second, third = third, second, first
print(first, second, third)
print(first, third, second)

