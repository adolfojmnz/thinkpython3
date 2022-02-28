def swap(x, y):
    (x, y) = (y, x)
    return x, y

(a, b) = ["This", "is", "fun"], [2, 3, 4]

print(swap(a, b) == (b, a))
