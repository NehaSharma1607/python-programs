'''
l1 = ["maria", 56]
l2 = list("Hello")
print(l2)
ele = l2[2]
print(ele)

len(l2)
print(l2[::2])
print(l2[-1::-2])
l1.append(l2)
print(l1)
print(l1 + l2)
print(l1 * 3)
for i in l2:
    print(i)

print(l1.count(56))

l1.extend(l2)
print(l1)
l1.remove(l2)
print(l1)
l1.insert(2, 55)
print(l1)
l1.reverse()
print(l1)
l1.sort
print(l1)
l1.remove()
print()
l1.pop()
print(l1)
del(l1)
print(l1)
l1.clear()
print(l1)
'''
'''
# (i) WAP count of unique value present in the list.

list=[1,5,6,1,2,2,3,4]
num=0
for i in list:
    if list.count(i)==1:
        num=num+1
print("Number of unique elements: ",num)
'''
# (ii) Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples
#l3=[(5,2,3,7),(7,9,6,2),(78,96,23)]
#for i in l3:

def last(n):
    return n[-1]

def sort(tp):
    return sorted(tp, key=last)

x = [(1, 4), (3, 5), (2, 3), (5,6)]
print("Sorted:")
print(sort(x))
print()

#Write a Python program to print a specified list after removing the 0th, 4th and
#5th elements, Sample List : ['Red', 'Green', 'White', 'Black', 'Pink',
#'Yellow'],Expected Output : ['Green', 'White', 'Black']
'''
list1=[]
list2 = []
list1 = [item for item in input("Enter the list items(with space in between) : ").split()]
for index, value in enumerate(list1):
    if index not in [0, 4, 5]:
        list2.append(value)

print(list1)
print(list2)
print()
'''


