# import configparser

class Personne:
    # Construct
    def __init__(self, nom , prenom):
        self.nom=nom
        self.prenom=prenom  # attributs
    print()
    def __str__(self):
        print("Bonjour, je m'appelle {} {}".format(self.nom, self.prenom))
    # def __repr__(self):
    #     return "Bonjour, je m'appelle {} {}".format(self.nom, self.prenom)
    # def __del__(self): 
    #     print("je suis le destructeur")
    def SePresenter(nom, prenom):
        nom = 'test'
        prenom = 'test'
        print("Bonjour, je m'appelle {} {}".format(nom, prenom))
        p=Personne(nom='Wattiez', prenom='Sofiane') # Instanciation
        # p1=Personne('nom', 'prenom') # Instanciation
        print('fin de création')
        return p
if __name__ == '__main__':
    print("Bonjour, je m'appelle {} {}".format("Sofiane", "Wattiez"))
    # p=Personne.SePresenter() # Appel de la fonction
    # p1=Personne.SePresenter() # Appel de la 
print()