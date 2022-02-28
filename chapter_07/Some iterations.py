def odds_btw_1_and_100():
    for i in range(1, 100, 2):
        print(i, "\t", i / 2)

def calculator():
    total = 0
    while True:
          r = input("Num")
          if r == "":
             break
          total += int(r)
    print(total)

def avoid_odd_numbers():
    for i in range(100):
        if i % 2 == 1:
           continue
        print(i)
    print('Done')


