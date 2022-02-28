def print_triangular(n):
    x = 0
    for i in range(1, n+1):
           print(i, '\t', i + x)
           x = x + i

print_triangular(5)

