"""
Zadanie 6
"""
nicki = {"Robert Lewandowski": 34, "Kylian Mbappe": 23, "Erling Haaland": 22, "Karim Benzema": 35,
         "Mohamed Salah": 30, "Edouard Mendy": 31, "Cristiano Ronaldo": 37, "Kevin De Bruyne": 31,
         "Lionel Messi": 35, "Ciro Immobile": 33}

pkt = {}
for nick in nicki:
    pkt[nick] = []
    for i in range(1):
        pkt[nick].append({f"2023-04-{i}": 0})

print(pkt)