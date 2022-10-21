########
### math
### powers
##########

# cube of and argument
import math

def cube(nombre):
    theCube = nombre**3
    return theCube
# using cube
def volumeSphere(rayon):
    volume = (4/3) * math.pi * cube(rayon)
    return volume