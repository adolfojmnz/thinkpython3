def swap(x, y):      # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    # This fuction isn't fruitfull. The statement "return x, y" needs to be add so the function can return
    # the swap values of x and y.
    print("after swap statement: x:", x, "y:", y)


a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
