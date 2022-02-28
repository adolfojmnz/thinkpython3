from RectangleClass import Rectangle

r = Rectangle(Point(0, 0), 10, 5)
print(r.contains(Point(3, 4.99999)))
print(r.contains(Point(3, 3)))
print(r.contains(Point(9, 1)))
print(not r.contains(Point(3, 7)))
print(not r.contains(Point(3, 5)))
print(not r.contains(Point(-3, -3)))

