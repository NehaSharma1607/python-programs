import textwrap
# Make a story line with blanks in it
# ask for some inputs for blanks of the story line
holiday = input("Enter the name of a holiday:")
noun1 = input("Enter a noun:")
place = input("Enter the name of a place:")
person=input("Enter the name of a person:")
adjective1 = input("Enter an adjective:")
body_part = input("Enter the name of a body part:")
verb1 = input("Enter a verb:")
adjective2 = input("Enter an adjective:")
noun2 = input("Enter a noun:")
food = input("Enter the name of a food item:")
plural_noun = input("Enter a noun in its plural form:")
print()
print("The story you made is:")
print()
story=f"i cant believe its already {holiday}" \
    f" i cant wait to put my {noun1} and visit every {place}" \
    f" in my neighbourhood.this year i am going to dress up as a  {person} with" \
    f" {adjective1} {body_part} before i {verb1} i make sure to grab my {adjective2} {noun2} " \
    f"to hold all of my {food}.Finally,all of my {plural_noun} are ready to go!"
print(textwrap.fill(story))
