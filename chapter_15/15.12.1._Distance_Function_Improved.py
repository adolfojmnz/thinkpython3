from pointClass import Point

def distanceImproved(p, q):
    mx = (p.x - q.x) ** 2
    my = (p.y - q.y) ** 2
    return f'{((mx + my) ** 0.5):.2f} units.'

p = Point(3, 4)
q = Point(6, 7)

print(distanceImproved(p, q))
