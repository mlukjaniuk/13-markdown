import main2


def test_dodaj():
    assert main2.odejmij(3, 4) == -1
    assert main2.odejmij(5, 6) == -1
    assert main2.odejmij(10, 100) == -90


def test_pierwiastek():
    assert main2.kwadrat(4) == 16
    assert main2.kwadrat(3) == 9
    assert main2.kwadrat(81) == 6561