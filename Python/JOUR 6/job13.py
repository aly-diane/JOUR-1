# Supprimer les doublons de la liste sans utiliser les fonctions système (len,sort,round...)
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
sans_doublons = []
for nombre in L:
    if nombre not in sans_doublons:
        sans_doublons.append(nombre)

print(sans_doublons)