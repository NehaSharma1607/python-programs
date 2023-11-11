'''
print("yeyyyyyy")
print('eyeyeyeye')
mystr="hello world"
print(mystr[0])
print(mystr[-1])
for i in mystr:
    print(i,end="")
print()
for i in range(0,len(mystr),2):
    print(mystr[i],end='')

s="tadadaaaaaaaaa makaleke liau"
print(s.capitalize())
print(s.upper())
print(s.title())
s1="                 stringgggggggggggggggggg"
print(s1.lstrip())
'''
# 1.WAP to check if a strng is palindrome or not
# 2. WAP to find uncommon words from two strings
# 3.WAP to add 'ing' at the end of the given string(length should be atleast three). If the given ends with ing,
#       and add ly. IF length is less tha 3 leave it unchanged.

# first
s = input("Enter a string: ")
if (s == s[::-1]):
    print("Is a palindrome")
else:
    print("Not a palindrome")

# second
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
words1 = s1.split()
words2 = s2.split()
uncommon_word = []
for word in words1:
    if word not in words2:
        uncommon_word.append(word)
for word in words2:
    if word not in words1:
        uncommon_word.append(word)
print("Uncommon words: ", uncommon_word)

# third
s = (input("Enter string: "))
if len(s) >= 3:
    if s.endswith("ing"):
        print(s + "ly")
    else:
        print(s + "ing")
else:
    print(s)
