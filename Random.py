import math
#help(math)
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*", end=" ")
    print()