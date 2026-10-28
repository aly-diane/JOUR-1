# Calcul du produit des valeurs de la liste d'un intervalle.
#multiplier toutes les valeurs comprises entre 25 et 90, bornes incluses.
L = [8, 24, 27, 48, 2, 16, 102, 7, 84, 91]
produit = 1
for nombre in L:
    if 25 <= nombre <= 90:
        produit *= nombre
print("produit:", produit)