def is_prime(n):
    if n > 2:
        if n % 2 == 0:  # Is n is even
            return False
        else:           # Is n is odd
            for i in range(2, n): 
                if n % i == 0:  # Is n has factors
                    return False
            return True
    return True

def primes_lessthan(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
           result.append(i)
    return result


print(primes_lessthan(15))