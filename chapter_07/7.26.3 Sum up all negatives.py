def sum_up_negatives(xs):
    sum_up = 0
    for i in xs:
        if i < 0:
           sum_up += i
    print(sum_up)
xs = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
sum_up_negatives(xs)

