def num_even_digits(n):
    evens = 0
    odds = 0
    l = len(str(n))
    for i in range(l):
        if n % 2 == 0:
            evens += 1
        else:
            odds +=1
        n = n // 10
    print('There is {0} even digits in your number'.format(evens))
    print('There is {0} odds digits in your number'.format(odds))

num_even_digits(1234567890)
