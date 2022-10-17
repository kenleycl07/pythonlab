###############
### using files
### part2
#########

# program sample
# Using sys argument
import sys

# print(sys.argv[1])
if len(sys.argv) < 3:
    sys.exit("Missing required files.")
# read file
def read_file(file):
    data = open(file, 'r', encoding="utf-8")
    names = data.read().split(",")
    print(names)

read_file("gnames.txt")
read_file("bnames.txt")

# using textwrap
import textwrap

file = open("somefile.txt", 'r')
f = file.read()
# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)
word_list = wrapper.wrap(text=value)
# Print each line.
for element in word_list:
    print(element)

