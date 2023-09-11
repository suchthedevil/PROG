n = 321547
sum = 0
while n>0:
    sum += n%10
    print(n%10)
    n //= 10
print(f"Digit sum is: {sum}")
