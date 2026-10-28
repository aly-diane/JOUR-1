# Gérer un inventaire 
# Information initiale du produit (Creation des variables)
nom= "clavier"
prix_unitaire= 25.0
quantite_stock= 10
# Afficher les informations
print("produit:", nom)
print("prix_unitaire:",prix_unitaire, "euro")
print("quantite en stock:", quantite_stock)
# Ajouter des produits au stock
ajout_stock= 5
quantite_stock = quantite_stock + ajout_stock

quantite_achat = int(input("Combien de produits souhaitez-vous acheter ? "))