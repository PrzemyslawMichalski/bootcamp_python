# zapytaj użytkownika o text
# zapytaj użytkownika o szerokość
# wyświetl tekst, który będzie mial same duze litery
# text powinien byc wycentrowany - zgodnie z wartoscia szerokosci
# podaj napis: ala
# podaj szerokość: 10
# !   ala   !

napis = input("Podaj napis: ")
width = int(input("Podaj szerokość: "))

print("!"+napis.center(width)+"!")
print(f"!{napis.center(width)}!")

