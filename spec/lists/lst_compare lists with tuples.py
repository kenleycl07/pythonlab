#################
### lists
### compare list with tuples
#################

# compare iterables

# compare a list and a tuple in term of capacity
# the list is larger in capacity
# we should  use tuple instead of list when dealing with huge amount of data
# it takes more time to create a list than to create a tuple
import sys
import timeit

somelist = [0, 1, 2, "hello", True, 0.6, 0.08]
sometuple = (0, 1, 2, "hello", True, 0.6, 0.08)

print('capacity of the list', sys.getsizeof(somelist), 'bytes')
print('capacity of the tuple', sys.getsizeof(sometuple), 'bytes')
print()
print('time required to create a list', 
      timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000), 'mseconds')
print('time required to create a tuple', 
      timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000), 'mseconds')

