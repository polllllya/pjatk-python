"""
Zmodyfikuj zadanie 5 w taki sposób aby stworzyć słownik składany.
Wartościami słownika będą listy słowników zawierające pary (data: punkty)
"""

gracze = ["LeBron James", "Kevin Durant", "Stephen Curry", "Giannis Antetokounmpo", "James Harden"]
punkty = [10.6, 9.1, 7.4, 6.6, 6.3]
daty = ["10-12-2022", "11-13-2023", "01-04-2021", "14-11-2022", "15-08-2021"]

slownik = {gracze[i]: [{"data": daty[i], "punkt": punkty[i]}] for i in range(len(gracze))}

for key, value in slownik.items():
    print(key, "-", end=" ")
    print(value)