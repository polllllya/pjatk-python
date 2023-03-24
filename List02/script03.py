size = int(input("Podaj rozmiar tabliczki mnożenia: "))

for i in range(1, size + 1):
    row = ""
    for j in range(1, size + 1):
        product = i * j
        row += str(product).rjust(4) # dopasuj do 4 znaków i wypełnij spacjami z lewej strony
    print(row)
