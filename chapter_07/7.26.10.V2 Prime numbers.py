def is_factor(n):         # Test if a number is even or not
    if n > 2:
        if n % 2 == 0:        # Return True when a number is even
            return True
        else:                     # If n is an odd number
            for i in range(2, n): # list of number from 2 to n-1
                if n % i == 0:    # Test if n is divisible by i
                    print('\nSome factors have been found in the odd number...')
                    return True   # Return True when it finds a factor of n
            return False          # Return False if it couldn't find a factor for n
    else:
        return False

        
def how_many_factors(n):
    for i in range(2, n):
        if n % i == 0:
            print(n, 'is divisible by', i)
            # Add a "Break" statement here to end when the first factor had been found
    
def is_it_prime_v2(n):
    if is_factor(n):
        print('')
        print(n, 'is a composite number')
        how_many_factors(n)
    else:
        print('')
        print(n, 'is a prime number')
        print('', 'It has no factors', sep='     ')

is_it_prime_v2(15)
is_it_prime_v2(6463297)