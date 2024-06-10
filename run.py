# You can delete these comments, but do not change the name of this file

# Importing random so the computer chooses a random word to use in the game
import random

# Setting up the names for word files
easy = open("easy.txt", "r")
########## medium = 
########## hard = 
########## mix = 

# Fn asking for User's name, will add code to set up game
def introduction():
    print("Hello!")
    name = input("What's your name? \n")
    print(f'Welcome to the Hangman Game {name}! \nDid you want to have a game?')
    
    # Code requesting User chooses how hard the game should be
    print("There are three difficulty levels you can choose from (Easy, Medium and Hard), or you can have a mix of them all. \n")
    level_choice = input("Please choose a level now (Easy, Medium, Hard or Mix):\n")
    # Turns input into lower case
    level_aplied = level_choice.lower()
    return level_aplied
    print(level_aplied)



# Fn which goes through chosen list and selects a word to use
def word_choice(level):
    if level == easy:
        word_selector = easy.read().split("\n")
        word = random.choice(word_selector)
    # return word
        print(word)

level = introduction()
word_choice(introduction)

