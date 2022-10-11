#################
### using dictionaries
### part1
#################

# create a dictionary

order = { 'first':'1', 'second':'2', 'third ':'3','fourth':'4', 'fifth':'5'}
print(order)

# using dict() function
order = dict(first = '1', second = '2', third = '3', fourth = '4', fifth = '5')
print(order)

# display values of keys first and second
print(order['first'])
print(order['second'])

# trying to access the value of a key that does not exist
# print(order['tenth']) # KeyError: 'tenth'
# print(order.get('tenth')) # None

# specify a default value for a key that does not exist
print(order.get('tenth', 'Not Found'))

# add a new entry to the dictionary
order['sixth'] = '60'
print(order)

# update multiple value using update method
order.update({'first':'1', 'second':'2', 'sixth':'6'})
print(order)

# delete a specific key and it's value using del keyword
del order['fifth']
print(order)

# delete a specific key and it's value using pop() method
n = order.pop('first')
print(n)
print(order)

# remove the last item using popitem() function
p = order.popitem()
print(p)
print(order)

# see how many keys there are in the dictionary
print(len(order))

# display keys using keys() method
print(order.keys())

# display values using values() method
print(order.values())

# display keys and values using items() method
print(order.items())

print(type(order.keys()))
print(type(order.values()))
print(type(order.items()))

# loop through the keys
for key in order:
    print(key)

# loop through keys and values
for key, value in order.items():
    print(key, value)




















