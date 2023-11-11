# INSERTION SORT
a = [12, 34, 56, 78, 90, 67, 45, 56, 78, 98, 23]
print("orignal list:", a)
for i in a:
    j = a.index(i)
    while j > 0:
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
        else:
            break
        j = j - 1
print("lis after sorting:", a)