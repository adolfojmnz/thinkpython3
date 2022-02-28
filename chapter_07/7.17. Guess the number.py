import random

def guess_the_number():
    rng = random.Random()
    number = rng.randint(1, 1000)

    guesses = 0
    msg = ''

    while True:
          guess = int(input(msg + '\nGuess my number from 1 and 1000.\nR:'))
          guesses += 1
          if guess > number:
             msg += str(guess) + ' is too high.\n'
          elif guess < number:
               msg = str(guess) + ' is too low.\n'
          else: break

    input('\n\nGreat! You got it in {0} guesses.\n\n'.format(guesses))
