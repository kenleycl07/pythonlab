########
### math
### number sign
###############

# example
integer = int(input("Please enter an integer: "))
if integer < 0:
    integer = 0
    print("Negative changed to zero.")
elif integer == 0:
    print("Zero.")
elif integer == 1:
    print("Single.")
else:
    print("More than zero or one...")

print("Integer:", integer)