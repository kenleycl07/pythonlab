#################
### class
### Point
#################

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __cmp__(self, other):
        return cmp((self.y, self.x), (other.y, other.x))
            
# create points A and B
A = Point(2, 3)
B = Point(5, 3)
# display coordinates
print('A =', A)
print('B =', B)
# add two points
print('A + B =', A + B)
# substract two points
print('A - B =', A - B)
# negation
print(-A)
print(-B)

# create points P and Q
P = Point(1, 1)
Q = Point(1, 5)  
# add the two points
R = P + Q
# display points
print('P =', P)
print('Q =', Q)
print('R = P + Q')
print(f"R = ({R.x}, {R.y})")