from etudiant import Etudiant
import sqlite3
connection = sqlite3.connect("personnes.db")
cursor = connection.cursor()

liste_etudiants = list()

##
# Accepter une chaine de caractère entre 1 à 50 caractères
# @return str
def getChaineDeCaractere():
	longueur_chaines = [i + 1 for i in range(50)]
    la_chaine = input("Entrer une chaine de caractère entre 1 à 50 caractères: ")
    
    while len(la_chaine) not in longueur_chaines:
    	if len(la_chaine) in longueur_chaines:
    		return la_chaine
    	else:
    		la_chaine = input("Entrer une chaine de caractère entre 1 à 50 caractères: ")
    return la_chaine
        

##
# Accepter un entier de 0 à 150
# @return str
def getEntier():
	entier = int(input("Entrer un entier de 0 à 150: "))

	while entier < 0 or entier > 150:
		if entier < 0:
			entier = int(input("Entrer un entier de 0 à 150"))
		elif entier > 150:
			entier = int(input("Entrer un entier de 0 à 150"))
		else:
			break
	return entier

##
# Remplissage de la liste avec les infos démographiques
#
def capturer_demographie():
	# accepter les attributs de personne comme input
	nom = getChaineDeCaractere()
	prenom = getChaineDeCaractere()
	age = getEntier()
	adresse = getChaineDeCaractere()

	personne = Etudiant(nom, prenom, age, adresse)
    
    liste_etudiants.append(personne)


# Imprimer une liste de personnes contenant dans la liste liste_etudiants
# Si ordre = True, la liste doit être par ordre alphabétique
#
def imprimer_liste(ordre=False):
	# Remplacer la ligne suivante par des codes collectant les infos
	la_liste_etudiants = list()
	for i in liste_etudiants:
		infos = f"{i.nom} {i.prenom} {i.age} {i.adresse}"
        la_liste_etudiants.append(infos)

     if ordre:
     	print(sorted(la_liste_etudiants))
     else:
     	print(la_liste_etudiants)

# Accepter un Nom et imprimer toutes les personnes possédant ce nom
#
def chercher_etudiant():
	# Remplacer la ligne suivante par des codes collectant les infos
    # print('Info trouvée ou non. Si trouvée alors imprimée ...\n')
    le_nom = input("Entrez le nom: ")
    la_liste_etudiants = list()

    for et in liste_etudiants:
    	if et.nom == le_nom:
    		infos = f"{et.nom} {et.prenom} {et.age} {et.adresse}"
    		la_liste_etudiants.append(infos)
    
    if len(la_liste_etudiants) > 0:
    	print("Info trouvée")
    	for et in la_liste_etudiants:
    		print(et)
    else:
    	print("Info non trouvée")

def sauvegarde_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS personnes_data (nom TEXT, "
                   "prenom TEXT, age INTEGER, adresse TEXT)")
    for et in liste_etudiants:
        data = (et.nom, et.prenom, et.age, et.adresse)
        cursor.execute("INSERT INTO personnes_data VALUES(?,?,?,?)", data)
        connection.commit()

def sauvegarde_fichier():
    f = open("personnes.txt", "w")

    for et in liste_etudiants:
        data = f"{et.nom} {et.prenom} {et.age} {et.adresse}"
        f.write(data + "\n")

    f.close()

def dispatch(choix):
    if choix == 1:
        capturer_demographie()
    elif choix == 2:
        imprimer_liste()
    elif choix == 3:
        imprimer_liste(True)
    elif choix == 4:
        chercher_etudiant()
    elif choix == 5:
        sauvegarde_fichier()
    elif choix == 6:
        sauvegarde_db()

def menu():
    choix = 0
    while choix not in [1 - 4]:
        print("1. Ajouter un dossier d’étudiant.")
        print("2. Imprimer la liste des étudiants.")
        print("3. Imprimer la liste des étudiants par Ordre Alphabétique.")
        print("4. Chercher un étudiant par Nom de Famille.")
        print("5. Sauvegarder dans Fichier.")
        print("6. Sauvegarder dans Base de Données.")
        print("7. Terminer\n")
        choix = int(input("Choix: "))
        if choix in [1, 2, 3, 4, 5, 6]:
            dispatch(int(choix))
        elif choix == 7:
            break
        else:
            print('Mauvais Choix ... \n')


if __name__ == "__main__":
    menu()





