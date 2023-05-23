"""
Zadanie 3 - Lista 2

Napisz skrypt, który będzie grą w kółko i krzyżyk
"""


# plansza
plansza = [' '] * 9

# wyswietlenie planszy
def wyswietl_plansze():
    for i in range(3):
        for j in range(3):
            print(plansza[i * 3 + j], end='')
            if j < 2:
                print(' | ', end='')
        print()
        if i < 2:
            print('---------')


def sprawdz_wygrana():
    wygrane = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # wiersze
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # kolumny
        [0, 4, 8], [2, 4, 6]  # przekątne
    ]
    for wygrana in wygrane:
        if plansza[wygrana[0]] == plansza[wygrana[1]] == plansza[wygrana[2]] != ' ':
            return True
    return False

def sprawdz_remis():
    return ' ' not in plansza

def gra_kolko_i_krzyzyk():
    kolej = 'X'  # Zaczyna gracz X

    while True:
        wyswietl_plansze()

        # Pobranie ruchu od gracza
        ruch = input(f"Gracz {kolej}, podaj numer pola (1-9): ")
        while not ruch.isdigit() or int(ruch) not in range(1, 10) or plansza[int(ruch) - 1] != ' ':
            print("Nieprawidłowy ruch. Spróbuj jeszcze raz.")
            ruch = input(f"Gracz {kolej}, podaj numer pola (1-9): ")
        ruch = int(ruch) - 1

        plansza[ruch] = kolej

        if sprawdz_wygrana():
            wyswietl_plansze()
            print(f"Gracz {kolej} wygrywa!")
            break
        elif sprawdz_remis():
            wyswietl_plansze()
            print("Remis!")
            break
        kolej = 'O' if kolej == 'X' else 'X'


print("Gra w Kółko i Krzyżyk")
gra_kolko_i_krzyzyk()