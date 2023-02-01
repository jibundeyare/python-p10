# Énigme 3-02
#
# 02. Persistance multiplicative
#
# Partons du nombre 673 et multiplions tous ses chiffres entre eux : on
# obtient 126. Recommençons l'opération avec 126, on arrive à 12. Enfin
# 12 nous donne 2, nombre à un seul chiffre. On arrête alors le processus.
# Il a donc fallu trois opérations pour passer de 673 à 2.
# On dit que la persistance multiplicative de 673 est trois et que sa suite
# multiplicative est :
#
#     1      2     3
# 673 -> 126 -> 12 -> 2
#
# Trouver la plus petite persistance multiplicative pour un entier
# inférieur à un million.

from pprint import pprint
from timeit import default_timer as timer

repeat = 1000000

# start benchmark
start = timer()

print("Méthode chaîne de caractères")

for _ in range(0, repeat):
    nombre = 673
    produit = 1
    chiffres = str(nombre)

    for chiffre in chiffres:
        produit *= int(chiffre)

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')
print()

# start benchmark
start = timer()

print("Méthode arithmétique")

for _ in range(0, repeat):
    nombre = 673
    produit = 1
    chiffres = nombre

    while chiffres != 0:
        produit *= chiffres % 10
        chiffres //= 10

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

