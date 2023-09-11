n = 21
n -= n%2
print(n*"*", end="\n")
print("*" + (n-2)*" " + "*")
print("*" + ((n-len("PYTHON"))//2-1)*" " + "PYTHON" + ((n-len("PYTHON"))//2-1)*" "  +"*")
print("*" + (n-2)*" " + "*")
print(n*"*", end="\n")

