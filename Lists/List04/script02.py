"""
Lista B - Lab5 - Zadanie 2
"""

# Pierwsza lista z nazwami sklepów
sklepy = ['Auchan', 'Carrefour', 'Lidl', 'Biedronka', 'Kaufland']

# Druga lista z produktami (słowniki)
produkty = [{'nazwa': 'Jogurt', 'producent': 'Danone', 'data_waznosci': '2023-01-01', 'kategoria': 'Nabial'},
            {'nazwa': 'Chleb', 'producent': 'Mąka Polska', 'data_waznosci': '2023-04-15', 'kategoria': 'Pieczywo'},
            {'nazwa': 'Masło', 'producent': 'Mlekovita', 'data_waznosci': '2023-03-30', 'kategoria': 'Nabial'},
            {'nazwa': 'Mleko', 'producent': 'Łowicz', 'data_waznosci': '2023-04-12', 'kategoria': 'Nabial'},
            {'nazwa': 'Pomidor', 'producent': 'Ogrodnik', 'data_waznosci': '2023-04-13', 'kategoria': 'Warzywa'}]

# Trzecia lista z cenami produktów
ceny = [2.5, 3.0, 5.5, 2.2, 1.5]

# Czwarta lista z klientami
klienci = ['Jan Kowalski', 'Adam Nowak', 'Maria Zielińska']

# Piąta lista z kupionymi produktami
kupione_produkty = ['Jogurt', 'Chleb', 'Masło', 'Mleko', 'Pomidor']

# 1. Wyświetlenie sklepów i produktów
sklepy_produkt = [(sklep, produkt['nazwa']) for i, sklep in enumerate(sklepy) if i % 2 != 0 for j, produkt in enumerate(produkty) if j % 6 == 0]
print("Sklepy i produkty:")
print(sklepy_produkt)

# 2. Utworzenie listy produktów dla każdego klienta
produkty_klientow = [[produkty[i] for i in range(len(produkty)) if (j+1) % (i+1) == 0] for j in range(len(klienci))]
print("Produkty dla każdego klienta:")
print(produkty_klientow)

# 3. Utworzenie listy przyporządkowującej cenę do produktu
produkty_ceny = [(produkty[i]['nazwa'], ceny[::-1][j]) for j, i in enumerate(range(len(produkty)))]
print("Produkty i ceny:")
print(produkty_ceny)
