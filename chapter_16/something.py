from rectangleClass import Rectangle
from pointClass import Point

q = Rectangle(Point(-6, -2), 10, 10)
p = Rectangle(Point(10, 10), 10, 5)

def reduction(p1, p2):
    count = 0
    r = Point(0, 0)
    rang = (p1.corner.x, p2.corner.x)

    if (p1.corner.x == p2.corner.x):
        return True

    for i in range(p1.corner.x, p2.corner.x-1, -1):
        print(i)
        r.x = i
        if p1.contains(r):
            return f'{p1} contains the point {r}'

print(reduction(p, q))
