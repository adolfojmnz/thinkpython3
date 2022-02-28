from copy import copy, deepcopy
from pointClass import Point
from rectangleClass import Rectangle

def same_coordinate(p, q):
    return (p.x == q.x) and (p.y == q.y)

def compareObjects(obj1, obj2):
    out1 = f'{obj1 == obj2} for {obj1} == {obj2}'
    out2 = f'{obj1 is obj2} for {obj1} is {obj2}'
    return f'{out1} \n{out2}'

# deep copy vs shallow copy
p = Point(3, 4)
q = Point(3, 4) 
r = copy(p)
s = deepcopy(q)
a = Rectangle(Point(5, 7), 100, 200)
b = copy(a)
c = deepcopy(a)

print(compareObjects(p, q))
print(compareObjects(p, r))
print(compareObjects(q, s))
print(compareObjects(a, b))

print(a.printObjectAddress())
print(b.printObjectAddress())
print(c.printObjectAddress())
