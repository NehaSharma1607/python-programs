# program to count and display the vowls in the given text
def vowels(text):
    vowels = "aeiouAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])


vowels("welcome")