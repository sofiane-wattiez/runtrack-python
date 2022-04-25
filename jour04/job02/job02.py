nombreEntier = int(input('Entrez un nombre entier pour renseignez la taille des mots que vous recherché : '))

with open('data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        for word in line:
            if len(word) == nombreEntier:
                print(word)
            for word in line:
                if word.count(' ') == nombreEntier:
                    print(word)