# przypomnienie
# int, float, complex, str,
# list -> [] <- to jest standaradowa lista, tuple -> ()
# dict -> {}  -> to jest znak jaki wstawiamy do słownika

print(dict())
x = dict()
print(type(x))

pol_ang = {
    # "klucz": "wartosc"
    "klucz": "key",
    "wartosc": "value",
    "pies": "dog"
}

print(pol_ang)
print(pol_ang["pies"])
print("dog" in pol_ang)

if "dog" in pol_ang:
    print(pol_ang["dog"])

print(dir(pol_ang))

print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang['kot'] = "cat"

print(pol_ang)

print({1: "a", 2: "b"})
print({1.1: "a", 2.1: "b"})
print({(1, 2): "pierwsza"})
# print({[1, 2]: "pierwsza"}) - lista nie moze być w słowniku


print(pol_ang.keys())
print(pol_ang.values())
print(pol_ang.items())

# set -> {} - jest to kolekcja unikalnch i nieuporzadkowanych watosci

zbior = {1, 2, 3, 4}

print(zbior, type(zbior))

zbior2 = {1, "a", 2, "c", "z", 3}
print(zbior2)

zbior2.add(9)
print(zbior2)

lista = [1, 2, 3, 4, 5, 4, 4, 3, 3, 2, 1, 1, 1, 16, 7]
print(set(lista))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("suma zbiorów: ", A | B, A.union(B))
print("róznica zbiorów: ", A - B, A.difference(B))
print("część wspólna, przecięcie: ", A & B, A.intersection(B))
print("różnica symetryczna: ", A ^ B, A.symmetric_difference(B))
print("podzbiór: ", A.issubset(B))
