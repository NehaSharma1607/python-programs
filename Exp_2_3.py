
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = dict(d1)
d3.update(d2)
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
print(d3)
'''
def highest_3_values(d):
    values = sorted(d.values(), reverse=True)[:3]
    return values
d = {}
n = int(input("Enter the number of key-value pairs in the dictionary: "))
for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    d[key] = value
    values = highest_3_values(d)
print("The top 3 values in this dictionary are:", values)
print()
'''