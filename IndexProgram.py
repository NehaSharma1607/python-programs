# program to print the index of the character of the string
str1=input("enter the string:")
for index,char in enumerate(str1):
    print("current character:",char,"position at:",index)



# program to remove nth index char
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_char("python", 3))