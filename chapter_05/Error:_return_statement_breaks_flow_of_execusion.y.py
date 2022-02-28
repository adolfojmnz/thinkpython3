def sprt_x(x=0):
    if x<=0:
        while x<=0:
            x = int(input('Enter a positiv value\n'))
    return f'The square of {x} is {x**0.5:.4f}'

print(sprt_x())
