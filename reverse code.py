n = 4  # number of rows

for i in range(n):
    print(" " * (2 * (n - i - 1)), end="")
    
    for j in range(i, -1, -1):
        print(chr(64+i), end=" ")
    
    print()
