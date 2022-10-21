########
### math
### pattern
###########

# rectangle
# display 20 stars 5 times
for i in range(5):
    # display 20 stars
    for j in range(20):
        print('*', end='')
    print()

# rectangle
def rectangle(width, length):
    # display length stars width times
    for i in range(width):
        # display length stars
        for j in range(length):
            print('*', end='')
        print()

rectangle(5, 20)

# Backtracks
# print 6 stars 8 times
for i in range(8):
    for j in range(6):
        print('*', end='')
    print()

# print ((6 + 1) - 1) stars ((8 + 1) -1) times
for i in range((8 + 1) - 1):
    for j in range((6 + 1) - 1):
        print('*', end='')
    print()

# triangle
# in the triangle pattern, we keep track of the number 
# of stars on each line and we use incrementation
# We print h number of stars n times
# The number of stars increases line by line

def triangle1():
    s = 1
    for i in range(8):
        for j in range(s):
            print('*', end= '')
        s = s + 2
        print()

def triangle2():
    s = 1
    for i in range(8):
        for j in range(s):
            print('*', end='')
        s = s + 4
        print()

triangle1()
triangle2()


# center aligned triangle with an odd number of stars
def centerAligned1(n):
    for s in range(n):
        print('a' * (6-s-1) + '*' * (2*s+1))
        
# center aligned triangle with an odd number of stars
def centerAligned2(n):
    for s in range(n):
        print(' ' * (6-s-1) + '*' * (2*s+1))

# center aligned triangle with an even number of stars
def centerAligned3(n):
    for s in range(n):
        if s == 0:
            print('a' * (6-s-1) + '*' * (2*s+1))
        else:
            print('a' * (6-s-1) + '*' * (2*s))

# left aligned triangle with an odd number of stars
def leftAligned1(n):
    for s in range(n):
        print('' * (6-s-1) + '*' * (2*s+1))

# left aligned triangle with an even number of stars
def leftAligned2(n):
    for s in range(6):
        if s == 0:
            print('' * (6-s-1) + '*'*(2*s+1))
        else:
            print('' * (6-s-1) + '*'*(2*s))
            
centerAligned1(6)   
centerAligned2(6)          
centerAligned3(6)   
leftAligned1(6) 
leftAligned2(6)  

# Backround
# Logic behind centerAligned1()
print('a' * (6-0-1) + '*' * (2*0+1)) 
print('a' * (6-1-1) + '*' * (2*1+1)) 
print('a' * (6-2-1) + '*' * (2*2+1)) 
print('a' * (6-3-1) + '*' * (2*3+1)) 
print('a' * (6-4-1) + '*' * (2*4+1)) 
print('a' * (6-5-1) + '*' * (2*5+1)) 

# Logic behind centerAligned2()
print(' ' * (6-0-1) + '*' * (2*0+1))
print(' ' * (6-1-1) + '*' * (2*1+1))
print(' ' * (6-2-1) + '*' * (2*2+1))
print(' ' * (6-3-1) + '*' * (2*3+1))
print(' ' * (6-4-1) + '*' * (2*4+1))
print(' ' * (6-5-1) + '*' * (2*5+1))

# Logic behind centerAligned3()
print('a' * (6-0-1) + '*' * (2*0+1)) 
print('a' * (6-1-1) + '*' * (2*1)) 
print('a' * (6-2-1) + '*' * (2*2)) 
print('a' * (6-3-1) + '*' * (2*3)) 
print('a' * (6-4-1) + '*' * (2*4)) 
print('a' * (6-5-1) + '*' * (2*5)) 

# Logic behind leftAligned1()
print('' * (6-0-1) + '*' * (2*0+1))
print('' * (6-1-1) + '*' * (2*1+1))
print('' * (6-2-1) + '*' * (2*2+1))
print('' * (6-3-1) + '*' * (2*3+1))
print('' * (6-4-1) + '*' * (2*4+1))
print('' * (6-5-1) + '*' * (2*5+1))

# Logic behind leftAligned2()
print('' * (6-0-1) + '*' * (2*0+1))
print('' * (6-1-1) + '*' * (2*1))
print('' * (6-2-1) + '*' * (2*2))
print('' * (6-3-1) + '*' * (2*3))
print('' * (6-4-1) + '*' * (2*4))
print('' * (6-5-1) + '*' * (2*5))

# left aligned triangle using while loop
s = 0
while s < 11:
    print('*' * s, end='')
    s = s + 1
    print()


# reversed left aligned triangle using while loop
i = 10
while i > 0:
    print('*' * i, end=' ')
    i = i - 1
    print()

# right aligned triangle using for loop
s = 0
n = 10
while n >= 0:
    print(' ' * n + '*' * s)
    s = s + 1
    n = n - 1

# putting a letter instead of a space
s = 0
n = 10
while n >= 0:
    print('a' * n + '*' * s)
    s = s + 1
    n = n - 1

#     *
#     ***
#     *****
#     *******
#     *********
#     ***********
#     *************

def triangle1():
     h = 1
     for i in range(1, 7 + 1):
        for j in range(1, h + 1):
            print("*", end="")
        h = h + 2
        print()

#     *
#     ** ** *
#     ** ** ** ** *
#     ** ** ** ** ** ** *
#     ** ** ** ** ** ** ** ** *
#     ** ** ** ** ** ** ** ** ** ** *
#     ** ** ** ** ** ** ** ** ** ** ** ** *

def triangle2(self):
    h = 1
    for i in range(1, 7 + 1):
        for j in range(1, h + 1):
            print("*", end="")
        h = h + 4;
        print()










