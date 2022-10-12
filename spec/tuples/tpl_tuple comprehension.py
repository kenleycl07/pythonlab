# create a tuple using tuple comprehension
sometuple = (i**2 for i in range(10))
print(sometuple) # <generator object <genexpr> at 0x00000289DE187970>

sometuple = tuple((i**2 for i in range(10)))
print(sometuple) 

