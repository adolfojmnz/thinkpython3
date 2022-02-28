import time

def seq_3n_plus_1(n): # 7.5. The Collatz 3n + 1 sequence (Collatz'z Conjecture)
    while n != 1:
          if n % 2 == 0:
             n = int(n / 2)
          else:
               n = n * 3 + 1
          if n > 1:
                print(n, end=", ")
          else:
               print(n, end=".\n")
          time.sleep(0.5)


def sequence_V2(n): # My "3n + 1" improved. It works with 1.
    print("3n + 1 conjecture. n =", n, end="\n")
    while True:
          if n % 2 == 0:
             n = int(n / 2)
          else:
               n = n * 3 + 1
          if n > 1:
             print(n, end=", ")
          elif n <= 1:
               print(n, end=".\n")
               break
          time.sleep(0.5)


sequence_V2(3)