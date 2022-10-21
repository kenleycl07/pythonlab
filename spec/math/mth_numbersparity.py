########
### math
### numbers and parity
######################

# example
numbers = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("So, we've got {} even numbers and {} odd numbers.".format(even_count, odd_count))


# example
numbers = [10, 21, 4, 45, 66, 93, 11]
even_count, odd_count = 0, 0
num = 0

while num < len(numbers):
    if numbers[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    num += 1

print("So, we've got {} even numbers and {} odd numbers.".format(even_count, odd_count))

# example
numbers =  [10, 21, 4, 45, 66, 93, 11]

odd_count = len(list(filter(lambda x: (x % 2 != 0), numbers)))
even_count = len(list(filter(lambda x: (x % 2 == 0), numbers)))

print("So, we've got {} even numbers and {} odd numbers.".format(even_count, odd_count))

# example
numbers = [10, 21, 4, 45, 66, 93, 11]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

even_count = len(even_numbers)
odd_count = len(odd_numbers)

print("So, we've got {} even numbers and {} odd numbers.".format(even_count, odd_count))

# example
numbers = [10, 21, 4, 45, 66, 93, 11]

even_numbers = [num for num in numbers if num % 2 == 0]

even_count = len(even_numbers)
odd_count = len(numbers) - even_count

print("So, we've got {} even numbers and {} odd numbers.".format(even_count, odd_count))

# example
even_numbers = [2, 4, 6, 8, 10, 12]
odd_numbers = [1, 3, 5, 7, 9, 11]
natural_numbers = even_numbers + odd_numbers

print("Even numbers: ", even_numbers)
print("Odd numbers:", odd_numbers)
print("Natural numbers:", natural_numbers)

# add 1 to every natural number
for n in range(len(natural_numbers)):
    natural_numbers[n] = natural_numbers[n] + 1
    
print("New natural numbers:", natural_numbers)

# example
for num in range(2, 10):
    if num % 2 == 0:
        print(num, 'is an even number.')
        continue
    print(num, 'is an odd number.')

# example
even_numbers = []
odd_numbers = []

for num in range(2, 10):
    if num % 2 == 0:
        even_numbers.append(num)
        continue
    odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
