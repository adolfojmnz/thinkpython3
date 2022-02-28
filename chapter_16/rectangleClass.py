from pointClass import Point

class Rectangle:
    """ Creates rectangle objects. """

    def __init__(self, posn, w, h):
        """ Instantiate and default rectangle object. """
        self.origin = posn
        self.width  = w
        self.height = h

    def __str__(self):
        """ Returns the objects contents. """
        return f'({self.origin}, {self.width}, {self.height})'

    def printObjectAddress(self):
        """ Returns the embedded object references. """
        return f'({self.origin, self.width, self.height})'

    def grow(self, dw, dh):
        """ Grow or Shrink the object by the deltas. """
        self.width += dw
        self.height += dh 

    def move(self, dx, dy):
       """ Move this object by the deltas. """       
       self.origin.x += dx
       self.origin.y += dy

    def area(self):
        """ Return the object's area. """
        return f'{self.width * self.height}'
    
    def perimeter(self):
        """ Return the perimeter's longitud. """
        return f'{self.width * 2 + self.height * 2}'

    def flip(self):
        """ Swaps the values between rectangle's width and height. """
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, p):
        x = (self.width - self.origin.x) + (p.x - self.width) # 
        x = (x >= self.origin.x) and (x < self.width) 
        y = (self.height - self.origin.y) + (p.y - self.height)
        y = (y >= self.origin.y) and (y < self.height)
        return x and y

    def secondCorner(self):
        """ Return the intersection point coords between width and height. """
        coord_x = self.origin.x + self.width
        coord_y = self.origin.y + self.height
        return Point(coord_x, coord_y)
        
    def halfcoord(self):
        """ Returns the halfway point of a given segment. """
        origin2 = self.secondCorner()
        x_coord = (self.origin.x + corner.x)/2
        y_coord = (self.origin.y + corner.y)/2 
        return Point(x_coord, y_coord)

    def doCollide(self, rect):
        """ Return True if the two objects collide. """
        pass

rect = Rectangle(Point(0,0), 60, 60)
print(rect.contains(Point(3,4)))
