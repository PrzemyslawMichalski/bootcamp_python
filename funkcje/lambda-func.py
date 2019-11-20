# funkcje anonimowe

# x = lambda x: x % 2 == 0
# print(x(10, 6))

# def fun_sort(x):
#    return x[1]

# lista = [('jablko', 2.99), ('banan', 4.99), ('winogrona', 1.99)]
# print(sorted(lista, key=lambda x: x[1]))

# lista = (1, 2, 3, 4, 5, 6, 7)

# def wybierz(lista, funkcja):
# wynik = []
#     if funkcja(el) is True:
#          wynik.append(el)
#           return wynik
#
#
# print(wybierz(lista, lambda x: x % 3 == 0))

lista = (1, 2, 3, 4, 5, 6, 7)
def wybierz(lista, funkcja):
    wynik = []
    for el in lista:
        if funkcja(el) is True:
            wynik.append(el)
        return wynik


print(wybierz(lista, lambda x: x > 3))
