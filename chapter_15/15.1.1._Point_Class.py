class Point:
    """ Point class represents and manipulates x,y coordinates."""

    def __init__(self, x=0, y=0): # For the instantiation
        """ Create a new point at the origin."""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Computes the distance from the origin to the given point. """
        return ((self.x**2)+(self.y**2))**0.5

    def __str__(self):
        """ Return the point cordinates as a string. """
        return f'({self.x}, {self.y})'

    def halfway(self, target):
        """ Return the halfway point between itself and a target point."""
        mx = (p.x + q.x)/2
        my = (p.y + q.y)/2
        return Point(mx, my) 

        
p = Point(3, 4)
q = Point(6, 7)

pdist = p.distance_from_origin()
qdist = q.distance_from_origin()

print(p.halfway(q))
