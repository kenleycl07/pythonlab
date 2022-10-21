########
### math
### noperations
###############

# example
# compute the sum of integers from 1 to n.
# n is obtained from the user
# sum = n(n+1)/2
# Output: stored in variable result

# obtenir n de l'utilisateur
n = int(input("Enter the value for n: "))
# compute the sum
_sum = (n * (n + 1)) // 2
# Display sum
print(_sum)


# example
# Un magasin vend des sacs de riz pesant 52 kilogrammes et des sacs 
# de sucre pesant 75 kilogrammes. Demandez à l'utilisateur le nombre 
# de sacs de riz (variable riz) et le nombre de sacs de sucre 
# (sucre comme variable) Calculer le poids total et Output sur l'ecran.

# poids d'un sac de riz et d'un sac de sucre
poids_riz = 52
poids_sucre = 75
# demander le nombre de sacs de riz à l'utilisateur
riz = int(input('Entrer le nombre de sacs de riz: '))
sucre = int(input('Entrer le nombre de sacs de sucre: '))
# calculer le poids total
poids_total = riz*poids_riz + sucre*poids_sucre
# Afficher le poids total
print(poids_total)


# example
# Demandez à l'utilisateur d'entrer 2 nombres entiers a et b
# Calculez et affichez sur l'écran:
# a) La somme a + b
# b) Le produit a x b
# c) La différence a - b

# demander à l'utilisateur d'entrer 2 nombres entiers a et b
a = int(input('Entrer un entier a: ')) 
b = int(input('Entrer un entier b: '))
# calculer et afficher la somme a + b
somme = a + b
print(somme)
# calculer et afficher le produit a x b
produit = a * b
print(produit)
# calculer et afficher la différence a - b
difference = a - b
print(difference)
