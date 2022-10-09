#################
### using strings
### part1
#################

# Create one line and multiline string
greeting = "I like programming in Python."
print(greeting)

greeting = 'I like programming in Python.'
print(greeting)

message = """Hello guys !
What is your favorite programming language?"""
print(message)

message = """Hello guys !
        My favorite programming language is Python.
        However, I like programming in C# too."""
print(message)


# create a multiline string
# remove new line characters
message = """Hello guys ! \
This will create a one line \
string."""
print(message)


# quotes, double quotes and 
# special character
sentence = "I'm a computer scientist."
print(sentence)

sentence = 'I\'m a computer scientist.'
print(sentence)

negative_sentence = "It doesn't matter."
print(negative_sentence)

negative_sentence = 'It doesn\'t matter.'
print(negative_sentence)

positive_answer = "\"Yes\", they answered."
print(positive_answer)

positive_answer = '"Yes", they answered.'
print(positive_answer)

negative_answer = "It isn't worth it, they specified."
print(negative_answer)

negative_answer = 'It isn\'t worth it, they specified.'
print(negative_answer)

exclamative = '''"Oh no", he exclaimed, "Ken's program has crashed !"'''
print(exclamative)

# indexing
print('Einstein'[0]) # E
print('Einstein'[1]) # i
print('Einstein'[4]) # t

hobbie = 'music'
print(hobbie[0]) # m
print(hobbie[1]) # u
print(hobbie[-1]) # c
print(hobbie[len(hobbie) - 1]) # c
print(hobbie[-2]) # i

artist = 'Picasso'
print(artist[:]) # Picasso
print(artist[::1]) # Picasso
print(artist[::2]) # Pcso
print(artist[::3]) # Pao
print(artist[0:3]) # Pic
print(artist[1:5]) # icas
print(artist[0:len(artist)]) # Picasso

greeting = 'Hello'
color = 'Y' + greeting[1:5] + 'w'
print(color)

message = 'Hello, world !'
theMessage = message[:6] + ' there !'
print(theMessage)

# create a string and print all letters in that string
hobbie = 'drawing'
for letter in hobbie:
    print(letter)

hobbie = 'drawing'
for letter in hobbie:
    print(letter, end="-")

# create strings and combine them to create new strings
greeting = "Hello"
name = "Mike"
print(greeting + " " + name)

# add a space between strings
greeting = "Hello"
name = "Mike"
print(greeting + " " + name)

# concatenation without using operator
favorite_language = 'Py' 'thon'
print(favorite_language)


