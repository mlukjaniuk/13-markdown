import main


def test_dodaj():
    assert main.dodaj(3, 5) == 8
    assert main.dodaj(100, 111) == 211
    assert main.dodaj(2.2, 3) == 5.2