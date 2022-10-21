########
### math
### multiplication
##################

# example
# dynamic multiplication table of 'number'
# table goes from 0 to n
def multiplication_table(n, number):
    for i in range(0, n+1):
        nth_term = number * i
        print("{} x {} = {}".format(number, i, nth_term))
    
multiplication_table(10, 3)

# example
# dynamic multiplication table
def multiplication_table(base, start, end, inc):
    for i in range(start, end + 1, inc):
        nth_term = base * i
        print("{} x {} = {}".format(base, i, nth_term))

multiplication_table(3, 0, 10, 1)

# example
# dynamic multiplication table
def multiplication_table(base, start, end, inc):
    while start <= end:
        print("{} x {} = {}".format(base, start, base*start))
        start += inc

multiplication_table(3, 0, 10, 1)

# example
# dynamic multiplication table
def table(base, start, end, inc):
    while start <= end:
        result = base * start
        print("{} x {} = {}".format(base, start, result))
        start += inc

multiplication_table(3, 0, 10, 1)

# example
# dynamic multiplication table
def table(base, start, end, inc):
    while start <= end:
        print(base, "x", start, "=", base * start)
        start = start + inc

# example
# multiplication table of 7
def multiplication_table_of_7(number):
    for i in range(1, n + 1):
        nth_term = number * i
        print(nth_term)
    print()

# example
# sequence of 12 numbers. Start with the number n. Each term is equal to three times
# the term preceding it.   
def tripple(n):
    for i in range(n, 16 + 1):
        nth_term = n * (3 ** (i - 1))
        print(nth_term)

tripple(1)
tripple(2)
