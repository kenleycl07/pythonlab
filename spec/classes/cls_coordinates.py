#################
### class
### Coordinates
#################

class Coordinates:

    def __init__(self, x=5, y=2, z=7):
        self.x = x
        self.y = y
        self.z = z

    def moveright(self):
        self.x += 1
        
    def __str__(self):
        return '(x, y, z) = ({}, {}, {})'.format(self.x, self.y, self.z)

# Create a point of coordinates x, y, and z
c1 = Coordinates(2, 4, 3)
print(c1)
# Move the point to the right
c1.moveright()
print(c1)