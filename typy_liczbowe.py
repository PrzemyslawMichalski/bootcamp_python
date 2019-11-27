# w Pythonie mamy:
# liczby całkowite - integer - int

x = 10
print(type(10))
print(int())
print(int("10"))
print(int("10", base=3))
print(int(2.7))

# liczby zmiennoprzecinkowe - float
print(float())
print(float(1 / 3))
print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 == 0.3)

from decimal import Decimal

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1))
print(Decimal(0.3))

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))

print(round(0.1 + 0.1 + 0.1, 1))
print(round(1.23, 3))
# notacja naukowa
print(1e12)

# liczby zespolone: complex
print(complex())
print(10 + 11j)

# wartości boolowskie: bool  True False
print(bool())
print(10 + True)
# print(10/False)
# or and not

# Prześledzić działanie operatorów logicznych or and not
print(True and False)
print(not (True))
print(True or False)

# github
