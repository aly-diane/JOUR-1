# Somme des valeurs paires de la liste L.
# Un nombre est pair lorsque le reste de sa division par 2 vaut 0.
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme=0
for nombre in L:
    if nombre % 2 ==0:
        somme+= nombre
print("somme des nombres pairs:",somme)