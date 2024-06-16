# You can delete these comments, but do not change the name of this file

# Importing random so the computer chooses a random word to use in the game
import random

# Setting up the names for word files
easy = open("easy.txt", "r")
medium = open("medium.txt", "r")
hard = open("hard.txt", "r")
mix = open("mix.txt", "r")


# Fn asking for User's name, will add code to set up game
def introduction():
    print("Hello!")
    name = input("What's your name?\n")
    game_request = input(f'Welcome to the Hangman Game {name}! \nDid you want to have a game? (yes/no)\n')
    if "yes" in game_request.lower():
         # Code requesting User chooses how hard the game should be
         print("There are three difficulty levels you can choose from (Easy, Medium and Hard), or you can have a completely random word.")
         level_choice = input("Please choose a level now (Easy, Medium, Hard or Random):\n").lower()
    else:
        introduction()
    
    if "easy" or "medium" or "hard" or "random" not in level_choice:
        print("Sorry, that's not an option, plese choose Easy, Medium, Hard or Random):\n")
        level_choice = input("Please choose a level now (Easy, Medium, Hard or Random):\n").lower()
    return level_choice.lower()
    


# Fn takes level's value from prev. fn & uses it to open the relevant text file, then chooses a random word to use.
def word_choice(level):
    if "easy" in level:
        word_selector = easy.read().split("\n")
    elif "medium" in level:
        word_selector = medium.read().split("\n")
    elif "hard" in level:
        word_selector = hard.read().split("\n")
    elif "random" in level:
        word_selector = mix.read().split("\n")
    # Assigns the word chosen by random.choice to the variable "game_word"
    # "word" is the word the User will try and guess
    game_word = random.choice(word_selector)
    return game_word


# Fn to go through letters and check if swaps the underscores for letters the user has guessed
def check_guess(game_word, user_guesses):
    word_with_guesses = ""
    for letter in game_word:
        if letter in user_guesses:
            word_with_guesses += letter
        else:
            word_with_guesses += "_"
    return word_with_guesses

# Fn that's called if User's guess isn't right
# Checks chances and displays the apropriate stick figure
def hanged_man(chances):
    hanged_man = [
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
        
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",

        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",

        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",

        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",

        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
    ]

    print(hanged_man[chances])


def rematch():
    rematch = input("Did you want another game? (yes/no)\n")
    if "yes" in rematch:
        introduction()
    else:
        print("Thanks for playing!")



###FUNCTIONS:
###introduction() - Gets user's name and level desired
###word_choice() - Takes the result from introduction() and chooses a word from the corresponding txt file. Then assigns it the variable name "game_word"
###hide_word() - Creates a new variable "blank" which is a string that has as many "_" as "game_word" has letters. "blank" is assignedd the variable "hidden_word" outside the fn when called

###VARIABLES
###easy = open("easy.txt", "r")
###medium = open("medium.txt", "r")




# Fn to start game
def game_start():
    user_guesses = []
    intro = introduction() # Asks User for name and level they want to play
    word = word_choice(intro) # Uses User's level request to access relevant file and choose a word for them to guess
    blank = "_" * len(word) # Swaps the letters for "_"s
    chances = 7
    print("****************************")
    print(f"Your word has {len(blank)} letters")
    print(f"This is your word: {blank}\n") # Displays the word to the User
    print("****************************")
    while chances > 0:
        user_guess = input("Choose a letter you think might be in the word: ").lower()

        # Checks if User's inputted more than one letter
        if len(user_guess) != 1:
            print("You can only enter one letter at a time!")
        else:

        # Nested statment to check if input is valid
            if user_guess.isalpha():
                # Checks if User's guess has already been tried
                if user_guess in user_guesses:
                    print("You've already tried that letter")
    
                else:
                    user_guesses.append(user_guess)
                    
                    if user_guess in word:
                        print("That's in!")
    
                    # Guess is a letter but wrong  
                    else:
                        print("That letter isn't in")
                        chances -= 1
                        hanged_man(chances)      
            
            # Guess is not a letter
            else:
                print("Not a letter, please choose a letter")
                #print(f"This is your word {blank}")
                #word_with_guesses = check_guess2(word, user_guesses)       
                #print(word_with_guesses)
            
        # Runs through the word, swaps the underscores for letters the user has guessed
        word_with_guesses = check_guess(word, user_guesses)

        # Prompts User for another guess 
        if chances != 0:
            print(f"Have another go: \n{word_with_guesses}\n")

        # Displays letters User has guessed so far to them
        print(f"You've guessed these letters so far: {user_guesses}")

        # Tells User how many wrong guesses they have left
        print(f"You have {chances} guesses left\n")
        print("****************************")

        # User got the word with chances left
        if "_" not in word_with_guesses:
            print("Congrats you won!")
            rematch()
            break

    # User's ran out of chances and not guessed the word
    if chances == 0:
        print("Sorry, you lost! ☹")
        print(f"Your word was {word}")
        rematch()

    

game_start()


### IF WRONG GUESS, ADD TO HANGMAN
### DRAW HANGMAN, IF CHANCES = 7 FULL, IF CHANCES = 6 ADD HEAD, ETC

