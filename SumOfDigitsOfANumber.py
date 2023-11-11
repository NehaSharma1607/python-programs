# program to print the sum of digits of a no.


def getsum(n):
    sum = 0
    if n == 0:
        return "invalid input"
    if len(str(n)) == 1:
        return "it is the sum of itself"

    while (n != 0):
        sum += int(n % 10)
        n = int(n / 10)
    return sum


n = int(input("enter the digits to be added:"))
print(getsum(n))
