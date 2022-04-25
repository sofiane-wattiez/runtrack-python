
nombreEntier = int(input('Entrez un nombre entier pour renseignez la taille des mots que vous recherché : '))

with open('data.txt', 'r') as f:
   index = 0
while index < len(nombreEntier):
    lettre = nombreEntier[index]
    print(lettre)
    index = index + 1