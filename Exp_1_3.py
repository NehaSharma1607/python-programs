'''
#AIm: WAP to demonstarte various concepts with different arguements
#1)wap tpcalculate area of 10 different circles.
#2) tables from 2-20
def add(a,b):
    print(a+b)
#add(5,6) #required
#add(a=52,b=56) #keyword
def new_add(*nums):
    sum=0
    for i in nums:
        sum=sum+i
    print(sum)
#new_add(56,23,45) #variable length


def factorial(n=10): #default
    fact=1
    while(n!=0):
        fact=fact*n
        n-=1
    print(fact)

#factorial()
hghiuekh
def table(n):
    hghiuekh

    for i in range(1,11):
        print(n,"*",i,"=",n*i)
    print()
#table(2)
#table(3)
#table(4)
#print(help(table))
#print(table.__doc__)

# the triple quotes thingy can be printed. like one way is to use the help() function while the other way is to function_name.doc
#this shit is ccol
'''
pi = 22 / 7


def circles1():
    radius = int(input("Enter the radius: "))
    area = pi * (radius ** 2)
    print(round(area, 2), " is the area of circle with radius", radius)


def circles2(radius):
    area = pi * (radius ** 2)
    print(round(area, 2), " is the area of circle with radius", radius)


def circles3():
    radius = int(input("Enter the radius: "))
    area = pi * (radius ** 2)
    return round(area, 2), " is the area of circle with radius", radius


def circles4(radius):
    area = pi * (radius ** 2)
    return round(area, 2), " is the area of circle with radius", radius


print(
    "choose one ampong the following ways:"
    "\n1)Simple function"
    "\n2)parameterized function"
    "\n3)function wih return"
    "\n4)parametereised with return type"
)
choice = int(input("Enter your choice: "))
if choice == 1:
    for i in range(1, 11):
        circles1()
        i += 1
elif choice == 2:
    for i in range(1, 11):
        circles2(i)
        i += 1
elif choice == 3:
    for i in range(1, 11):
        print(circles3())
        i += 1
elif choice == 4:
    for i in range(1, 11):
        print(circles4(i))
        i += 1
else:
    print("invalid input")

'''
def multiply1():
    num = int(input("Enter the number to multiply with: "))
    for j in range(1, 11):
        multiplication = num * j
        print(num, "x", j, "=", multiplication)
        j += 1


def multiply2(num):
    for j in range(1, 11):
        multiplication = num * j
        print(num, "x", j, "=", multiplication)
        j += 1


def multiply3():
    num = int(input("Enter the number to multiply with: "))
    list=[]
    for j in range(1, 11):
        list.append((num, "x", j, "=", num * j))
        j = j + 1
    return list


def multiply4(num):
    list = []
    for j in range(1, 11):
        list.append((num, "x", j, "=", num * j))
        j=j+1
    return list

print(
    "choose one among the following ways:"
    "\n1)Simple function"
    "\n2)parameterized function"
    "\n3)function wih return"
    "\n4)parameterized with return type"
)
choice = int(input("Enter your choice: "))
if choice == 1:
    for i in range(2, 21):
        multiply1()
        i += 1
elif choice == 2:
    for i in range(2, 21):
        multiply2(i)
        i += 1
elif choice == 3:
    for i in range(2, 21):
        print(multiply3())
        i += 1
elif choice == 4:
    for i in range(2, 21):
        print(multiply4(i))
        i += 1
else:
    print("invalid input")

'''