#
# array slicing
#
s = "Hello!"

print(s[0]) # H
print(s[-2])
print(s[0:5]) #od indeksu 0 do 4 włacznie
print(s[-3]) #3-ci znak od konca

s = "Ruda tańczy jak szalona"
arr = s.split(" ")
print(arr) # pierwszy element listy

print(s[0:16:2]) #co 2-znak od indeksu 0 do 15 włacznie
print(s[::3]) #caly string co 3-ci znak

# Grande finale
# reverse w Pythonie
print(s[::-1])

print("Hello" + "World!")
a = "Hello"
b = "ALX"

# print(f"{a} {b} {1+2}")
# print("{} {} {}".format(a, b, 5+7))

# x = int(input("Podaj wartość x: "))
# # x = int(x)
# print(x, type(x))

