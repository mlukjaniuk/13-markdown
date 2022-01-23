from main import dodaj
from main import pierwiastek

def test_dodaj():
    assert dodaj(3, 5) == 8
    assert dodaj(100, 111) == 211
    assert dodaj(2.2, 3) == 5.2


def test_pierwiastek():
    assert pierwiastek(4) == 2.0
    assert pierwiastek(3) == 1.7320508075688772
    assert pierwiastek(-1) == "Nie da się obliczyć pierwiastka."
