a=[5,6,7,8,9,4,3]
size=8
if len(a)==0:
    print("stack empty")
elif len(a)==size:
    print("stack full")
else:
    print("continue")
a.append(5)
print(a)
a.pop()
print(a)
