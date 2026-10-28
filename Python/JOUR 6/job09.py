# Trouver la valeur maximale et minimale des éléments de la liste.
L = [8, 24, 27, 48, 2, 16, 102, 7, 84, 91]
maximum = L[0]
minimum = L[0]
for nombre in L:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre
print("Maximum:",maximum)
print("Minimum:",minimum)