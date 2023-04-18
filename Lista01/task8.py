"""
Zadanie 8
"""
poczatek = int(input("Wpisz pocz: "))
koniec = int(input("Wpisz koncowu liczbu: "))
k = int(input("Wpisz liczba dla k: "))

result = {}
for i in range(poczatek, koniec + 1):
    if i % k == 0:
        result[i] = i / k
print(result)
