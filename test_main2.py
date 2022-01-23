from main2 import odejmij
from main2 import kwadrat


def test_odejmij():
    assert odejmij(3, 5) == -2
    assert odejmij(111, 100) == 11
    assert odejmij(3, 2.2) == 0.7999999999999998


def test_kwadrat():
    assert kwadrat(4) == 16
    assert kwadrat(0) == 0
    assert kwadrat(-1) == 1
