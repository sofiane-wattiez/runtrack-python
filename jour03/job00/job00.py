nombreEntier = int(input("Veuillez entrer un nombre entier :"))

def factorielle(n):
    if n == 0:
        return 1
    else:
        return  n  * factorielle(n-1)
print("Voici le résultat factorielle de votre nombre entier ", factorielle(nombreEntier))