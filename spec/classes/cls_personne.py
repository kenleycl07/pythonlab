def entree():
    class Personne:
        def __init__(self, nom, prenom, age, numero_tel):
            self.nom = nom
            self.prenom = prenom
            self.age = age
            self.numero_tel = numero_tel

    Personnes = list()
    for i in range(2):
        nom_utilisateur = input("Entre votre nom: ")
        prenom_utilisateur = input("Entre votre prenom: ")
        age_utilisateur = int(input("Entre votre age: "))
        tel_utilisateur = input("Entre votre téléphone: ")
        p1 = Personne(nom_utilisateur, prenom_utilisateur, age_utilisateur, tel_utilisateur)
        Personnes.append(p1)
    return Personnes


def sortie():
    valeur = entree()
    for i in range(len(valeur)):
        donnee = f"{valeur[i].nom} {valeur[i].prenom} {valeur[i].age} {valeur[i].numero_tel}"
        f = open("personnes.txt", 'a', encoding="utf-8")
        f.write(donnee + "\n")
        f.close()


if __name__ == "__main__":
    sortie()
