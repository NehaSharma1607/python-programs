import string, os
os.chdir('letters')
for letter in string.ascii_uppercase:
 with open(letter + ".txt", "w") as f:
    f.writelines(letter)
print("Successfully Created")
#------------------
#import string
def letters_file_line(n):
 with open("words1.txt", "w") as f:
    alphabet = string.ascii_uppercase
    letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
    f.writelines(letters)
letters_file_line(3)
print("Successfully Created")
#---------------------
import random
def random_line(fname):
     lines = open(fname).read().splitlines()
     return random.choice(lines)
print(random_line('text.txt'))
#---------------------
from collections import Counter
def word_count(fname):
 with open(fname) as f:
    return Counter(f.read().split())
print("Number of words in the file :",word_count('text.txt'))
#----------------------
with open('text.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
print("Successfully Copied")
