#################
### function
### type()
#################

# print the type of an object

message = 'Hello there !'

print(type(message)) # <class 'str'>
print(type('This is a string')) # <class 'str'>
print(type("And so is this.")) # <class 'str'>
print(type("""and this.""")) # <class 'str'>
print(type('''and even this...''')) # <class 'str'>

num1 = '17'
num2 = '3.2'
print(type(num1)) # <class 'str'>
print(type(int(num1))) # <class 'int'>
print(type('17')) # <class 'str'>
print(type(num2)) # <class 'str'> 
print(type(float('3.2'))) # <class 'float'>

num3 = 17
num4 = 3.2
print(type(num3)) # <class 'int'>
print(type(17)) # <class 'int'>
print(type(num4)) # <class 'float'>
print(type(3.2)) # <class 'float'>

class Test():
    pass

print(type(Test)) # <class 'type'>
print(type(Test())) # <class '__main__.Test'>












