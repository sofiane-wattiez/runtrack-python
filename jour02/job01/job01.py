class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return "La personne {} {}".format(self.nom, self.prenom)
    def __repr__(self):
        return "Personne({}, {})".format(self.nom, self.prenom)
print("{} {}".format(Personne.nom, Personne.prenom))
class Auteur(Personne):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return "L'auteur {} {}".format(self.nom, self.prenom)
    def __repr__(self):
        return "Auteur({}, {})".format(self.nom, self.prenom)
print("L'auteur {} {}".format(Auteur.nom, Auteur.prenom))
        
class Livre(Auteur):
    def __init__(self, titre, auteur, nbpages):
        self.titre = titre
        self.auteur = auteur
        self.nbpages = nbpages
    def __str__(self):
        return "Le livre {} de {} a {} pages".format(self.titre, self.auteur, self.nbpages)
    def ecrireUnLivre(titre , auteur , nbpages):
        return "Le livre {} de {} a {} pages".format(titre, auteur, nbpages)
# def __repr__(self):
    #     return "Livre({}, {}, {})".format(self.titre, self.auteur, self.nbpages)
print("Le livre {} de {} a {} pages".format(Livre.titre, Livre.auteur, Livre.nbpages))
