# program to check whether a string starts with specifed character
def specific_char(str):

    for char in str[:1]:
        if char =="a" or "A":
            print("continue")
        else:
            print("error")

specific_char("amazing")


# program to change first char to $ when repeated
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, "$")
    str1 = char + str1[1:]
    return str1


print(change_char("restart"))