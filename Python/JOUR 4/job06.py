def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

verifier_nombre(5)
verifier_nombre(-6)
verifier_nombre(0)