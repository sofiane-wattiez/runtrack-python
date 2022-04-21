nombreEntier = int(input("Veuillez entrer un nombre entier :"))

def Puissance(n):
    if n == 0:
        return 1
    else:
        return  n  * Puissance(n-1)
print("Voici le résultat de votre nombre", Puissance(nombreEntier))