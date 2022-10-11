#################
### using dictionaries
### part2
#################

# create a dictionary 
order = { 'first':'1', 'second':'2', 'third ':'3','fourth':'4', 'fifth':'5'}
print(order)

# create a copy of the dictionary
order1 = order
print(order1)
print(order)

# modify the value of third in order1
# copy gets changed. Original gets changed also
order1['third'] = '30'
print(order1)
print(order)

# create a copy of a dictionary using copy() method
order2 = order.copy()
print(order2)

# modify the value of fourth in order2
# copy gets changed
# original remains the same
order2['fourth'] = '40'
print(order2)
print(order)


# create a copy of a dictionary using dict() function
order3 = dict(order)
print(order3)

# modify the value of fifth in order3
# copy gets changed
# original remains the same
order3['fifth'] = '50'
print(order3)
print(order)
   
# merge two dictionaries using update() method
# this overrides the existing items
order1 = {'a':'once', 'b':'twice', 'c':'three times'}
order2 = dict(a='first', b='second', c='third', d='fourth')
print(order1)
print(order2)

order1.update(order2)
print(order1)













