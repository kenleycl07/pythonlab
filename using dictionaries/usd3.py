#################
### using dictionaries
### part3
#################

# combine dictionaries with other objects

# use a tuple as key for the dictionary
asum = (7, 3)
thesum = {asum:15}
print(asum)
print(thesum)

# create a dictionary of dictionaries
# create a french-to-english translation dictionary
french_to_english = {
        'Chien':'Dog',
        'Chat':'Cat',
        'Souris':'Mouse',
        'Oiseau':'Bird'
}
# create an english-to-french translation dictionary
english_to_french = {
        'Dog':'Chien',
        'Cat':'Chat',
        'Mouse':'Souris',
        'Bird':'Oiseau'
}
# create a translation dictionary using both laguages dictionaries
translation = {
         'translator1':french_to_english,
         'translator2':english_to_french
}

print(french_to_english)
print(english_to_french)
print(translation)

# dict comprehension
numbers = [0, 1, 2, 3, 4, 5]
words = ['zero', 'one', 'two', 'three', 'four', 'five']

# create a dictionary using enumerate() function
order = {key:value for key, value in enumerate(words)}
print(order)

# create a dictionary using zip() function
order = {number:word for number, word in zip(numbers, words)}
print(order)

# dict comprehension       
square_pairs = {str(key):key**2 for key in range(0, 20)}
print(square_pairs)


