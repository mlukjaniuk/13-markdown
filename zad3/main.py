


def dodaj(a,b):
    suma = a + b
    print(suma)


def test_dodaj():
    assert dodaj(3, 5) == 8
    assert dodaj(100, 111) == 211
    assert dodaj(2.2, 3) == 5.2