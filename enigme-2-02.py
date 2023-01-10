# 2. Entiers consécutifs
# 198, 199, 200, 201 et 202 sont des entiers consécutifs dont la somme est égale à 1000.
# Trouvez d'autres entiers consécutifs dont la somme vaut 1000.

# [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# [198, 199, 200, 201, 202]

somme = 0
nombres = []

for i in range(1, 500):
    nombres.append(i)
    somme = sum(nombres)

    while somme > 1000:
        nombres.pop(0)
        somme = sum(nombres)

    if somme == 1000:
        print(nombres)
