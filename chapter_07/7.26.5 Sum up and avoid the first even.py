def sum_up_evens(xs):
    sum_up = 0
    avoid = 0

    for i in xs:
        if i % 2 == 0:
           avoid += 1
           if avoid > 1:
              sum_up += i
    print(sum_up)

xs = [1, 3, 5, 7, 9, 1]
sum_up_evens(xs)

