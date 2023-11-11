'''
The integer cube root of a positive number 𝑛 is the smallest number 𝑖 such that 𝑖^3≤𝑛 but (𝑖+1)^3>𝑛

For instance, the integer cube root of 100
is 4 since 4^3≤100 but 5^3>100. Likewise, the integer cube root of 1000 is 10

Write a function integerCubeRootHelper(n, left, right) that searches for the integer cube-root of n between left and right given the following pre-conditions:

𝑛≥1
left<right
left^3<𝑛
right^3>𝑛


def integerCubeRootHelper(n, left, right):
    cube = lambda x: x * x * x  # anonymous function to cube a number
    assert (n >= 1)
    assert (left < right)
    assert (left >= 0)
    assert (right < n)
    assert (cube(left) <= n), f'{left}, {right}'
    assert (cube(right) > n), f'{left}, {right}'
    # your code here
    for i in range(left, right+1):
        if cube(i)<=n and cube(i+1)>n:
            return 1
        i=i+1
        else:
            print("shit")




def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)



assert(integerCubeRoot(1) == 1)
assert(integerCubeRoot(2) == 1)
assert(integerCubeRoot(4) == 1)
assert(integerCubeRoot(7) == 1)
assert(integerCubeRoot(8) == 2)
assert(integerCubeRoot(20) == 2)
assert(integerCubeRoot(26) == 2)
for j in range(27, 64):
    assert(integerCubeRoot(j) == 3)
for j in range(64,125):
    assert(integerCubeRoot(j) == 4)
for j in range(125, 216):
    assert(integerCubeRoot(j) == 5)
for j in range(216, 343):
    assert(integerCubeRoot(j) == 6)
for j in range(343, 512):
    assert(integerCubeRoot(j) == 7)
print('Congrats: All tests passed! (10 points)')


cube = lambda x: x * x * x  # anonymous function to cube a number
print(cube(3))
'''

n=125

print(int(n ** (1 / 3)))


'''
if x[(left+right)//2]>y[(left+right)//2]:
        flag=0
        if x[(left+right)//2+1]>y[(left+right)//2+1]:
            findCrossoverIndexHelper(x,y,(left+right)//2+1,right)
        else:
            flag=1
        if flag==1:
            print(((left+right)//2))
            return (left+right)//2
    elif x[(left+right)//2]<=y[(left+right)//2]:
        flag=0
        if x[(left+right)//2-1]<=y[(left+right)//2-1]:
            findCrossoverIndexHelper(x,y,left,(left+right)//2-1)
        else:
            flag=1
        if flag==1:
            print(((left+right)//2)-1)
            return ((left+right)//2)-1
            '''

'''
# First write a "helper" function with two extra parameters
# left, right that ddedscribes the search region as shown below
def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert (len(x) == len(y))
    assert (left >= 0)
    assert (left <= right - 1)
    assert (right < len(x))
    # Here is the key property we would like to maintain.
    assert (x[left] > y[left])
    assert (x[right] < y[right])

    # your code here
    mid = (left + right) // 2
    if x[mid] > y[mid]:
        flag = 0
        if x[mid + 1] > y[mid + 1]:
            findCrossoverIndexHelper(x, y, mid + 1, right)
        else:
            flag = 1
        if flag == 1:
            print(mid)
            # return mid
    elif x[mid] <= y[mid]:
        flag = 0
        if x[mid - 1] <= y[mid - 1]:
            findCrossoverIndexHelper(x, y, left, mid - 1)
        else:
            flag = 1
        if flag == 1:
            print()
    # return (mid)-1


def findCrossoverIndex(x, y):
    assert (len(x) == len(y))
    assert (x[0] > y[0])
    n = len(x)
    assert (x[n - 1] < y[n - 1])  # Note: this automatically ensures n >= 2 why?
    # your code here
    print(findCrossoverIndexHelper(x, y, 0, n - 1))


findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9])
'''