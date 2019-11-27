#
# Typ danych: napisy (albo string)
#
napis1 = "Ala ma kota"
napis2 = 'Ala ma kota'
napis3 = 'A to jest "cudzysłów" '
napis4 = "A to jest \"cudzysłów\" "
napis5 = "Znaki specjalne: \t \n \r "

#dlugosc = len(napis1)
#print("Dlugosc zmiennej napis1 to ",dlugosc,"znaków")

#wiek = input("Podaj wiek:")
#print("Twój wiek to:",wiek.strip())

s = "Ruda tańczy jak szalona"
print(s.capitalize()) #kapitaliki
print(s.upper()) #w gore
print(s.lower()) #w dol
print(s.title()) #formatowanie jako tytul
print(s.swapcase()) #duze->male , male->duze
print(s.center(100)) #centrowanie
print(s.replace("R","D")) #zamiana znakow
print("Czy liczba:",s.isdecimal()) #sprawdzanie czy string jest liczba

print("4-ta litera:", s[3]) #pobierz 4-tą literę napisu
print("Litera przedostatnia:", s[-2]) #

