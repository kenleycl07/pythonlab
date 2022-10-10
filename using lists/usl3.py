#################
### using lists
### part3
#################

# create a list of squares

# create a list of squares from (1**2) to (100**2)
# Method 1
squares = []
for number in range(1, 10 + 1):
    square = number**2
    squares.append(square)
print(squares)

# create a list of squares from (1**2) to (10**2)
# Method 2
square = []
for number in range(1, 10 + 1):
    square = [number**2]
    squares += square
print(squares)

# create a list of squares from (1**2) to (100**2)
# List comprehension
squares = [number**2 for number in range(1, 100 + 1)]
print(squares)

# create a list of cubes

# create a list of cubes from (1**3) to (10**3)
# Method 1
cubes = []
for number in range(1, 10 + 1):
    cube = number**3
    cubes.append(cube)
print(cubes)

# create a list of cubes from (1**3) to (10**3)
# Method 2
cubes = []
for number in range(1, 10 + 1):
    cube = [number**3]
    cubes += cube
print(cubes)

# create a list of squares from (1**2) to (100**2)
# List comprehension
cubes = [number**3 for number in range(1, 100 + 1)]
print(cubes)

# create a list of squares using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number**2 for number in numbers]
print(squares)

# create a list of cubes using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = [number**3 for number in numbers]
print(cubes)
