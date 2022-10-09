#################
### using lists
### part1
#################

# create an empty list

# using list function
a_list = list()
print("An empty list", a_list)

# using brackets
another_list = []
print("Another empty list", another_list)

# create nested lists

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
letters_and_numbers = [letters, numbers]

print("Letters:", letters)
print("Numbers:", numbers)
print("Letters and Numbers:", letters_and_numbers)

# display letters and numbers
print("Letters:", letters_and_numbers[0]) 
print("Letters:", letters_and_numbers[1]) 

# display the first and the second letter
print("First letter:", letters_and_numbers[0][0]) 
print("Second letter:", letters_and_numbers[0][1]) 

# display the first and the second number
print("First number:", letters_and_numbers[1][0]) 
print("Second number:", letters_and_numbers[1][1]) 

# display letters and numbers using zip() function
for letter, number in zip(letters, numbers):
    print(letter, "-", number)

  
# concatenate lists

squares = [1, 4, 9, 16, 25]
other_squares = [36, 49, 64, 81, 100]
all_squares = squares + other_squares

print("squares:", squares)
print("other squares:", other_squares)
print("all squares:", all_squares)


# modify lists

cubes = [1, 8, 27, 65, 125]
print("cubes:", cubes)

# 4 to the power of 3 is 64, but not 65
# replace 65 by 64
cubes[3] = 4**3
print("replace 65 by 64:", cubes)

# add cubes at the end of the list

cubes.append(6**3) 
print("add the cube of 6 to the end of the list:", cubes)
cubes.append(7**3) 
print("add the cube of 7 to the end of the list:", cubes)

# create a list of integers
integers = [30, 120, 96, 49, 54] 
print("integers:", integers)

# using insert method
integers.insert(4, 36) 
print("insert 36 at index 4:", integers)

# add another list to the list of integers
integers.extend([78, 12, 80, 23, 44]) 
print("extend the list of integers:", integers)

# count integers
print("There are", len(integers), "integers in the list.") 

# count integers occurences in the list
print("12 occurs", integers.count(12), "time(s)")
print("44 occurs", integers.count(44), "time(s)")
print("80 occurs", integers.count(80), "time(s)")

# displaying integers

for integer in integers:
    print(integer)

for integer in integers:
    print(integer, end=' ')

for index in range(len(integers)):
    print(integers[index], end=' ')

for index, integer in enumerate(integers):
    print(index, "-", integer)

# using sort() method
integers.sort() 
print(integers)

# remove an integer (last by default)
integers.pop() 
print(integers)

# remove the first integer
integers.pop(0) 
print(integers)

# remove the fourth integer
integers.pop(3)
print(integers)

# using remove() method
integers.remove(78)
print(integers)

# using reverse() method
integers.reverse()
print(integers)

# using clear() method
integers.clear()
print(integers)

# using del keyword
# display list after deletion throws a NameError
del integers
print(integers)

# create copy of lists

# Method 1
# create a list of fruits (assignation)
fruits = ['Banana', 'Cherry', 'Apple']

# copy the list of fruits using assignation
theFruits = fruits
print("Original list of fruits:", fruits)
print("Copy of the list of fruits:", theFruits)

# add 'Lemon' to the copy
print("Add 'Lemon' to the copy:")
theFruits.append('Lemon')
print("The copy gets changed:", theFruits) 
print("The original gets changed also:", fruits)

# Method 2
# create a list of fruits
fruits = ['Banana', 'Cherry', 'Apple']

# # copy the list of fruits using list() function
theFruits = list(fruits)
print("Original list of fruits:", fruits)
print("Copy of the list of fruits:", theFruits)

# add 'Orange' to the copy
print("Add 'Orange' to the copy:")
theFruits.append('Orange')
print("The copy gets changed:", theFruits)
print("The original remains the same:", fruits)

# Method 3
# create a list of fruits
fruits = ['Banana', 'Cherry', 'Apple']

# copy the list of fruits using copy() method
theFruits = fruits.copy()
print("Original list of fruits:", fruits)
print("Copy of the list of fruits:", theFruits)

# add 'Papaya' to the copy 
theFruits.append('Papaya')
print("The copy gets changed:", theFruits)
print("The original remains the same:", fruits)

# Method 4
# create a list of fruits
fruits = ['Banana', 'Cherry', 'Apple']

# copy the list of fruits using slicing
theFruits = fruits[:]
print("Original list of fruits:", fruits)
print("Copy of the list of fruits:", theFruits)

# add 'Guava' to the copy 
theFruits.append("Guava")
print("The copy gets changed:", theFruits)
print("The original remains the same:", fruits)



