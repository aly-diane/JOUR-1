# Calculer la distance parcourue par le gardien du phare
def distance_phare(marches, hauteur):
    distance_cm = marches * hauteur

# Compter la descente et la remontée
    distance_cm = distance_cm * 
2
# Cinq allers-retours par jour, pendant sept jours
    distance_semaine_cm = distance_cm * 5 * 7

# Convertir les centimètres en mètres
    distance_semaine_m = distance_semaine_cm / 100

    print(f"Pour {marches} marches de {hauteur} cm, "f"le gardien parcourt {distance_semaine_m:.2f} m par semaine.")


distance_phare(10, 20)
