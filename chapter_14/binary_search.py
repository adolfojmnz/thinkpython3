def search_binary(xs, target):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
            return -1

        mid_index = (lb + ub) // 2
        item_at_mid = xs[mid_index]

        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
               .format(lb, ub, ub-lb, item_at_mid, target))

        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index

