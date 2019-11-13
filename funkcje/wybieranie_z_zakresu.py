def wybierz_z_przedzialu(lista, a, b):
    wynik = []
    return wynik


def test_wybierz_z_przedzialu_pusta_lista():
    assert wybierz_z_przedzialu([], 10, 20) == []


def test_wybierz_z_przedzialu():
    assert wybierz_z_przedzialu([1, 13, 20, 35, 27, 2, 1], 10, 20) == [13, 20]
