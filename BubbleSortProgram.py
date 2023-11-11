# BUBBLE SORT
def main():
    l = [42, 34, 45, 67, 97, 87, 95, 12, 21]
    n = len(l)
    print("original list:", l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print("list after sorting is:", l)


main()