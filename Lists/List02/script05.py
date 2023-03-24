from prettytable import PrettyTable

# inicjalizacja bazy danych
products = [
    {'Nr': 1, 'nazwa': 'Jabłka', 'ilość': 5, 'cena': 2.5},
    {'Nr': 2, 'nazwa': 'Chleb', 'ilość': 1, 'cena': 3.0},
    {'Nr': 3, 'nazwa': 'Mleko', 'ilość': 2, 'cena': 2.0},
    {'Nr': 4, 'nazwa': 'Ser', 'ilość': 3, 'cena': 5.0}
]


# funkcja wyświetlająca produkty w postaci tabeli
def display_products(products):
    table = PrettyTable()
    table.field_names = ["Nr", "Nazwa produktu", "Ilość", "Cena"]
    for product in products:
        table.add_row([product['Nr'], product['nazwa'], product['ilość'], product['cena']])
    print(table)


# funkcja dodająca nowy produkt do bazy danych
def add_product(products):
    nr = len(products) + 1
    nazwa = input("Podaj nazwę produktu: ")
    ilosc = int(input("Podaj ilość produktu: "))
    cena = float(input("Podaj cenę produktu: "))
    product = {'Nr': nr, 'nazwa': nazwa, 'ilość': ilosc, 'cena': cena}
    products.append(product)
    print(f"Dodano produkt: {product}")


# funkcja usuwająca produkt z bazy danych
def delete_product(products):
    nr = int(input("Podaj numer produktu, który chcesz usunąć: "))
    product = None
    for p in products:
        if p['Nr'] == nr:
            product = p
            break
    if product is not None:
        products.remove(product)
        print(f"Usunięto produkt: {product}")
    else:
        print("Nie znaleziono produktu o podanym numerze")


# funkcja modyfikująca produkt w bazie danych
def modify_product(products):
    nr = int(input("Podaj numer produktu, który chcesz zmodyfikować: "))
    product = None
    for p in products:
        if p['Nr'] == nr:
            product = p
            break
    if product is not None:
        nazwa = input("Podaj nową nazwę produktu lub zostaw puste: ")
        ilosc = input("Podaj nową ilość produktu lub zostaw puste: ")
        cena = input("Podaj nową cenę produktu lub zostaw puste: ")
        if nazwa:
            product['nazwa'] = nazwa
        if ilosc:
            product['ilość'] = int(ilosc)
        if cena:
            product['cena'] = float(cena)
        print(f"Zmodyfikowano produkt: {product}")

print("Wyświetlanie:")
display_products(products)
print()

print("Dodawanie:")
add_product(products)
display_products(products)
print()

print("Usuwanie:")
delete_product(products)
display_products(products)
print()

print("Modyfikowanie:")
modify_product(products)
display_products(products)
