#################
### using strings
### part2
#################

# combine strings

# put several strings within parentheses to have them join together
text = ('I like mathematics' 'and computational thinking.')
print(text)

# repetition and concatenation
such_string = 3 * 'Pa' + 'ta'
print(such_string)

# concatenation and slicing
text = 'Python is a high level programming language.'
print(text[:21] + text[21:])
print(text[:31] + text[31:])

# remove whitespaces from the right and from the left
message = "    Hello there     "
message = message.strip()
print(message)

# remove whitespaces from the right 
message = "    Hello there     "
message = message.rstrip()
print(message)

# remove whitespaces from the left
message = "    Hello there     "
message = message.lstrip()
print(message)

# remove all whitespaces
town = "Port - au - Prince"
town = town.replace(" ", "")
print(town)

# capitalize every first letter
town = "new york city"
town = town.title()
print(town)

# change lowercase to uppercase
message = "hello there Ken !"
message = message.upper()
print(message)

# change uppercase to lowercase
message = "HELLO THERE KEN !"
message = message.lower()
print(message)

# return the index of the first character in a substring
message = "Bang Bang Lucky Luc !"
print(message.find("Luc"))
print(message.find("Luc !"))

# count character occurences
magic = "abracadabra"
print(magic.count("b"))

# replace a substring by another substring
message = "Hello there Ken !"
message = message.replace("Ken", "Kenley")
print(message)
