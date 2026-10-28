# Créer une fonction qui reçoit un entier et une phrase, puis retourner les mots dont la longueur est strictement supérieure à cet entier.
# Ne pas utiliser les fonctions len() ni sort ().
def my_long_word(chiffre, phrase):
    mots = phrase.split()
    resultat = []
    for mot in mots:
        longueur = 0
        for caractere in mot:
            longueur += 1
        if longueur > chiffre:
            resultat.append(mot)
    return " ".join(resultat)
phrase = ("La peur est le chemin vers le côté obscur," "la peur mène à la colère, la colère mène à la haine," 
          "la haine mène à la souffrance")
print(my_long_word(3, phrase))