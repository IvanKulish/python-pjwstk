"""
Zadanie 4
"""
przed = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
po = [4.5, 5.5, 4.69, 4.99, 4.00]
przedIPo = przed + po
sumaPrzed = sum(przed)
iloscPrzed = len(przed)
sredniaPrzed = sumaPrzed / iloscPrzed
sumaPo = sum(po)
iloscPo = len(po)
sredniaPo = sumaPo / iloscPo
print("Najwyższej cenie po nałożeniu podatku", str(max(po)))
print("Najniższej cenie biorąc pod uwagę wszystkie ceny (przed i po)", str(min(przedIPo)))
print("Średniej cenie przed podwyżką cen: ", sredniaPrzed)
print("średniej cenie po dodaniu nowego podatku: ", sredniaPo)


