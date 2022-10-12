#################
### function
### range()
#################

print(range(10)) # range(0, 10)
print(sum(range(4))) # 6
print(list(range(4))) # [0, 1, 2, 3]

# range(stop)

# increasing, start 1 (default), step 1 (default)
# i goes from 0 to 20
for n in range(21):
    print(n, end=' ')

# increasing, start 1 (default), step 1 (default)
# i goes from 0 to 20
for n in range(20 + 1):
    print(n, end=' ')

# increasing, start 1 (default), step 1 (default)
# i goes from 0 to 4
for i in range(5):
    print(i)

# increasing, start 1 (default), step 1 (default)
# i goes from 0 to 4
for i in range(5):
    print(i, end=" ")

# range(start, stop)

# increasing, step 1 (default)
# i goes from 0 to 20
for n in range(0, 21):
    print(n, end=' ')

# increasing, step 1 (default)
# i goes from 1 to 20
for n in range(1, 21):
    print(n, end=' ')

# increasing, step 1 (default)
# i goes from 5 to 9
for i in range(5, 10):
    print(i, end=" ")

# increasing, step 1 (default)
# i goes from -10 to -6
for i in range(-10, -5):
    print(i, end=" ")

# range(start, stop, step)

# increasing, step 1
# i goes from 1 to 20
for n in range(1, 21, 1):
    print(n, end=' ')

# increasing, step 1
# i goes from 1 to 20
for n in range(1, 20 + 1, 1):
    print(n, end=' ')

# increasing, step 2
# i goes from 1 to 19
for n in range(1, 21, 2):
    print(n, end=' ')

# increasing, step 2
# i goes from 2 to 8
for i in range(0, 10, 2):
    print(i, end=" ")

# increasing, step 3
# i goes from 0 to 9
for i in range(0, 10, 3):
    print(i, end=" ")

# increasing, step 2
# i goes from -100 to -12
for i in range(-100, -10, 2):
    print(i, end=" ")

# decreasing, step -30
# i goes from -10 to -70
for i in range(-10, -100, -30):
    print(i, end=" ")

# decreasing, step -2
# i goes from -10 to -98
for i in range(-10, -100, -2):
    print(i, end=" ")

# decreasing, step -2
# i goes from 2 to 8
for i in range(10, 1, -2):
    print(i, end=" ")

    


