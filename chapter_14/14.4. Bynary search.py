def search_binary(xs, target):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
            return -1
        
        mid_index = (lb + ub) // 2
        item_at_mid = xs[mid_index]

        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else: 
            ub = mid_index
    

xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
print(search_binary(xs, 20) == -1)
print(search_binary(xs, 99) == -1)
print(search_binary(xs, 1) == -1)
print(search_binary(xs, 7) == 3)

for (i, v) in enumerate(xs):
    print(search_binary(xs, v) == i)
    