# linear searching
def search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1
print(search([1,5,6,3,5,89,2], 2))


# binary searching
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1



arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")


# bubble sorting
def bubblesort():
    l = [42, 34, 45, 67, 97, 87, 95, 12, 21]
    n = len(l)
    print("original list:", l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print("list after sorting is:", l)

bubblesort()

# selection sort
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i], end=" , ")

# insertion sort
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
