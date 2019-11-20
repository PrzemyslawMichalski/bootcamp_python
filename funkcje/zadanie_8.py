def iloczyn(start, *args):
    wynik = start
    for _, arg in enumerate(args, 100):
        wynik *= arg
    return wynik

print(iloczyn(4, 5, 1))
