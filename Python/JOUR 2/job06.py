# Afficher les résultats de la multiplication de N par 7
N = int(input("Saisissez un entier N : "))

i = 1

while i <= 10:
    resultat = N * 7 * i
    print(N, "x 7 x", i, "=", resultat)
    i = i + 1