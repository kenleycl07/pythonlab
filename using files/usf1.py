###############
### using files
### part1
#########

# program sample
# Create the file 'name.txt'. Append your name and your favorite
# programming language to the end of in the file. Write each information on one line.
name = 'Kenley'
favLanguage = 'Python'
f = open('name.txt', 'a')
f.write(name + '\n' + favLanguage + '\n')
f.close()
# Read the file after the appending and print the content of the file on the console.
f = open('name.txt', 'r')
content = f.read()
print(content)

# Overwrite the content of the file by writing your name and your favorite color.
# Write each information on one line.
name = 'Kenley Clermont'
favColor = 'Black'
f = open('name.txt', 'w')
f.write(name + '\n' + favColor + '\n')
f.close()

# program sample
# Create a file 'palindrome.txt'. Append a list of palindrome sequences to the end of the file.
# Write each information on one line.
# Open file in append mode.
f = open('palindrome.txt', 'a')
# Create a list of palindromes.
palindromes = ['civic', 'deed', 'deified', 'deked']
# Write palindromes into the file.
for pal in palindromes:
    f.write(pal + '\n')
f.close()
# Open the file containing the palindromes and print the content of the file in the console.
f = open('palindrome.txt', 'r')
content = f.read()
print(content)

# program sample
# Open a file from a different location.
# Create a new empty file to Desktop.
f = open("C:\\Users\hp\Desktop\\towns.txt", 'w')
f.close()
# Open a file from a different location.
f = open("C:\\Users\hp\Desktop\\towns.txt", "r")
# Read the five first characters of the file.
someletters = f.read(5)
print(someletters)

# program sample
# Open a file 'squares.txt' to write squares from
# 0^2 to 9^2. Write each square evaluation omn one line.
with open('squares.txt', 'w') as f:
    for num in range(10):
        f.write(f"{num}^2 = {num**2}\n")
# Open the file 'squares.txt' to read the squares from the file
# and print them to the console.
with open('squares.txt', 'r') as f:
    content = f.read().splitlines()
    print(content)
# Open the file 'squares.txt' to read the squares from the file
# and print them to the console. Use list comprehension.
content = [line.strip() for line in open('squares.txt', 'r')]
print(content)


# program sample
# Create a function getInformation() to get these information from the user
# firstname, lastname, and age. This function will store the information
# into a list. Open a file 'data.txt', and append the information to the 
# end of the file. Use commas to separate information about one person.
# Create a function readInformation() that will read the content of the 
# file and print it to the console.

# gets information from user
def getInformation():
    
    # get user input
    firstname = input('Enter firstname: ')
    lastname = input('Enter lastname: ')
    age = int(input('Enter age: '))
    
    # store the information into a list
    information = [firstname, lastname, age]
    
    # append information to the end of the file
    datafile = 'data.txt'
    f = open(datafile, 'a')
    
    f.write(firstname + ', ' + lastname + ', ' + str(age) + '\n')
    f.close()

# prints out the information to the console
def readInformation():
    
    datafile = 'data.txt'
    f = open(datafile, 'r')
    
    # read file content
    content = f.read()
    print(content)
    f.close()
    
getInformation()
readInformation()

# program sample
# Create a list of 30 words. Open a file 'randomwords.txt' to write the words of 
# the list. Select a random word in the list. Open the file to append the chosen word 
# followed by the number of characters it contains to the end of the file. Print a number 
# of hyphens corresponding to the number of characters in the chosen word. Repeat the process
# of picking a number a certain number of time.

# Create a list of 30 words
words = ['coin', 'side', 
         'world', 'capital', 
         'moon', 'light',
         'chance', 'random', 
         'average', 'Bottom', 
         'Top', 'Wisdom', 
         'King', 'Blessing', 
         'Sword', 'Promise', 
         'event', 'time', 
         'circle', 'existence', 
         'value', 'change', 
         'flip', 'life', 
         'curse', 'surplus', 
         'math','computation', 
         'logic', 'scale']

# Write words in the file.
f = open('randomwords.txt', 'w')
for word in words:
    f.write(word + '\n')
f.write('\n'*2)
f.close()

# Pick a random word.
import random as rd

# Append the word to the end of the file.
f = open( 'randomwords.txt', 'a')
random_word = rd.choice(words)
nhyphens = len(random_word)

f.write(f"The selected word is {random_word} and it has {len(random_word)} characters\n")
# Display the number of hyphens according to the number of letters.
print('-' * nhyphens)
f.close()

# program sample
# Create a function called write_in_file(). Open a file called myfile.txt.
# Create a list called Words and write the words of the list in the file.
# Each word should be written on one line of the file.
# Create a function called read_from_file(). Open the file and 
# read the words which will be put in a list called result.
# return the list result.

def write_in_file(words):
    # open file
    f = open("myfile.txt", "w")
    # write each word on one line of the file
    for word in words:
        f.write(word + "\n")
    # close file
    f.close()

def read_from_file():
    # open file
    f = open("myfile.txt", "r")
    # assign file content to result
    result = f.read().split()

    return result
