# You can delete these comments, but do not change the name of this file

# Importing random so the computer chooses a random word to use in the game
import random



# Fn asking for User's name, will add code to set up game
def introduction():
    print("Hello!")
    name = input("What's your name?\n")
    print(f"Welcome to the Hangman Game {name}! \nPlease only answer yes or no unless you're prompted for a different answer")
    # game_request = input(f'Did you want to have a game {name}?\n')
    #while "yes" or "no" not in game_request.lower():
    #    print(game_request)
    #    print("Sorry I didn't understand that, please only answer yes or no\n")
    #    game_request = input(f'Did you want to have a game {name}?\n')
    #    
#
    #    if "yes" in game_request.lower():
    #        game_start()
    #    #pass
#
    #    elif "no" in game_request.lower():
    #        print("No worries!")
    #        print("****************************")
    #        introduction()
    
        


    
# Fn takes level's value from prev. fn & uses it to open the relevant text file, then chooses a random word to use.
def word_choice():
     # Code requesting User chooses how hard the game should be
    print("There are three difficulty levels you can choose from or you can have a completely random word.")
    print("\nPlease type:\n1 - For an Easy word \n2 - For an Average word \n3 - For a Hard word \n4 - For a Random word \n")
    
    while True:
        try:
            word_selector = int(input("Please choose a level now:\n")) # Attempting to use easy, random, etc.
             
            # word_selector = int(input("Please choose a level now:\n"))
            if word_selector not in (1,2, 3, 4):
                print("Please choose an option between 1 & 4")
                continue

        except ValueError or TypeError:
            print("Sorry that isn't a number, please choose a level.")
            continue

        else:
            break

        

    if word_selector == 1:
        # Setting up the names for word files
        easy = open("easy.txt", "r")
        word_selector = easy.read().split("\n")
    elif word_selector == 2:
        medium = open("medium.txt", "r")
        word_selector = medium.read().split("\n")
    elif word_selector == 3:
        hard = open("hard.txt", "r")
        word_selector = hard.read().split("\n")
    elif word_selector == 4:
        mix = open("mix.txt", "r")
        word_selector = mix.read().split("\n")
      

    # Assigns the word chosen by random.choice to the variable "game_word"
    # "word" is the word the User will try and guess
    game_word = random.choice(word_selector)
    #print(game_word)
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


#def rematch():
#    while True:
#        rematch = input("Did you want another game?\n")
#        game_start()
#        if "yes" in rematch:
#            print("****************************")
#            return True
#        else:
#            print("Thanks for playing!")
#            return False
        

#def rematch():
#    while True:
#        rematch = input("Did you want another game?\n")
#        if rematch.lower() == "no":
#            return False
#        elif rematch.lower() == "yes":
#            return True



###FUNCTIONS:
###introduction() - Gets user's name and level desired
###word_choice() - Takes the result from introduction() and chooses a word from the corresponding txt file. Then assigns it the variable name "game_word"
###hide_word() - Creates a new variable "blank" which is a string that has as many "_" as "game_word" has letters. "blank" is assignedd the variable "hidden_word" outside the fn when called

###VARIABLES
###easy = open("easy.txt", "r")
###medium = open("medium.txt", "r")

def replay():
    game_start()




# Fn to start game
def game_start(word):    
    
    user_guesses = []
    chances = 7
    blank = "_" * len(word) # Swaps the letters for "_"s
    print("****************************")
    print(f"Your word has {len(blank)} letters")
    print(f"This is your word: {blank}\n") # Displays the word to the User

    
    while chances > 0:
        user_guess = input("Choose a letter you think might be in the word: ").lower()
        print("****************************")
     # Checks if User's inputted more than one letter
        if len(user_guess) != 1:
            print("You can only enter one letter at a time!")
            print("****************************")
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
                        print("****************************")
    
                    # Guess is a letter but wrong  
                    else:
                        print("That letter isn't in")
                        chances -= 1
                        hanged_man(chances)
                        print("****************************")      
            
            # Guess is not a letter
            else:
                print(f"{user_guess} is not a letter, please choose a letter")
                print("****************************")
            
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
            print("****************************")
            #rematch()
            break
            #replay()
            
 # User's ran out of chances and not guessed the word
    if chances == 0:
        print("Sorry, you lost! ☹")
        print(f"Your word was {word}")
        #rematch()
        #return
        #break
        #replay()
       
    rematch = input("Did you want another game?\n")
    if rematch.lower() == "yes":
        new_word = word_choice()
        game_start(new_word)
    
        
    else:
        print("Thanks for playing!")
        
        
    






#while True:
#    game_start()
#    rematch = input("Did you want another game?\n")
#    if rematch.lower() != "yes":
#        break
#print("Thanks for playing!")

introduction()       
word = word_choice() # Uses User's level request to access relevant file and choose a word for them to guess
game_start(word)


### IF WRONG GUESS, ADD TO HANGMAN
### DRAW HANGMAN, IF CHANCES = 7 FULL, IF CHANCES = 6 ADD HEAD, ETC

