# Afficher les nombres premiers jusqu'a 1000.
for nombre in range(2, 1001):
    premier = True 
    for diviseur in range(2, nombre):
        if nombre % diviseur == 0:
            premier = False
            break
    print(nombre)

# Transformer en fonction
def nombre_premier():
    for nombre in range(2, 1001):
        premier = True
        for diviseur in range(2, nombre):
            if nombre % diviseur == 0:
                premier = False
                break
        print(nombre)    
nombre_premier()
