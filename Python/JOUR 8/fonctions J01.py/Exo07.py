#Transformer en fonction les variables
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




def gerer_stock():
    nom = "clavier"
    prix_unitaire = 25.0
    quantite_stock = 10

    print("Produit :", nom)
    print("Prix unitaire :", prix_unitaire, "euros")
    print("Quantité en stock :", quantite_stock)

    ajout_stock = 5
    quantite_stock = quantite_stock + ajout_stock

    print("Stock après ajout :", quantite_stock)

    quantite_achat = int(
        input("Combien de produits souhaitez-vous acheter ? ")
    )

    if quantite_achat <= quantite_stock:
        quantite_stock = quantite_stock - quantite_achat
        print("Achat effectué.")
        print("Stock restant :", quantite_stock)
    else:
        print("Stock insuffisant.")

gerer_stock()



def gerer_stock():
    nom = "clavier"
    prix_unitaire = 25.0
    quantite_stock = 10

    return("Produit :", nom)
    return("Prix unitaire :", prix_unitaire, "euros")
    return("Quantité en stock :", quantite_stock)

    ajout_stock = 5
    quantite_stock = quantite_stock + ajout_stock

    return("Stock après ajout :", quantite_stock)

    quantite_achat = int(
        input("Combien de produits souhaitez-vous acheter ? ")
    )

    if quantite_achat <= quantite_stock:
        quantite_stock = quantite_stock - quantite_achat
        return("Achat effectué.")
        return("Stock restant :", quantite_stock)
    else:
        return("Stock insuffisant.")

gerer_stock()