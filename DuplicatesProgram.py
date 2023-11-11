#program to remove duplicates from a list
a=[10,20,30,10,50,40,90,79,50,90]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)