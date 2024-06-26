# **TESTING**

# MANUAL TESTING

## USER TESTING

The application was thoroughly tested using VS Code's Terminal and there are no issues currently present with the application.

## INPUT VALIDATION

The app has been built so that whenever a User's input is required this is validated. The instructions at the beginning do ask for any input to be "yes" or "no" unless specified otherwise in an attempt to minimise any errors, however further checks throughout the code will deal with any other issues. The User will always see a message should any issues arise.

- **When they are asked to provide their name** the code checks that the User has only included letters or numbers. Any blank entries or special characters aren't allowed and an Error message is displayed to them asking them to only use letters and numbers

![Error message on name](readme_images/error_message_name.png)

- **When they are asked what level of difficulty** they want the program will only accept the User's input if they've typed in a number between 1 & 4. If they add any other number they are asked to only choose numbers between 1 & 4, and if they type in a letter, blank or special character a message will appear to say that their input is not a number and to please choose one of the options.

![Level number error message](readme_images/error_message_level.png)

- **When they're asked to guess a letter** the code will check that only letters are entered. Any numbers, blank entries or special characters will prompt a message to appear and ask that only letters are entered. If more than one letter is entered a message will ask them to only submit one letter at a time, and if they've already tried a letter the app will let them know and ask for another guess.

![Too many letters error message](readme_images/error_message_letters.png)

![Special Character as guess error message](readme_images/error_message_special_character.png)

![Number as guess error message](readme_images/error_message_number.png)

- **When the game ends and they are asked if they want to play again** the app will process the User's response. If anything but "yes" or "no" is entered, they will be asked to only respond using "yes" or "no".

![Error message for empty input](readme_images/error_message_rematch_blank.png)

![Error message for numbers](readme_images/error_message_rematch_number.png)

![Error message for invalid input](readme_images/error_message_rematch_other.png)

# BUGS

## FIXED BUGS

There were some bugs which arose during the building process and these are listed below along with the steps taken to resolve them:

- If a User tried a letter that wasn't correct, and then tried it again within the same game the app would take away two lives instead of just one. A condition was then added which checked if their guess had been tried already and if so, no lives would be taken and the User would see a message telling them they already tried it.

- Originally the introduction() function would accept blank input and special characters, so a condition was applied so only letters and/or numbers are now accepted.

No further bugs have been detected in the application.

# PERFORMANCE & ACCESSIBILITY

## CODE VALIDATION

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to test the code in the app and there are no issues.

![CI PEP8 Validator results](readme_images/pep8_validator_results.png)

## BROWSER COMPATIBILITY

The application was tested on the following browsers and it ran without any issues:

- Google Chrome

- Microsoft Edge

- Mozilla Firefox

## GOOGLE LIGHTHOUSE RESULTS

The Lighthouse feature on Google Chrome's Dev Tools was used in order to carry out performance testing. A screenshot showing the results can be seen below:

![Google Lighthouse results](readme_images/lighthouse_results.png)
