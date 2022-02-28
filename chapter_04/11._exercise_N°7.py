# Write a fruitful function sum_to(n) that returns
# the sum of all integer numbers up to and including
# n. So sum_to(10) would be 1+2+3...+10 which would
# return the value 55.

def _sum(start, stop, steps):   # Today's.
    n = 0
    for i in range(start, stop+1, steps):
        n += i
    return n

def sum_to(n):                  # Two moths ago.
    m = n
    for i in range(n):
        m = m + (n - 1)
        n = n - 1
    return m


#print('The sum from 1 to', x, 'is:', sum_to(10))
print(_sum(1, 10, 1))
print(_sum(55, 100, 3))
print(_sum(2, 10, 3))
print(_sum(197, 1000, 89))
