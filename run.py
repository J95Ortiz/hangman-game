# You can delete these comments, but do not change the name of this file

# Importing random so the computer chooses a random word to use in the game
import random

# Setting up the names for word files
easy = open("easy.txt", "r")
print(easy)
medium = open("medium.txt", "r")
print(medium)
########## hard = 
########## mix = 

# Fn asking for User's name, will add code to set up game
def introduction():
    print("Hello!")
    name = input("What's your name? \n")
    game_request = input(f'Welcome to the Hangman Game {name}! \nDid you want to have a game?')
    if game_request.lower() == "yes":
         # Code requesting User chooses how hard the game should be
         print("There are three difficulty levels you can choose from (Easy, Medium and Hard), or you can have a mix of them all. \n")
         level_choice = input("Please choose a level now (Easy, Medium, Hard or Mix):\n").lower()
         return level_choice
    else:
        introduction()

# Calls the introduction fn, and assigns level a value to be used in the next fn (word_choice)
###level = introduction()
###print(level)


# Fn takes level's value from prev. fn & uses it to open the relevant text file, then chooses a random word to use.
def word_choice(level):
    if level == "easy":
        word_selector = easy.read().split("\n")
    elif level == "medium":
        word_selector = medium.read().split("\n")
    
    word = random.choice(word_selector)
    return word
    #print(word)

# Calls the word_choice fn, and assigns level_used a value """"to be used in the next fn (word_choice)"""""
###game_word = word_choice(level)
###print(game_word)

# Fn to go through letters in game_word and replace each with "_"
def make_word_secret(game_word):
    game_word = game_word.split()
    print(game_word)
    x = 0
    while x <= len(game_word):
        game_word.insert(game_word[x], "_")
        x +=1
        print(game_word)
    print(game_word)
#print(game_word)


#    for letter in game_word:
#        print(game_word.replace(letter, "_"))
        
game_word = "meticulous"
make_word_secret(game_word)



