"""
Zadanie 7
"""
k = int(input("Wpisz liczbe dla k: "))

result = []
for i in range(20, 81):
    if i % k == 0:
        result.append(i / k)
print(result)
