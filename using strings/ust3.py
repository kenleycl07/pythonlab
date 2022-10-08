#################
### using strings
### part3
#################

# using old formatting style for a string
fcountry = "Italy"
preference = "My favorite country is %s" %fcountry
print(preference)

# using old formating style for an integer
pnumber = 7
perfection = "The number for representing perfection is %d" % pnumber
print(perfection)

# using old formating style for a decimal
pi = 3.14
pvalue = "pi is evaluated to %f" %pi
print(pvalue)

# the value of pi
pi = 3.14
pi_value = "The value of pi is %.2f" %pi
print(pi_value)

# a decimal value
dvalue = 7.659043
evaluate = "The decimal value is %.4f" % dvalue
print(evaluate)

# a decimal value
dvalue = 7.659043
evaluate = "The decimal value is {}".format(dvalue)
print(evaluate)

# introducing yourself
age = 22
text = "My name is Kenley and I am {} years old."
introduction = text.format(age)
print(introduction)

# introducing yourself
name, age = 'Kenley', 22
text = "My name is {} and I am {} years old."
introduction = text.format(name, age)
print(introduction)

# placing an order
quantity, itemno, price = 3, 567, 49.95
need = "I want {} pieces of item {} for {} dollars."
order = need.format(quantity, itemno, price)
print(order)

# placing an order
quantity, itemno, price = 3, 567, 49.95
need = 'I want to pay {2} dollars for {0} pieces of item {1}'
order = need.format(quantity, itemno, price)
print(order)

# a decimal value
dvalue = 7.6590437389
evaluation = "The decimal value is {:.4f}".format(dvalue)
print(evaluation)

# a decimal value
dvalue = 7.659043
ivalue = 7
evaluation = "The decimal value is {:.4f} and the integer value is {}".format(dvalue, ivalue)
print(evaluation)

# recommended formatting style

# history
firstname = "Isaac"
lastname = "Newton"
statement = f"{firstname} {lastname} was a great physician"
print(statement)

# decimal value
dvalue = 7.659043
ivalue = 7
evaluation = f"The decimal value is {dvalue} and the integer value is {ivalue}"
print(evaluation)

# multiples
dvalue = 7.659043
ivalue = 7
multiplication1 = f"three times {dvalue} is {dvalue * 3} and three times {ivalue} is {ivalue * 3}"
multiplication2 = f"four times {dvalue} is {dvalue * 4} and two times {ivalue} is {ivalue * 2}"
print(multiplication1)
print(multiplication2)

# convert a string to a list
somestring = "use the split function to change the list"
somelist = somestring.split()
print(somelist)

# convert a list back to a string
somelist = ['use', 'the', 'join', 'function', 'to', 'change', 'the', 'string']
somestring = ' '.join(somelist)
print(somestring)

# create list of repeated letters
letter = "a"
thelist = [letter] * 10
print(thelist)

# reverse a string using slicing
art = "Ontario"
revart = art[::-1]
print(revart)







