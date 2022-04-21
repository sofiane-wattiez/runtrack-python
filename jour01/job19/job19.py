L = int(input('Veuillez saisir le nombre de ligne : '))
C = int(input('Veuillez saisir le nombre de colonnes : '))

for i in range(1, L+1):
    for j in range(1, C+1):
        if i == 1 or i == L:
            print("-", end='')
        elif  j == 1 or j == C:
            print("", end='|')
        else:
            print("", end=' ')
    print()
