# Afficher la table de multiplication de 1 à N.
n= int(input("Entrez un nombre entier"))
for i in range (11):
    print(f"{n}x{i}={n*i}")
else:
    
    print("Erreur: le nombre doit être supérieur à zéro")

# Transformer en fonction
def table_multiplication():
    n= int(input("Entrez un nombre entier"))
    for i in range (11):
        print(f"{n}x{i}={n*i}")
    else:
    
        print("Erreur: le nombre doit être supérieur à zéro")
table_multiplication()