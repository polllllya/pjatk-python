"""
Lab04 - For Loop
"""

# przykłady pętli for
listaA = ["abc", [1, 2, 3]]

for i in listaA:
    print(i)

for i in range(len(listaA)):
    print(i)

print()

for i in listaA:
    print(i)
    for j in i:
        print(j)

print()
# przykłady formatowania tekstu
for x in range(-10, 11):
    print("%+i" % x, end=" ")  # + - znak przed liczbą

print("\n")

for x in range(5, 100, 10):
    print("%3i%6o%5x" % (x, x, x))  # wyrownanie po prawej

print()

for x in range(5, 100, 10):
    print("%#-3i%#-6o%#-5x" % (x, x, x))  # wyrównanieod lewej #-prefiks

print()

for x in range(5, 100, 5):
    print("%-3i%-6o%-5x" % (x, x, x))


print()

for x in range(5,100,10):
    print("%03i %04o %04x" % (x,x,x))

print()

# Formatowanie tekstu
for x in range(5, 100, 10):
    print("{2} {0} {1}".format(x,oct(x),hex(x)))  # wyrownanie po prawej
