#################
### lists
### loops, conditions and iteration
#################

# Créer des listes

chiffres = [x for x in range(50)]
carres = [x**2 for x in chiffres]
mots = ['La', 'maison', 'est', 'belle', 'et', 'je', "l'aime", 'beaucoup.', 'Mais', 
        'elle', "n'est", 'pas', 'la', 'mienne', "c'est", 'la', 'maison', "d'un", 'ami', 
        'qui', 'me', 'laisse', "l'utiliser", 'papa', 'maman']

print(chiffres)
print(carres)
print(mots)

# Affichage des éléments des listes

for c in chiffres:
    print(c)
for m in mots:
    print(m)

for m in mots:
    print(str(len(m)) + ' '*8 + m)

for c in chiffres:
    if c % 2 == 0:
        print(c)

# utilisation de list comprehension 
# création d'une liste de cubes 
cubes = [c**3 for c in chiffres]

# Ecrire les mots d'une liste dans un fichier
fichier = open('monfichier.txt', 'w')
for m in mots:
    fichier.write(m + '\n')
fichier.close()

# Ecrire les mots longs dans un fichier
fichier = open('motslongs.txt', 'w')
for m in mots:
    if len(m) > 4:
        fichier.write(m + '\n')
fichier.close()

# Ecrire les mots purs dans un fichier
fichier = open('motspurs.txt', 'w')
for m in mots:
    mp = m.rstrip(',.!?:;')
    fichier.write(mp + '\n')
fichier.close()

# Ecrire les mots purs dans un fichier
fichier = open('motspurs.txt', 'w')
mots_purs = [m.rstrip(',.;!?:') for m in mots]
for mp in mots_purs:
    fichier.write(mp + '\n')
fichier.close()

# Ecrire les mots purs dans un fichier
fichier = open('motspurs.txt', 'w')
for m in mots:
    mp = m.rstrip(',.!?:;')
    fichier.write(mp + '\n')
fichier.close()

# Parité
def estPair(c):
    if c % 2 == 0:
        return True
    else:
        return False

# utilisation de la fonction filter()
pairs = filter(estPair, chiffres)
for c in pairs:
    print(c)

# list comprehension
double = [m*2 for m in mots]

# Créer un dictionnaire à partir de deux listes
# utilisant la méthode zip()
dico = {}
for key, value in zip(chiffres, mots):
        dico[key] = value
print(dico)

# read lines of a file containing a maze
fichier = open('maze.txt', 'r')
contenue = fichier.read().split()
maze2 = [ligne.replace('#', '0').replace('_', '1') for ligne in contenue]
fichier.close()

# create list of repeated objects

# create a list of 12 repeated zeros
n = 12
zeros = [0]*n
print('list of zeros:', zeros)

# create a list of 12 ones
n = 12
ones = [1]*n
print('list of ones:', ones)

# create a nested list using list comprehension
repeated = [[n for n in range(6)] for m in range(2)]
print(repeated)

# create a nested list using list comprehension
# including operations
repeated = [[n + 1 for n in range(3)] for m in range(4)]
print(repeated)

repeated = [[n + m for n in range(3)] for m in range(4)]
print(repeated)

repeated = [[n - m for n in range(3)] for m in range(4)]
print(repeated)

# sums, average, and lists

# compute the sum of a sequence of numbers and do the average
total = 0.0
count = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    total += number
    count += 1

average = total / count
print(total)
print(average)


# Write a Python program to sum all the items in a list.
# Hints: Create a function sum_list() that takes one
# parameter called 'items'. Your function Should return
# the sum of all the numbers in the list. 
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_list(numbers))

# list and Condition

# this program checks if there is any value in a list that
# is greater than five. If a number is greater than five, the 
# program breaks.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater = False
for number in numbers:
    if number > 5:
        greater = True
        print('the program breaks at', number)
        break


