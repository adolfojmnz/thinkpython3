from pointClass import Point

p = Point(4, 6)
q = Point(3, 7)

print_list = [
        p.halfway(q),
        p.reflect_x(),
        p.slope(q),
        p.slope_to_origin(),
        p.straight_line_eq(q),]

for instruction in print_list:
    print(instruction)
