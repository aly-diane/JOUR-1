# Simulation financière d'un investissement
# Investissement initial (Création des variables)
capital = 10000.0
taux = 5.0
# Calcul du gain annuel initial
gain = capital * taux / 100
print("===Ivestissement initial===")
print("Capital:", capital, "euro")
print("Taux annuel:", taux, "%")
print("Gain annuel:", gain, "euro")

# Ajouter 5000 euros au capital
capital = capital + 5000 

# Augmente le taux de 2
taux = taux + 2

# Recalculer le gain annuel
gain = capital * taux / 100

print("=== Après augmentation ===")
print("Capital :", capital, "euros")
print("Taux annuel :", taux, "%")
print("Gain annuel :", gain, "euros")