def mul_tup(t):
    product=1
    for num in t:
        product *=num
    return product
t1=(1,2,3,4)
print("product is:",mul_tup(t1))

#1
def remove(t):
    t=[tup for tup in t if tup]
    return t
t2=[(),(2,3),(),(56,23)]
print(remove(t2))

#3
t3=('2','3','4')
x=[int (i) for a,i in enumerate(t3)]
print(tuple(x))

#4
t4=("2","3","4","5")
print("org tup:",t4)
ele="2"
x=[ele for i in t4 if ele in i]
print(["yes" if x else "no"])