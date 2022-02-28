def how_many_odds(xs):
    count = 0
    for n in xs:
          if n % 2 == 1:
             count += 1
    print(count)


xs  = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15]
how_many_odds(xs)

