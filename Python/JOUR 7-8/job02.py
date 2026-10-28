# Dessiner un triangle
def draw_triangle(height):
    for i in range(height):
        espaces = " " * (height - i - 1)

        if i == 0:
            print(espaces + "_")
        elif i == height - 1:
            print("/" + "_" * (2 * i - 1) + "\\")
        else:
            print(espaces + "/" + " " * (2 * i - 1) + "\\")

hauteur = int(input("Entrez la hauteur du triangle :"))

draw_triangle(hauteur)