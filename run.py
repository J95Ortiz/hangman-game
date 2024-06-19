"""
HANGMAN GAME:

- Code set up so that the User is greeted by the computer and asked for their
name.

- They are then asked to choose a difficulty level.

- The computer will then choose a random wrd from the corresponding file and
 replace the letters with underscores.

- A loop is then ran whereby the User is meant to guess a letter they think is
in the word.

- Once the word is guessed or they run out of lives the User is asked if they'd
like a rematch.

- If they do they are asked which level they want to play again and the process
restarts, but if they say no then the computer thanks them for playing and the program ends.

"""

# Importing random module to be used when choosing a random word to use
import random


# Fn asking for User's name
def introduction():
    print("Hello!")

    while True:
        name = input("What's your name?\n")

        if not name.isalnum():
            print("Sorry please only use letters and numbers")
            continue
        else:
            break

    print(f"Welcome to the Hangman Game {name}!")
    # Instructions printed out to the User
    print(
        """
Please only answer yes or no unless you're prompted for a different answer.

Your goal is to reveal the hidden word by guessing a letter you think might be in it.

There are three difficulty levels you can choose from, or you can have a completely random word.

If your guess is correct I'll pop the letter you choose wherever it appears in the word, but if it's wrong you'll lose a life and the stickman won't be happy!

Whatever level you choose you'll always get 7 chances so don't worry if you don't get it as you'll have the chance for a rematch once the game has finished.

\tGOOD LUCK!! 😁
                    """)


# Fn that asks User what level they want & uses it to open the relevant text file, then chooses a random word to use.
def word_choice():

    # Code requesting User chooses how hard the game should be
    print("""
Please type:

    1 - For an Easy word

    2 - For an Average word

    3 - For a Hard word

    4 - For a Random word
    """)

    # Handles any input that isn't a level option
    while True:
        try:
            word_selector = int(input("Please choose a level now:\n"))

            if word_selector not in (1, 2, 3, 4):
                print("Please choose an option between 1 & 4")
                continue

        except ValueError or TypeError:
            print("Sorry that isn't a number, please choose a level.")
            continue

        else:
            break

    # Uses User's choice to open the apropriate file
    if word_selector == 1:
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

    # Computer goes through txt file and assigns the word chosen by random.choice to the variable "game_word".
    # This values is then used as the game_start() function's argument
    game_word = random.choice(word_selector)
    return game_word


# Fn used in game_start() that checks if the User's guessed letter is in game_word, and swaps any underscores for this letter if it's in. Otherwise it keeps the underscore.
# The blank word with User's guesses is returned as "word_with_guesses".
def check_guess(game_word, user_guesses):
    word_with_guesses = ""
    for letter in game_word:
        if letter in user_guesses:
            word_with_guesses += letter
        else:
            word_with_guesses += "_"
    return word_with_guesses


# Fn that's called if User's guess isn't right and checks their chances.
# Then it displays the apropriate stick figure depending on how many they have left.
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


# Fn combining most functions and starts the game after the intro and level_choice functions.
def game_start(word):

    user_guesses = []  # Empty list to store User's guesses
    chances = 7
    blank = "_" * len(word)  # Swaps the letters for "_"s

    print("****************************")
    print(f"Your word has {len(blank)} letters")  # Tells the User how many letters in the word.
    print(f"This is your word: {blank}\n")  # Displays the word to the User as just underscores.

    # Loop that runs while User has chances left
    while chances > 0:
        user_guess = input("Choose a letter you think might be in the word: \n").lower()
        print("****************************")

        # Checks if User's inputted more than one letter
        if len(user_guess) != 1:
            print("You can only enter one letter at a time!")
            print("****************************")

        else:

            # Nested statment to check if input is a letter
            if user_guess.isalpha():

                # Checks if User's guess has already been tried
                if user_guess in user_guesses:
                    print("You've already tried that letter")

                # Adds their guess to the user_guesses list
                else:
                    user_guesses.append(user_guess)

                    # Tells the User the letter they guessed is in the word
                    if user_guess in word:
                        print("That's in!")
                        print("****************************")

                    # User guesses a letter but it's wrong
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
        print(f"You have {chances} lives left\n")
        print("****************************")

        # User got the word with chances left
        if "_" not in word_with_guesses:
            print("Congrats you won!")
            print("****************************")
            break

    # User's ran out of chances and not guessed the word
    if chances == 0:
        print("Sorry, you lost! ☹")
        print(f"Your word was {word}")

    # Checks with User if they wanted to play again
    while True:
        rematch_question = input("Did you want another game?\n")
        rematch = str(rematch_question)

        # Checks User's input is either a "yes" or a "no"
        # If neither, message displayed requesting User only enter "yes" or "no"
        if rematch.lower() not in ("yes", "no"):
            print("Sorry I didn't understand that, please only answer yes or no")
            print("****************************")
            continue

        # Goodbye message displayed if User's input is "no"
        if rematch.lower() == "no":
            print("Thanks for playing!")
            print("****************************")
            break

        # If User's input is "yes" game restarts
        if rematch.lower() == "yes":
            print("****************************")
            # Word_choice function ran again within function so a new random word is chosen.
            new_word = word_choice()
            game_start(new_word)
            break


# Calls the intro() function.
introduction()

# Runs word_choice function to set up first game.
word = word_choice()

# Sets up first game for the User and runs in a loop until User doesn't say "yes" when asked if they want to play again.
game_start(word)
