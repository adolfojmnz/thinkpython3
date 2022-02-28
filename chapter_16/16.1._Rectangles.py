from pointClass import Point
from rectangleClass import Rectangle

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print(f'Box: {box}')
print(f'Bomb: {bomb}')

box.grow(45, -30)
box.move(30, -15)
bomb.grow(55, -35)
bomb.move(-20, 20)

print(f'Box: {box}')
print(f'Bomb: {bomb}')
