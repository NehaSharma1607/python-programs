# leap year
'''
Aim:program to demonstrate the use of if,if-else,while,for,break, continue
1)python code to find largest of 3 numbers
2)palindrome
3)armstrong

2)add digits of a number using while loop
3)wap for sum of 15 natural numbers
4)wap to print all characters of string
5)
1
22
333
4444
55555
'''

'''
year=int(input("enter year:"))
if((year%4==0)and(year%100!=0)):
    print("year",year,"is leap year")
elif((year%400==0) and (year%100==0)):
    print("year",year,"is leap year")
else:
    print("year",year,"is not a leap year")
   
x=0
while(x<5):
    print("in while loop")
    x+=1
print("end of while loop")

#235====2+3+5=10
number=int(input("Enter a number: "))
sum=0
while(number!=0):
    mod=number%10
    sum=sum+mod
    number=int(number/10)
print(sum)

sum=0
for i in range(0,16):
    sum=sum+i
print(sum)

str=input("Enter a string:")
for i in str:
    print(i)

rows=5
for i in range(1,rows+1):
    for j in range(1,i + 1):
        print(i,end="")
    print()

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()

for i in range(21):
    if(i%2==0):
        continue
    print(i)
'''
# largest of 3 numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if (a > b):
    if (a > c):
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if (b > c):
        print("b is greatest")
    else:
        print("c is greatest")

# palindrome
n = int(input("enter a number:"))
temp = n
reverse = 0
while (n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if (temp ==  reverse):
    print("the number is palindrome")
else:
    print("not palindrome")

# armstrong
n = input("enter a number:")
sum = 0
for i in n:
    condition = int(i) ** 3
    sum = sum + condition
if (sum == int(n)):
    print(" it is a armstrong number")
else:
    print("not a armstrong number")
