xs = list("Crunchy Frog")
xs = "".join(xs)

def find(n):
    for i in range(106, n):
        if (i % 21 == 0):
            return i

n = 10000000000
print(find(n))

range(10)           # range(0, 10)
list(range(10))     # [0, ..., 10]
