print("podaj mi liczby: ")

import random

DEBUG = True

# print(random.randint(1, 10))

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

print("polożenie gracza", gracz_x, gracz_y)
print("położenie skarbu", skarb_x, skarb_y)

odległość_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
print('to jest odległość od twojego skarbu: ', odległość_po_wylosowaniu)

if DEBUG:
    print(f'położenie gracza (x={gracz_x}, y={gracz_y})')
    print(f'położenie skarbu (x={skarb_x}, y={skarb_y})')
    print(f"minimalna liczba ruchów = {odległość_po_wylosowaniu}")

while True:
    ruch = input('wpisz komendę (a-lewo, d-prawo, w-góra, s-dół)')
    if ruch == 'a':
        gracz_x = gracz_x - 1
    elif ruch == 's':
        gracz_y = gracz_y - 1
    elif ruch == 'd':
        gracz_x = gracz_x + 1
    elif ruch == 'w':
        gracz_y = gracz_y + 1
    else:
        print('trzymaj się reguł')

    if DEBUG:
        print(f'położenie gracza (x={gracz_x}, y={gracz_y})')
        print(f'położenie skarbu (x={skarb_x}, y={skarb_y})')

    if not (1 <= gracz_x <= 10 and 1 <= gracz_y <= 10):
        print('wypadłeś poza planszę')
        break

    odległość_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    if odległość_po_ruchu < odległość_po_wylosowaniu:
        print('ciepło')
    elif odległość_po_ruchu > odległość_po_wylosowaniu:
        print('zimno')
    else:
        print('bez zmian')
