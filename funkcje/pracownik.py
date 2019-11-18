def utworz_pracowika(imie, nazwisko, email='info@firma.pl', telefon=None):
    pracownik = dict()
    pracownik['imie'] = imie
    pracownik['nazwisko'] = nazwisko
    pracownik['email'] = email
    pracownik['telefon'] = telefon

    return pracownik


print(utworz_pracowika("Jan", "Kowalski"))
print(utworz_pracowika('adam', 'nowa', 'anowak@firm.pl', '5556643'))
print(utworz_pracowika('jan', 'zielisnki', telefon='888666888'))
print(utworz_pracowika('jan', 'zielisnki', email='cos@wp.pl'))
