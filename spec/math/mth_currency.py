########
### math
### currency
############

# currency change
def change():
    for i in range(1, 15+1):
        amount_euros = 1 * (2**(i-1))
    for j in range(1, 15+1):
        amount_dollars = 1.65 * (2**(j-1))
          
        print('|' + str(amount_euros) + ' euros = ' + str(amount_dollars) + " dollars |")
        print('___________________________')
        print()

change()
