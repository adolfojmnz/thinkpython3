# 12.1 Random Numbers.
import random
rng = random.Random() # Create a black box object that generates random numbers

dice_throw = rng.randrange(1,7)   # Return an int, one of 1,2,3,4,5,6
delay_in_seconds = rng.random() * 5.0
r_odd = rng.randrange(1, 100, 2)

cards = list(range(52))  # Generate ints [0 .. 51]
rng.shuffle(cards)       # Shuffle the pack

def printing_random_numbers():
    print(dice_throw)
    print(delay_in_seconds)
    print(r_odd)
    print(cards)

# 12.1.1.1 Repeatability and Testing.
drng = random.Random(123)  # Create generator with known starting state
print(drng.random())
