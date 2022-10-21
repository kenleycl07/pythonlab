###############
### using lists
### part2
#########

# indexing and slicing

# create a list of fruits
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(fruits[-4:-1]) # ['orange', 'kiwi', 'melon']

# create a list of fruits and change the second item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits) # ["apple", "blackcurrant", "cherry"]

# change a range of item values
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits [1:3] = ["blackcurrant", "watermelon"]
print(fruits) # ["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]

# substitute one value by multiple values
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["blackcurrant", "watermelon"]
print(fruits) # ["apple", "blackcurrant", "watermelon", "cherry"]

# substitute multiple values by one value
fruits = ["apple", "banana", "cherry"]
fruits[1:3] = ["watermelon"]
print(fruits) # ["apple", "watermelon"]

# insert a value into the list using insert() method
fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "watermelon")
print(fruits)

# add a fruit to the list using append() method
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) # ["apple", "banana", "cherry", "orange"]

# add another iterable object to a list

# add a list to another list using extend() function
fruits = ["apple", "banana", "cherry"]
more_fruits = ["mango", "pineapple", "papaya"]
fruits.extend(more_fruits)
print(fruits) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# add a list to another list using append() method
fruits = ["apple", "banana", "cherry"]
more_fruits = ["mango", "pineapple", "papaya"]
for fruit in more_fruits:
    fruits.append(fruit)
print(fruits) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# add a tuple to a list
fruits = ["apple", "banana", "cherry"]
more_fruits = ("kiwi", "orange")
fruits.extend(more_fruits)
print(fruits)

# sort a list

# sort a list alphabetically
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# sort a list numerically
numbers = [100, 50, 65, 82, 23]
numbers.sort()
print(numbers) # [23, 50, 65, 82, 100]

# sort a list alphabetically descending
letters = ["a", "c", "b", "d", "f", "e"]
letters.sort(reverse=True)
print(letters) # ['f', 'e', 'd', 'c', 'b', 'a']

# sort a list numerically descending
numbers = [2, 6, 7, 9, 1, 10, 3, 2]
numbers.sort(reverse=True)
print(numbers) # [10, 9, 7, 6, 3, 2, 2, 1]

# sort a list using a keyword argument
# customize your own function by using the keyword argument key = function
# the function will return a number that will be used to sort the list
# (the lowest number first) 
# sort the list based on how close the number is to 50
# distance of the number from 50 is given by |n - 50|
def close_enough(n):
    distance = abs(n - 50)
    return distance

numbers = [100, 50, 65, 82, 23]
numbers.sort(key=close_enough)
print(numbers)

# case sensitive sorting vs case-insensitive sorting
# case sensitive sorting can give an unexpected result
# by default, the sort method is case sensitive, resulting in all
# capital letters being sorted before lowercase letters
letters = ['a', 'B', 'c', 'd', 'E', 'f', 'g']
letters.sort()
print(letters)

# you can use built-in functions as key functions when sorting a list
# if you want a case-insensitive sort function, use str.lower
# as a key function then perform a case-insensitive sort of the list
letters = ['a', 'f', 'c', 'd', 'B', 'E', 'g']
letters.sort(key=str.lower)
print(letters)

# reverse the order of a list using reverse() method
letters = ["a", "c", "b", "d", "f", "e"]
letters.reverse()
print(letters)
