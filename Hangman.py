import random

animals = ["LION", "TIGER", "HYENA", "DOGS", "CATS", "COW", "GOAT", "OX", "MONKEY","BEAR", "HORSE", "DONKEY", "CAMEL"]
countries = ["BRAZIL", "GERMANY", "FRANCE", "ITALY", "FINLAND", "SWITZERLAND"]
colours = ["RED", "PINK", "BLACK", "WHITE", "BLUE", "GREY", "TEAL", "ORANGE", "BROWN", "PEACH", "SILVER", "GOLD"]
subject = input("You want to play in which subject(in small letters)[animals,countries,colours]:")


def game(word):
    #print(word)
    guesses = ""
    failed = 0
    print("The number of attempts you get is equal to the number of letters in the word!!WATCH OUT! ")

    for turns in range(1, len(word)+1):

        guess = input("Enter your guess(in capital letters):")
        guesses += guess

        for char in word:
            if char in guesses:
                print(char)

            else:
                print("-")
                failed += 1

    if guesses == word:
        print("YOU WIN!!")
        print("THE WORD IS:", word)

    else:
        print("Nah! That's not right!")
        print("You loose!!")
        print("THE WORD IS:", word)


if subject == "animals":
    print("Great! Lets start the game!")

    game(random.choice(animals))
elif subject == "countries":
    print("Great! Lets start the game! ")

    game(random.choice(countries))
elif subject == "colours":
    print("Great! Lets start the game! ")

    game(random.choice(colours))
else:
    None
