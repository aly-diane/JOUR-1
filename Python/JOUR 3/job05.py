# Afficher les nombres premiers jusqu'a 1000.
for nombre in range(2, 1001):
    premier = True 
    for diviseur in range(2, nombre):
        if nombre % diviseur == 0:
            premier = False
            break
If premier:
    print(nombre)