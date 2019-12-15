import Funkcje

def test_add():
    assert Funkcje.add(7, 3) == 10
    assert Funkcje.add(7, -1) == 6
    assert Funkcje.add(4.3, 5.6) - 9.9 < 0.0000001


def test_product():
    assert Funkcje.product(0, 0) == 0
    assert Funkcje.product(-1, 0) == 0
    assert Funkcje.product(-1, -1) == 1
    assert Funkcje.product(5, 2.5) == 12.5
    assert Funkcje.product(3, 4) == 12

def test_polidrom():
    assert Funkcje.polidrom("nurses run")
    assert Funkcje.polidrom("Ala")
    assert Funkcje.polidrom("Kobyła ma mały bok")
    assert Funkcje.polidrom("111")
