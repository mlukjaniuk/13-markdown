import main


def test_dodaj():
    assert main.dodaj(3, 4) == 7
    assert main.dodaj(5, 6) == 11
    assert main.dodaj(10, 100) == 110


def test_pierwiastek():
    assert main.pierwiastek(-1) == "Nie da się policzyć pierwiastka."
    assert main.pierwiastek(3) == 1.7320508075688772
    assert main.pierwiatek(81) == 9.0
