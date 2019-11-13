print("Wyobraż sobie plansze 100 na 100 pól...")

print("i teraz podaj mi liczbę X i Y, a powiem Ci czy zmieścisz się na planszy: ")

print("powiem Ci nawet dokładnie gdzie trafisz ! ")


x = int(input("podaj mi liczbę X: "))
y = int(input("podaj mi liczbę Y: "))

if x > 100 or x < 0 or y > 100 or y < 0:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w górnym prawym rogu!")
elif x > 90 and y < 10:
    print("Jesteś w dolnym prawym rogu!")
elif x < 10 and y > 90:
    print("Jesteś w lewym górnym rogu!")
elif x < 10 and y < 10:
    print("Jesteś w lewym dolnym rogu!")
elif x > 90:
    print("Jeteś na prawej krawędzi")
elif x < 10:
    print("Jeteś na lewej krawędzi")
elif y > 90:
    print("Jeteś na górnej krawędzi")
elif y < 10:
    print("Jeteś na dolnej krawędzi")
else:
    print("Jesteś w Centrum")

