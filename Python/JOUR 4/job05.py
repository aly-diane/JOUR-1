def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return"Erreur : division par 0"
        return num1 % num2
    else:
        return "operateur invalide"


    print(calcule(10, "+", 5))
    print(calcule(10, "-", 5))
    print(calcule(10, "*", 5))
    print(calcule(10, "/", 5))
    print(calcule(10, "%", 5))