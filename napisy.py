#
# typ danych - napisy (albo string)
#
napis1 = "ala ma kota"
napis2 = 'ala ma kota'
napis3 = 'a to jest "cudzysłów" '
napis4 = "a to jest \"cudzysłów\" "
napis5 = "znaki specjalne: \t \n \r "

dlugosc = len(napis1)
print("dlugosc zmiennej napis 1 to ", dlugosc, "znaków")

# wiek = input("podaj wiek")
# print("twoj wiek to: ",wiek.strip())

s = "ruda tanczy jak szalona"
print(s.capitalize())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.center(100))
print(s.replace("r","d"))
print("czy liczba: ", s.isdecimal())


print("4 litera: ", s[3])
print("przed ostatnia litera: ", s[-2])
print("litery pomiedzy: ", s[0:8])

s = "hello!"
print(s[0:4])
