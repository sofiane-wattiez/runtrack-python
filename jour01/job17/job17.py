def extract(L):
    pair = []
    impaire =  []
    for x in L:
        if x % 2 == 0:
            pair.append(x)
        else:
            impaire.append(x)
    print("La liste des nombres pairs est : ", pair)
    print("La liste des nombres impairs est : ", impaire)

# Tester l'algo
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(extract(L))