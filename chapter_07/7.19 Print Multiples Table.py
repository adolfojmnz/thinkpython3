def print_multiples(n, height):
    for i in range(1, height + 1):
        print(i * n, '\t', end='   ')
    print()


def print_mult_table(heigh):
    for i in range(1, heigh + 1):
        print_multiples(i, heigh)

print_mult_table(12)
