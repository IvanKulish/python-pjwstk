"""
Zadanie 9
"""
a = int(input("Wpisz a: "))
b = int(input("Wpisz b: "))
c = int(input("Wpisz c: "))

if a > 0 and b > 0 and c > 0:
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Trójki pitagorejskie.")
    else:
        print("Nie trójki pitagorejskie.")
else:
    print("All numbers must be greater than 0.")
