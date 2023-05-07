"""
Własny moduł
"""

def oblicz_wiek(data_urodzenia):
    rok_urodzenia = int(data_urodzenia.split('.')[-1])
    return 2023 - rok_urodzenia