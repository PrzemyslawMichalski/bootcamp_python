def iloczyn(*args):
    wynik = 1
    for nr, arg in enumerate(args, 1):
        # print(f'Pozycja {nr}={arg}')
        wynik = wynik * arg
        return wynik


print(iloczyn(1, 2, 3, 4, 5))
