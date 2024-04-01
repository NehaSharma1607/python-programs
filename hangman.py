

import random

def hangman():
  words = ['apple', 'banana', 'cherry', 'mango', 'orange']
  chosen_word = random.choice(words)
  guessed_letters = []
  attempts = 6

  while attempts > 0:
    print("\n")
    print("Word:", end=" ")
    for letter in chosen_word:
      if letter in guessed_letters:
        print(letter, end=" ")
      else:
        print("_", end=" ")

    print("\n")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single letter.")
      continue

    if guess in guessed_letters:
      print("You already guessed that letter.")
      continue

    guessed_letters.append(guess)

    if guess in chosen_word:
      print("Correct!")
    else:
      print("Incorrect.")
      attempts -= 1

    if all(letter in guessed_letters for letter in chosen_word):
      print("\n")
      print("You win!")
      break

  if attempts == 0:
    print("\n")
    print("You lose! The word was", chosen_word)

hangman()
