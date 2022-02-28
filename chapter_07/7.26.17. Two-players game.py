# You and your friend are in a team to write a two-players game,
# human against computer, such as Tic-Tac-Toe / Noughts and Crosses.
# Your friend will write the logic to play one round of the game,
# while you will write the logic to allow many rounds of play,
# keep score, decide who plays, first, etc.
# The two of you negotiate on how the two parts of the program will fit together,
# and you come up with this simple scaffolding (which your friend will improve later):

"""
   Must play one round of the game. If the parameter
   is True, the human gets to play first, else the
   computer gets to play first.  When the round ends,
   the return value of the function is one of
   -1 (human wins),  0 (game drawn),   1 (computer wins).
"""

import random

def play_once(human_plays_first):
    rng = random.Random()
    result = rng.randrange(-1,2)
    if human_plays_first: # If True, human plays first | plays
        player = "Human plays first"
    elif not human_plays_first: # If False, computer plays first | plays
        player = "Computer plays first"
    print(player,  '\nNum =', result)
    return result


def play_again(boolean):
    win = 0
    drawn = 0
    loss  = 0
    while True:
        result = play_once(boolean)
        if result == 1:
            print('Computer wins')
            loss += 1
            boolean = False
        elif result == 0:
            print('Shame! Game drawn...')
            drawn += 1
            boolean = not boolean
        elif result == -1:
            print('Human wins')
            win += 1
            boolean = True
        print("\nHuman's wins:",win, "\nComputer's wins:",loss, "\nDrawns:",drawn)
        total_rounds = win + loss + drawn
        value = ('{0:.2f}'.format(win/total_rounds)) #value = int((win/total_rounds * 100)*10)/10
        print('Human has win the', value,'% of the total rounds')
        ask = input('\nDo you want to play again?'
                    '\nEnter Y or N'
                    '\n-')
        if ask == 'Y' or ask == 'y':
            continue
        else:
            print('Goodbye')
            break


play_again(True)

#   Write the main program which repeatedly calls this function to play the game,
#   and after each round it announces the outcome as: “I win!”, “You win!”, or “Game drawn!”.
#   It then asks the player “Do you want to play again?” and either plays again, or says “Goodbye”, and terminates.

#   Keep score of how many wins each player has had, and how many draws there have been.
#   After each round of play, also announce the scores.

#   Add logic so that the players take turns to play first.

#   Compute the percentage of wins for the human, out of all games played.
#   Also announce this at the end of each round.

#   Draw a flowchart of your logic.