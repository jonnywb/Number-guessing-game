"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution. -- Number chosen from within range
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )

    For Extra credit:
    -----------------
    1. As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
        (For example, if the range is 1-10 and the player enters 12 they should be informed that this number is outside the range.)
    2. As a player of the game, after I guess correctly I should be prompted if I would like to play again.
    3. As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
    4. Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.

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