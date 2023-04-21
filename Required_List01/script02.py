"""
Zmodyfikuj zadanie 1 w taki sposób aby nicki były wypisywane w osobnych wierszach.
Również wykorzytaj tylko jendą instrukcję print.
"""

gracze = ["LeBron James", "Kevin Durant", "Stephen Curry", "Giannis Antetokounmpo", "James Harden",
          "Kawhi Leonard", "Anthony Davis", "Damian Lillard", "Joel Embiid", "Luka Dončić", "Nikola Jokić"]

print(*gracze[:10], sep="\n")