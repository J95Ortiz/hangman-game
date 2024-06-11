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

# Calls the word_choice fn, and assigns game_word a value to be used in the next fn (hide_word)
###game_word = word_choice(level)
###print(game_word)

# Fn to go through letters in game_word and replace each with "_"        
def hide_word(game_word):
    blank = "_" * len(game_word)
    return blank

#####random word to test fn, delete before submission!!!!!!############
game_word = "master" 

# Calls the hide_word fn, and assigns hidden_word the game_word with letters replaced as blanks
hidden_word = hide_word(game_word)
###print(hidden_word)

# Fn to check if User's guess is 
def check_guess(game_word):
    user_guess = input("Choose a letter you think might be in the word: ").lower()
    if user_guess.isalpha():
        if user_guess in game_word:
            print(hidden_word.replace("_", user_guess)) ### Need to change this as replaces all the letters instead of the right one :(((

lol = check_guess(game_word)

            
            




###FUNCTIONS & VARIABLES:
###introduction() - Gets user's name and level desired
###word_choice() - Takes the result from introduction() and chooses a word from the corresponding txt file. Then assigns it the variable name "game_word"
###hide_word() - Creates a new variable "blank" which is a string that has as many "_" as "game_word" has letters. "blank" is assignedd the variable "hidden_word" outside the fn when called
