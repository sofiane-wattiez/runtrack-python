nombreEntier = int(input("Veuillez entrer un nombre entier :"))
nombrePuissance = int(input("Veuillez entre la puissance par laquelle vous souhaitez calculer votre nombre entier :"))
# n = nombreEntier
def Puissance(x,n):
    if n==0 :
        return 1
    else :
        return x*Puissance(x,n-1)
print("Voici la Puissance de votre nombre :", Puissance(nombrePuissance,nombreEntier))