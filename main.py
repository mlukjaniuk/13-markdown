import math

def dodaj(a, b):
    suma = a+b
    print(suma)

def pierwiastek(a):
    if a < 0:
        print("Nie da się policzyć pierwiastka.")
    else:
        print(math.sqrt(a))

