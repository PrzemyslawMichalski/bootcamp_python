# losowanie

import random

print(dir(random))
print(help(random.randint))

print(random.randint(1, 10))

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

print("polożenie gracza", gracz_x, gracz_y)
print("położenie skarbu", skarb_x, skarb_y)

# print(abs(100))


odległość = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
print(odległość)

while True:
    print("jestem w pętli")
    break

while True:
    instrukcja = input("by zakończyć wczyśnij: k")
    if instrukcja == "k":
        break