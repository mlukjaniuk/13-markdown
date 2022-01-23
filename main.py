import math

def dodaj(a,b):
    suma = a + b
    return suma


def pierwiastek(a):
    if a<0:
        return "Nie da się obliczyć pierwiastka."
    else:
        return math.sqrt(a)
