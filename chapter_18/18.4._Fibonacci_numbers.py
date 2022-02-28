import time

def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


t0 = time.time()
n = 40
result = fib(n)
t1 = time.time()

print(f'fib({n}) = {result}, ({t1-t0:.2f} secs.)')
