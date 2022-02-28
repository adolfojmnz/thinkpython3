def num_digits(n):
    count = 0
    while n != 0:
          count = count + 1
          n = n // 10
    return count


def num_digits_v2(n):
    count = 0
    while n >= 0:
        count = count + 1
        n = n // 10
        if n == 0:
            break
    return count


def num_digits_v3(n):
    count = 0
    while True:
          digit = n % 10
          if digit == 0 or digit == 5:
             count += 1
          n = n // 10
          if n == 0:
             break
    return count


print(num_digits_v2(0))