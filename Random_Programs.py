s="hello world"
str=""
for i in range(len(s)):
    if i%2==0:
        str=str+s[i].upper()
    else:
        str=str+s[i].lower()
print(str)
