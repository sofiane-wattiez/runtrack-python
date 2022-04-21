nombreEntier = int(input("Veuillez entrer un numéro :"))

def factorielle(n):
    if n == 0:
        return 1
    else:
        return  n  * factorielle(n-1)
print(factorielle(nombreEntier))