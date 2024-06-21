# **HANGMAN WORD GUESSING GAME**

# INTRODUCTION

![AmIResponsive Screenshot]()

This programme is a digital version of Hangman, the popular game believed to have started in the 17th Century.

It is a Command Line Interface Application designed for a single User to play this classic game. It has three levels of difficulty and a random level, in which a word of any level can be picked.

The game was designed so that anyone can play it, from children to adults. The aim is to improve the User's vocabulary and spelling abilities in a way that is interactive and doesn't feel boring.

If you want to try it out, please follow the link below to access the application:

- [Hangman Game](https://hangman-game-joe-ortiz-bab2aa56a3ab.herokuapp.com/)

# CONTENTS

- [INTRODUCTION](#introduction)

- [CONTENTS](#contents)

- [USER EXPERIENCE](#user-experience)

  - [User's Stories](#user's-stories)

    - [Primary Goal](#primary-goal)
    - [Visitor Goals](#visitor-goals)
      - [First Time Visitors](#first-time-visitors)
      - [Returning Visitors](#returning-visitors)
      - [Frequent Visitors](#frequent-visiors)

  - [Creation Process](#creation-process)
    - [Planning](#planning)
    - [App Flowchart](#app-flowchart)
    - [App Structure](#app-structure)
    - [Python Logic](#python-logic)
  - [Design Choices](#design-choices)

- [FEATURES](#features)

  - [Outline](#outline)

  - [Main Features](#main-features)

    - [Welcome Message](#welcome-message)
    - [Instructions](#instructions)
    - [Difficulty Levels](#difficulty-levels)
    - [Game Process](#game-process)
    - [Choosing a Word & Displaying It To The User](#choosing-a-word--displaying-it-to-the-user)
    - [Processing The User's Guesses](#processing-the-users-guesses)
    - [Lives & Stickman Art](#lives--stickman-art)
    - [Game End & Rematch Request](#game-end--rematch-request)

  - [Future Features](#future-features)

- [TECHNOLOGIES USED](#technologies-used)

- [PYTHON PACKAGES](#python-packages)

- [TESTING](#testing)

  - [Manual Testing](#manual-testing)
  - [External Testing](#external-testing)

            ******Think about adding a separate testing.md file******

  - [Performance & Accessibility](#performance--accessibility) - Include in testing.md
  - [Validator Testing](#validator-testing) - Include in testing.md

  - [Troubleshooting](#troubleshooting) - Include in testing.md

- [DEPLOYMENT TO HEROKU](#deployment)

  - [Project Deployment](#project-deployment)
  - [How to fork the repository from Github](#how-to-fork-the-repository-from-github)
  - [How to clone the project](#how-to-clone-the-project)

- [CREDIT](#credit)
  - [Content Credits](#content-credit)
  - [Media Credts](#media-credits)
  - [Acknowledgements](#acknowledgements)

# USER EXPERIENCE

[Back to top](#contents)

## USER'S STORIES

### PRIMARY GOAL

The main goal this programme was built for was to provide Users with a digital alternative to the Hangman game.

This aim of the game is that over time the User improves their spelling and vocabulary in a dynamic fashion.

[Back to top](#contents)

### VISITOR GOALS

The application was created for people who enjoy playing this type of game. Its use should feel simple and straightforwards, and instructions have been provided to ensure users feel confident they know how to use it without issues or difficulties.

The User can choose a difficulty level at the beginning, and once the game has completed they are asked if they want to replay. They are also able to choose a difficulty at this stage.

[Back to top](#contents)

#### FIRST TIME VISITORS

First time visitors will:

- Be able to add their name at the start
- Read the instructions before starting
- Know how many chances they have to guess the word (lives)
- Choose a difficulty level
- Guess a letter they think is in the word
- Depending on the outcome of the game they will get a different message
- Have the ability to have another game

[Back to top](#contents)

#### RETURNING VISITORS

Returning visitors will still have the same cues and messages as a first time User.

The numbers for each level are always the same, so as soon as they type their name and press the Enter key they are able to choose the level they want, and don't have to read the instructions each time before selecting.

[Back to top](#contents)

#### FREQUENT VISITORS

A frequent visitor will know the structure and how the game works. They shouldn't feel the need to read through the instructions and would know which number corresponds to each level and how the game works.

[Back to top](#contents)

## CREATION PROCESS

### PLANNING

At the start of the project there were a few different ideas I was considering. I made a list of the different ideas and set out a basic structure for each.

After doing some research into the different projects I was thinking, I decided to build a version of Hangman.

[Back to top](#contents)

### APP FLOWCHART

![Lucidcharts Flowchart]()

The flowchart was created using [Lucid Charts](https://www.lucidchart.com/pages/).

I followed the suggestions in the [Love Sandwiches Walkthrough](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) and the first thing I did once I'd decided to build a Hangman game for this project was create a flowchart.

I found it a very helpful tool to visualize the structure the application should have and logic it should follow.

[Back to top](#contents)

### APP STRUCTURE

The app structure is very simple as it was built to be a Command Line Interface Application.

[Back to top](#contents)

### PYTHON LOGIC

The logic used in this programme is quite straightforwards.

The User's response is validated whenever they are asked for input. If the input doesn't meet the requirements for the application to proceed, the User will be shown a message prompting them to answer a specific way.

Plenty of testing was done to ensure that the messages the User will see are relevant to the issue.

[Back to top](#contents)

## DESIGN CHOICES

The minimalist design used is due to it being built to be used in a Command Line Interface. The advantage here is that the structure is simple and easy for Users to understand and play.

ASCII characters were used on each of the Hangman drawings Users see if they get a letter wrong.

[Back to top](#contents)

# FEATURES

## OUTLINE

The game outline is as follows:

1. The User is greeted by the computer and asked for their name.

2. They are shown the instructions and asked their preferred difficulty level for the game.

3. The letters are swapped for underscores, and the User is shown the word and told how many letters are in it.

4. The User is prompted to guess a letter.

5. The User keeps getting asked to guess a letter until they guess all the letters, or they run out of lives.

6. Once the game ends the User is asked if they'd like to play again.

7. If they choose to play again they will have to choose their difficulty level and the game restarts.

[Back to top](#contents)

## MAIN FEATURES

### WELCOME MESSAGE

When a User starts the application they are greeted by the computer and asked to type out their name.

Only letters and numbers are allowed in a User's name, so input validation checks for any special characters and ensures that a blank name isn't entered either. If the programme encounters any characters which aren't accepted, the User will see a message asking them to only input letters and numbers.

The computer then displays a message using the name the User entered welcoming them to the "Hangman Game".

[Back to top](#contents)

### INSTRUCTIONS

Once the User has been welcomed to the game, the display will load the instructions and ask them to choose a level of difficulty.

Once they have chosen, the next screen will tell them how many letters in the word, and ask them to type their first guess.

The programme only accepts 1, 2, 3 or 4 as options at the Instructions stage, so if a User types anything else a message will pop up and ask them to please choose an option betwen 1 and 4. The input validation also takes into account any input that isn't numerical and in this case displays a slightly different message.

[Back to top](#contents)

### DIFFICULTY LEVELS

There are three difficulty levels a User can choose as well as a random word option.

There are around 50 easy words, 50 medium words and 30 hard words in the hard level. So as to make the game more fun to a frequent User they can also choose the random option which chooses a word that could be of any difficulty.

- The Easy words are between 3 and 5 letters long.

- The Medium difficulty words words are between 5 and 9 letters long.

- The Hard words have at least 7 letters and are meant to present more of a challenge for a User.

[Back to top](#contents)

### CHOOSING A WORD & DISPLAYING IT TO THE USER

Once the User has chosen the level they want, the application runs through the words in the corresponding file and selects one for them to guess.

Every letter in the word is then replaced with an underscore. This is displayed to the User along with a message telling them how many letters there are. They are then asked for their first guess.

[Back to top](#contents)

### PROCESSING THE USER'S GUESSES

Once the User has entered their first guess the program checks whether that letter is in the word.

The application checks that the input isn't blank or more than one character in length, and asks the user to only input letters if their guess is a number or special character.

If the User's guess appears in the word, the screen will display a message confirming their guess is right and the app replaces the underscores with the letter.

When the Users are asked for their next guess they are shown the word which now includes the letter they last guessed.

If the letter they guessed does not appear, a message appears telling them that letter isn't in. The stickman is also shown at this stage with a message telling the User how many chances they have left.

Each guess is added to a list which is displayed back to the User after each turn, so they can see what letters they've guessed. However, if a letter is guessed more than once a message tells them that they've already tried it.

The process is repeated until all the letters are guessed and the word is revealed, or they run out of chances.

[Back to top](#contents)

### LIVES & STICKMAN ART

The User can have up to seven incorrect guesses per game.

If they don't guess the word before running out of lives then they will see a message telling them what the word was, and ask them if they'd like to play again.

Each time an incorrect guess is entered the User is told that the letter isn't in. The stickman will also be displayed at this stage.

The stickman the User sees will depend on the lives they have left, and it was created using ASCII characters.

[Back to top](#contents)

### GAME END & REMATCH REQUEST

When the word has been guessed or the User has no more lives left, a message is displayed which asks the User if they'd like to play again.

Input validation checks the input and if it's anything but "yes" or "no" another message is shown prompting the user to only use these.

If they don't want to play again, the computer thanks them for playing and the application quits.

If they choose to have another game they will have to choose the level they want, and the game will start.

[Back to top](#contents)

## FUTURE FEATURES

In future I would like to add an option so that if a User does know the word they can type it in, instead of just a letter and I'd like to implement this as a form of "sudden death". This would mean that if the word guessed is incorrect they will lose any remaining lives, and they will be asked if they want to play again.

I will also be adding more words to each difficulty level.

I would also like to add more animations and will look into applying more ASCII designs.

[Back to top](#contents)

# TECHNOLOGIES USED

- [Github](https://github.com/) - Used to create and host the repository.
- [Heroku](https://heroku.com/) - Used to deploy and run the application.
- [Gitpod](https://gitpod.io/) - Used together with VS Code to build the application.
- [Visual Studio Code Desktop Application](https://code.visualstudio.com/) - Used to code and build the application.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to check and validate the code for the application.
- [Lucid Charts](https://www.lucidchart.com/pages/) - Used to create the initial flowchart for the application.

[Back to top](#contents)

# PYTHON PACKAGES

- [Random](https://docs.python.org/3/library/random.html) - Used to select a word for the User to guess.

[Back to top](#contents)

# TESTING

[Back to top](#contents)

## MANUAL TESTING

[Back to top](#contents)

## EXTERNAL TESTING

[Back to top](#contents)

                ******Think about adding a separate testing.md file******

## PERFORMANCE & ACCESSIBILITY - Include in testing.md

[Back to top](#contents)

## VALIDATOR TESTING - Include in testing.md

[Back to top](#contents)

## TROUBLESHOOTING - Include in testing.md

[Back to top](#contents)

# DEPLOYMENT TO HEROKU

[Back to top](#contents)

## PROJECT DEPLOYMENT

[Back to top](#contents)

## HOW TO FORK THE REPOSITORY FROM GITHUB

[Back to top](#contents)

## HOW TO CLONE THE PROJECT

[Back to top](#contents)

# CREDIT

[Back to top](#contents)

## CONTENT CREDIT

[Back to top](#contents)

## MEDIA CREDITS

[Back to top](#contents)

## ACKNOWLEDGEMENTS

[Back to top](#contents)
