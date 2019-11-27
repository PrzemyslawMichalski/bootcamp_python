from random import shuffle

osoby = ['marek', 'przemek', "michał", "kamila"]
osoby2 = ['marek', 'przemek', "michał", "kamila"]
#osoby2 = ['kamila', 'michał', "przemek", "marek"]



def is_in_same_position(lista1, lista2):
    for i, os in enumerate(lista1):
        if os == lista2[i]:
            return True
    return False


print(is_in_same_position(osoby, osoby2))

# tutaj wasza magia:
i = 0
while is_in_same_position(osoby, osoby2):
    i += 1
    shuffle(osoby)
    # shuffle(osoby2)

print(i)
# i sprawdzamy - z wykorzystaniem funkcji zip

for os1, os2 in zip(osoby, osoby2):
    print(f"{os1} kupuje prezent {os2}")


osoby = ['marek', 'przemek', "michał", "kamila"]
shuffle(osoby)
osoby2 = osoby[1:] + osoby[0]