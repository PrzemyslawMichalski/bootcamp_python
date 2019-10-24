#a = [1, 2, 3, 4]
#if 6 in a:
#    print("tak jest !")
#else:
#    print("nie ma")

print("ok, zadanie dla Ciebie. Podaj mi liczby, o powiem czy jestes na planszy. O to liczby: ")
x = input("podaj liczbę x: ")
y = input("podaj liczbę y: ")

if x > 100 or x < 0 or y > 100 or y < 0:
    print("przykro mi, jesteś poza planszą")
elif x > 90 and y < 90:
    print("jesteś w górnym prawym rogu")


q