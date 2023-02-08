# 5. À la queue leu-leu
#
# Pour savoir jusqu'où elle sait compter, la petite Azélie écrit sur une
# feuille de papier tous les entiers à partir de 1 et à la queue leu-leu :
# 123456789101112131415 etc. On voit par exemple que dans cette liste,
# arrive en 20ème position le chiffre un.
#
# Quel chiffre occupe la 2018ème position ?

# Analyse
#
# chiffres    1  2  3  4  5  6  7  8  9  1  0  ...
# position    1  2  3  4  5  6  7  8  9  10 11 ...

from timeit import default_timer as timer

# start benchmark
start = timer()

# version simple ou il faut lire le résultat à l'écran
position = 0

# le nombre 710 a été trouvé « à la main » de façon à atteindre ou dépasser 2018 en ajoutant seulement un nombre
nombre_max = 710

for nombre in range(1, nombre_max):
    nombre_str = str(nombre)
    position += len(nombre_str)

    # afficher des données ralentit l'algo
    # on affiche que le dernier nombre pour l'accélérer
    if nombre == nombre_max - 1:
        print(f'{nombre = }', f'{position = }')

# réponse : le chiffre à la 2018ème position est 0

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)
print()

# start benchmark
start = timer()

# version alternative plus compliquée mais totalement automatisée
# choix de la position cible
cible = 2018
nombre = 0
position = 0

while position < cible:
    nombre += 1
    nombre_str = str(nombre)
    position += len(nombre_str)

# juste pour info
print(f'{nombre = }', f'{position = }')

# calcul de la position relative de la cible dans nombre_str
position_relative = len(nombre_str) - (position - cible) - 1
chiffre = nombre_str[position_relative]
print(f'{chiffre = }')

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)
