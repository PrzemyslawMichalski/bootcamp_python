print("podaj mi 10-cięć liczb: ")



suma = 0

for liczby in range(10):
    liczba = input("podaj tresc pytania: ")
    liczba = int(liczba)

    suma = suma + liczba

print(suma / 10)
