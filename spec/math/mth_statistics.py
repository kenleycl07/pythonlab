########
### math
### statistics
##############

###############################
# Median and Standard Deviation
###############################

# example
# Sans utiliser le module statistics
sommeDesDonnees = 0 # Accumulateur pour la somme des données.
nombreDeDonnees = 0 # Compteur pour le nombre de données.
sommeCarreEcart = 0 # Somme des carrés des écarts.

# Liste de données.
MaListe = [2, 3, 45, 56, 76, 89, 32, 12, 35, 55, 66, 78, 3, 4, 5, 76, 12, 32, 33]

# Accumuler les données, incrémenter le nombre de données.
for donnee in MaListe:
   sommeDesDonnees += donnee
   nombreDeDonnees += 1
# Calculer la moyenne.
moyenne = sommeDesDonnees / nombreDeDonnees

# Fonction pour calculer la racine carrée de la variance.
def racineCarree(laVariance):
    for racine in range(0, int(abs(laVariance)) + 1):
        if racine**2 >= abs(laVariance):
            return racine
      
# Parcourir la liste de données.
for donnee in MaListe:
    # Calculer la somme des carrés des écarts.
    sommeCarreEcart += ((donnee - moyenne)**2)
    # Calculer la médiane.
    MaListe.sort() # Ordonner les données.      
    milieu = len(MaListe) // 2 # Trouver le milieu de la liste
    mediane = int((MaListe[milieu] + MaListe[~milieu]) / 2) # Trouver la médiane                      
    
    # Calculer la moyenne des carrés des écarts ou variance.
    variance = int(sommeCarreEcart / len(MaListe))
    # Calculer la racine carrée de la variance ou écart type.
    ecartType = racineCarree(variance)
    
    
# example
# En utilisant le module statistics
import statistics as stat

# Calculer la moyenne, la médiane et l'écart type.
mean = stat.mean(MaListe)
median = stat.median(MaListe)
standardDeviation = int(stat.pstdev(MaListe, mean))

""" Sortie """
print('Partie 1 - Sans utiliser le module statistics')
print('---------------------------------------------')
print('Moyenne =', moyenne)
print('Médiane =', mediane)
print('Ecart type =', ecartType)

print() # Retour à la ligne.

print('Partie 2 - En utilisant le module statistics:')
print('---------------------------------------------')
print('Moyenne =', mean)
print('Médiane =', median)
print('Ecart type =', standardDeviation)
