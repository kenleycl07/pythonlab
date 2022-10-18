class Etudiant:
	def __init__(self, nom, prenom, age, adresse):
		self.nom = nom
		self.prenom = prenom
		self.age = age
		self.adresse = adresse

	def __str__(self):
		return '{} {}'.format(self.prenom, self.nom)
