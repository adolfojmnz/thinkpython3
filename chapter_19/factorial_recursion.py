def fact(n):
    if n == 0:
        return 1
    return n * (n-1)


n = 9
result = 1

for i in range(n):
    print(n, result)
    result *= fact(n)
    n = n-1
print(result)
