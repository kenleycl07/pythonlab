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

# create list of repeated objects

# create a list of 12 repeated zeros
n = 12
zeros = [0]*n
print('list of zeros:', zeros)

# create a list of 12 ones
n = 12
ones = [1]*n
print('list of ones:', ones)

# create a nested list using list comprehension
repeated = [[n for n in range(6)] for m in range(2)]
print(repeated)

# create a nested list using list comprehension
# including operations
repeated = [[n + 1 for n in range(3)] for m in range(4)]
print(repeated)

repeated = [[n + m for n in range(3)] for m in range(4)]
print(repeated)

repeated = [[n - m for n in range(3)] for m in range(4)]
print(repeated)

# sums, average, and lists

# compute the sum of a sequence of numbers and do the average
total = 0.0
count = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    total += number
    count += 1

average = total / count
print(total)
print(average)

# Write a Python program to sum all the items in a list.
# Hints: Create a function sum_list() that takes one
# parameter called 'items'. Your function Should return
# the sum of all the numbers in the list. 
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_list(numbers))

"""conditions and lists"""

# this program checks if there is any value in a list that
# is greater than five. If a number is greater than five, the 
# program breaks.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater = False
for number in numbers:
    if number > 5:
        greater = True
        print('the program breaks at', number)
        break

