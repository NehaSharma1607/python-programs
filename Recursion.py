# recursion program to find the factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(5))

#binary search using recursion
def binary_search(list,low,high,val):
    if (high<low):
        return None
    else:
        midval=low+((high-low)//2)
        if list[midval]>val:
            return binary_search(list,low,midval-1,val)
        elif list[midval]<val:
            return binary_search(list,midval+1,high,val)
        else:
            return midval
list=[5,11,21,32,65,85,45]
#print(binary_search(list,0,5,32))
#print(binary_search(list,0,5,65))
