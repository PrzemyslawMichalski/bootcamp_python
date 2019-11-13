# str - jest to zamiana liczny na ciąg tekstowy
# int - zamiana testu na liczbę (domyslenie input zawsze podaje str i jak podamy liczbe i chcemy coś do niego dodac to  
#       musimy zmienic ten "test" na liczbę - dlatego używamy int.
# float ma takie samo zastosowanie jak int , ale dotyczny liczb zmienno przecinkowych np. 9.99


#spam = input()
#print(spam)
#print(10 + int(spam))

#spam = int(spam)
#print(spam)
#print(10 + spam)

spam = input()
print(spam)
print(10 + float(spam))

spam = float(spam)
print(spam)
print(10 + spam)