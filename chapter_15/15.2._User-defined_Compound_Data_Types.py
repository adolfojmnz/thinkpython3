class Point:
    """ Point class represents and manipulates x,y coordinates. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y. """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """ Compute the distance from the origin. """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(3, 4)
q = Point(5, 12)

pdist = p.distance_from_origin()
qdist = q.distance_from_origin()
print('\n', pdist, '\n', qdist)