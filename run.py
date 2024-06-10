# You can delete these comments, but do not change the name of this file

# Importing random so the computer chooses a random word to use in the game
import random

# Fn asking for User's name, will add code to set up game
def introduction():
    print("Hello!")
    name = input("What's your name? \n")
    print(f'Hi {name}, did you want to have a game of Hangman?')


# Fn which goes through chosen list and selects a word to use
def word_choice():
    with open("easy.txt", mode="r") as file:
        word_selector = file.read().split("\n")
    word = random.choice(word_selector)
    print(word)


introduction()
word_choice()

