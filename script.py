"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


# Print game header
print("""
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
Welcome to the Number Guessing Game!
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
""")

# User input - Would you like to play?
play = input('Would you like to play?\nPlease enter \'y\' to continue...\n>    ')

# Game function
def start_game():

    # default highscore set to 10 ('lowest' score possible)
    highscore = 100

    while True:
        # Print Highscore each time the game begins
        print('HIGHSCORE: {}'.format(highscore))

        # Random number is generated using range of 1-10
        random_num = random.randint(1, 10)

        # initialise variables for num_of_guesses and user_guess
        num_of_guesses = 0
        user_guess = None

        # Loopception. Will Loop until user has guessed correctly.
        while user_guess != random_num:

            # Begin Exception code
            try:
                # Temporary variable for input, for use in error code.
                temp_user_guess = input("Guess which number I'm thinking of, between 1 and 10...\n>  ")

                # Now convert string to integer (Will raise ValueError for wrong type of input)
                user_guess = int(temp_user_guess)
                
                # Catch numbers outside of range and set valueerror message and 'continue' loop
                if user_guess < 1 or user_guess > 10:
                    raise ValueError('The number needs to be between 1 and 10.')
                    continue
                
                # Set else if for num_lower and num_higher. Print message, increase num_of_guesses and 'continue' loop.
                elif user_guess < random_num:
                    print('It\'s higher!')
                    num_of_guesses += 1
                    continue

                elif user_guess > random_num:
                    print('It\'s lower!')
                    num_of_guesses += 1
                    continue
                
                # Show user how many guesses it took them to find the right number. 
                # I added some extra if/elif logic that changes the print message, dependent on num_of_guesses.
                else:
                    num_of_guesses += 1
                    if num_of_guesses == 1:
                        print('Wow! You got it first time!')

                    elif num_of_guesses <= 5:
                        print('Got it! That was quick, it only took you {} guesses!'.format(num_of_guesses))

                    elif num_of_guesses <= 10:
                        print('You got it! Took you a while, though. {} guesses, actually.'.format(num_of_guesses))

                    else:
                        print('Ouch! {} tries!? At least you got there eventually...'.format(num_of_guesses))

                    # Check if highscore, set highscore & print message.
                    if highscore > num_of_guesses:
                        highscore = num_of_guesses
                        print('Congrats, you set a new highscore!')
            
            # Exception code - deals with strings and integers seperately.
            except ValueError as err:
                if "invalid" in str(err):
                    print('Oops! \'{}\' isn\'t a number... Please try again!'.format(temp_user_guess))

                else:
                    print('Oops! {} Please try again.'.format(err))
                continue
        
        # Allow the user to play again - continue loop, else break loop and go to end game.
        play = input('Would you like to play again?\nEnter \'y\' to continue...\n >')
        if play.lower() != 'y':
            break
        else:
            continue

# Start game if 'y', otherwise, display exit message.
if play.lower() == 'y':
    start_game()
print('Thanks for playing!')