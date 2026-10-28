#Créer une fonction draw_rectangle(width, height) qui affiche un rectangle avec des tirets - et des barres verticales.
def draw_rectangle(width, height):
    # Construire le haut et le bas du rectangle
    ligne_horizontale = "|" + "-" * (width - 2) + "|"

    # Afficher la première ligne
    print(ligne_horizontale)

    # Afficher les lignes du milieu
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Afficher la dernière ligne si elle existe
    if height  > 1:
        print(ligne_horizontale)

draw_rectangle(10, 3)
