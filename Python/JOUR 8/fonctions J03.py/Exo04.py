# Afficher les nombres de 1 à 100 en utilisant Fizz et Buzz.
for nombre in range(1, 101):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre  % 3 == 0:
        print("Fizz")
    elif nombre  % 5 == 0:
        print("Buzz")
    else:
        print(nombre)

# Transformer en fonction
def nombre_comp():
    for nombre in range(1, 101):
        if nombre % 3 == 0 and nombre % 5 == 0:
            print("FizzBuzz")
        elif nombre  % 3 == 0:
            print("Fizz")
        elif nombre  % 5 == 0:
            print("Buzz")
        else:
            print(nombre)
nombre_comp()

