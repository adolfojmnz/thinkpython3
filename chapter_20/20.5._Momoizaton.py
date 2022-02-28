import time

known = {0: 0, 1: 1}

def fib(n):
    if n not in known:
        value = fib(n-1) + fib(n-2)
        known[n] = value
    return known[n]

t0 = time.time()
num = fib(900)
t1 = time.time()

print(num, len(f'{num}'))
print(f'Total run time: {t1-t0:.9f}')

