class Point:
    """ Point class represents and manipulates x,y coordinates."""

    def __init__(self, x=0, y=0): # For the instantiation
        """ Create a new point at the origin."""
        self.x = x
        self.y = y

    def __str__(self):
        """ Return the point cordinates as a string. """
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        """ Returns a new point resulting from the addition of the two points. """
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """ Returns the dot product between the two gievn points. """
        return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        """ Returns the scalar product between the point and the integer. """
        return Point(other * self.x, other * self.y)

    def reverse(self):
        self.x, self.y = self.y, self.x

    def distance_from_origin(self):
        """ Computes the distance from the origin to the given point. """
        return ((self.x**2)+(self.y**2))**0.5

    def halfway(self, target):
        """ Return the halfway point between itself and a target point."""
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my) 

    def reflect_x(self):
        """ Mirrors the point to the oposive side of y coord. """
        self.y = -(self.y)

    def slope(self, target):
        """ Returns the slope of the line traced throughout the given points. """
        dx = self.x - target.x
        dy = self.y - target.y
        if dx == 0:
            return f'The straight line has no slope. Its equation is x = x1.' 
        return dy/dx 

    def slope_to_origin(self):
        """ Returns the slope of the line "point and the origin". """
        return (self.y / self.x)

    def straight_line_eq(self, target):
        """ Returns the "x" and "b" coefitiens of the straight line equation. """ 
        m = (self.slope(target))
        if type(m) == str:
            return m
        m = int(m)
        b = int(-m * self.x + self.y)
        return (m, b)
