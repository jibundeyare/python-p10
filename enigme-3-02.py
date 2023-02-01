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
# Trouver la plus grande persistance multiplicative pour un entier
# inférieur à un million.

from timeit import default_timer as timer

# start benchmark
start = timer()

nombre_maximum = None
compteur_maximum = 0

for nombre in range(10, 1000000):
    # la variable `compteur` va permettre de stocker le nombre d'étapes nécessaires pour calculer la persistance multiplicative du nombre
    compteur = 0
    # la variable `produit` va servir de cumulateur
    # il faut l'initialiser à zéro car nous n'allons par faire d'additions, nous allons faire des multiplications 
    produit = 1
    # on fait une copie du nombre dans une autre variable pour éviter d'en perdre la trace
    # dans la suite de l'algo la variable `chiffres`` sera modifiée
    chiffres = nombre

    # une boucle `while True` permet de s'assurer qu'on rentrera au moins une fois dans la boucle
    while True:
        # on passe en revue tous les chiffres du nombre pour calculer leur produit
        while chiffres != 0:
            # récupération du chiffre la plus à droite dans la variable `chiffre`
            chiffre = chiffres % 10
            # élimination du chiffre la plus à droite (vu qu'on la stocké dans une autre variable)
            chiffres //= 10
            # calcul du produit
            produit *= chiffre

            # si le produit est devenu zéro, ce n'est plus a peine de continuer
            if produit == 0:
                break

        # quand python arrive ici c'est qu'on a calculé une fois le produit de tous les chiffres du nombre, c-à-d qu'on a fait une étape
        # il faut donc incrémenter le compteur d'étapes
        compteur += 1

        # @debug
        # print(nombre, produit)

        # si le produit s'écrit en un seul chiffre, on peut sortir de la boucle 
        if produit < 10:
            break

        # sinon on repart pour une étape en réutilisant les chiffres du produit
        chiffres = produit
        # il faut remettre à 1 la variable produit pour pouvoir calculer la nouveau produit
        produit = 1

    # @debug
    # on affiche le produit seulement s'il est diffférent de 0
    # if produit != 0:
    #     print(f'{nombre = } {compteur = } {produit = }')

    if compteur > compteur_maximum:
        # @debug
        # print(f'{nombre = } {compteur = } {produit = }')

        compteur_maximum = compteur
        nombre_maximum = nombre

print(f'{nombre_maximum = } {compteur_maximum = }')

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

