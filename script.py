"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random

print("""
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
Welcome to the Number Guessing Game!
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
""")

play = input('Would you like to play?\nPlease enter \'y\' to continue...\n>    ')

def start_game():
    highscore = 10

    while True:
        
        print('HIGHSCORE: {}'.format(highscore))
        
        random_num = random.randint(1, 10)
        num_of_guesses = 0
        user_guess = None

        while user_guess != random_num:

            try:
                temp_user_guess = input("Guess which number I'm thinking of, between 1 and 10...\n>  ")
                user_guess = int(temp_user_guess)

                if user_guess < 1 or user_guess > 10:
                    raise ValueError('The number needs to be between 1 and 10.')
                    continue

                elif user_guess < random_num:
                    print('It\'s higher!')
                    num_of_guesses += 1
                    continue

                elif user_guess > random_num:
                    print('It\'s lower!')
                    num_of_guesses += 1
                    continue

                else:
                    num_of_guesses += 1
                    if num_of_guesses == 1:
                        print('Wow! You got it first time!')

                    elif num_of_guesses <= 5:
                        print('Got it! That was quick, it only took you {} guesses!'.format(num_of_guesses))

                    elif num_of_guesses <= 9:
                        print('You got it! Took you a while, though... {} guesses, actually.'.format(num_of_guesses))

                    elif num_of_guesses == 10:
                        print('Ouch! {} tries!? At least you got there eventually!'.format(num_of_guesses))

                    if highscore > num_of_guesses:
                        highscore = num_of_guesses
                        print('Congrats, you set a new highscore!')

            except ValueError as err:
                if "invalid" in str(err):
                    print('Oops! \'{}\' isn\'t a number... Please try again!'.format(temp_user_guess))

                else:
                    print('Oops! {} Please try again.'.format(err))
                continue
        
        play = input('Would you like to play again?\nEnter \'y\' to continue...\n >')
        if play.lower() != 'y':
            break
        else:
            continue

if play.lower() == 'y':
    start_game()
print('Thanks for playing!')