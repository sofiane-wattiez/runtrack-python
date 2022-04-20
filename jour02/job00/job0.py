# import configparser

class Personne:
    # Construct
    def __init__(self, nom , prenom):
        self.nom=nom
        self.prenom=prenom
    # def __del__(self): 
    #     print("je suis le destructeur")
    def SePresenter(nom, prenom):
        print("Bonjour, je m'appelle {} {}".format(nom, prenom))
        p=Personne(nom='Wattiez', prenom='Sofiane') # Instanciation
        # p1=Personne('nom', 'prenom') # Instanciation
        print('fin de création')
        return p
if __name__ == '__main__':
    print(Personne.SePresenter())
# p=SePresenter() # Appel de la fonction
    p1=Personne.SePresenter() # Appel de la fonction
    print(Personne.SePresenter(p1))