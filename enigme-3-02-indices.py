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

# méthode 1 : chaîne de caractères
nombre = 673
# la valeur initiale du produit doit être `1` et pas `0` sinon le résultat final sera aussi un `0`
# cette variable sert d'accumulateur
produit = 1
# on convertit le nombre en chaîne de caractères
chiffres = str(nombre)

# on parcourt chaque caractère de la chaîne
# cet algorithme ressemble à celui de la somme (addition) mais ici c'est pour pour obtenir un produit (multiplication)
for chiffre in chiffres:
    print(chiffre)
    # avant de multiplier le chiffre, il faut le reconvertir en nombre
    produit *= int(chiffre)

print(f'{produit = }')

# méthode 2 : arithmétique
nombre = 673

# le modulo `%` permet de récupérer le ou les chiffres qui sont à droite dans un nombre
chiffres = nombre % 10
print(chiffres) # 3

chiffres = nombre % 100
print(chiffres) # 73

chiffres = nombre % 1000
print(chiffres) # 673

# la division entière `//` permet de récupérer le ou les chiffres qui sont à gauche dans un nombre
chiffres = nombre // 1
print(chiffres) # 673

chiffres = nombre // 10
print(chiffres) # 67

chiffres = nombre // 100
print(chiffres) # 6

# en combinant les deux opérations on peut récupérer les chiffres un par un

# algo A : récupération des chiffres par la droite
temp = nombre // 1 # 673
chiffre = temp % 10 # 3 <- chiffre
print(chiffre)

temp = nombre // 10 # 67
chiffre = temp % 10 # 7 <- chiffre
print(chiffre)

temp = nombre // 100 # 6
chiffre = temp % 10 # 6 <- chiffre
print(chiffre)

# maintenant la question se pose de comment obtenir la suite [1, 10, 100, ...]
#
# la suite [1, 10, 100, ...] est une suite de puissance de 10 :
#
# 1     = 10 / 10           = 10 ** 0
# 10    = 10                = 10 ** 1
# 100   = 10 * 10           = 10 ** 2
# 1000  = 10 * 10 * 10      = 10 ** 3

# affichage des puissances de 10 en ordre croissant pour l'algo A
for i in range(0, 3):
	# la variable i indique la puissance
	print(10 ** i)

# du coup on peut combiner la génération de puissance de 10 et la récupération des chiffres du nombre

# affichage des chiffres par la droite
for i in range(0, 3):
	# on applique l'algo A décrit en haut
	temp = nombre // (10 ** i)
	chiffre = temp % 10
	print(f'{chiffre = }')

# le nombre de fois où on boucle dépend du nombre de chiffres du nombre
# 1 chiffres -> 1 itérations
# 2 chiffres -> 2 itérations
# 3 chiffres -> 3 itérations
# 4 chiffres -> 4 itérations
# ...

# mais comment savoir le nombre de chiffres ?

# méthode 1 : chaîne de caractères
nombre = 673
nombre_str = str(nombre)
longueur = len(nombre_str)
print(f'{longueur = }') # 3

# méthode 2 : arithmétique

# on peut utilier la division entière `//` pour enlever un chiffre à droite à chaque fois

# algo C
# on copie le nombre dans une variable pour éviter de modifier le nombre
chiffres = nombre # 673

chiffres //= 10 # 67
print(chiffres)

chiffres //= 10 # 6
print(chiffres)

chiffres //= 10 # 0
print(chiffres)

# il a fallu 3 étapes pour arriver à zéro `0`
# ça veut dire qu'il y a 3 chiffres

# on peut utiliser une boucle while pour trouver le nombre d'étapes nécessaires pour arriver à zéro `0`
longueur = 0
chiffres = nombre

while chiffres != 0:
	# on applique l'algo C
	chiffres //= 10
	longueur += 1

print(f'{longueur = }') # 3

# maintenant on peut tou combiner pour créer une fonction qui renvoie la liste des chiffres en partant de la droite ou de la gauche

def longueur_nombre(nombre):
	longueur = 0
	chiffres = nombre

	while chiffres != 0:
		chiffres //= 10
		longueur += 1

	return longueur

def chiffres_par_droite(nombre):
	chiffres = []
	longueur = longueur_nombre(nombre)

	# on utilise la longueur au lieu d'une valeur fixe
	for i in range(0, longueur):
		temp = nombre // (10 ** i)
		chiffre = temp % 10
		chiffres.append(chiffre)
	
	return chiffres

# on test
nombre = 673
produit = 1
longueur = longueur_nombre(nombre)
chiffres = chiffres_par_droite(nombre)

print(f'{longueur = }') # 3
print(f'{chiffres = }') # [3, 7, 6]


for i in chiffres:
	produit *= i

print(f'{produit = }') # 126

# ça marche :)

# cependant ATTENTION :
# - cet l'algo ne fonctionne qu'avec des nombres positifs
#   pour les nombres négatifs, il faudra l'adapter
# - quand on fait un benchmark des algo méthode chaîne de caractère et méthode arithmétique, la méthode chaine de caractère est plus rapide !
#   pour que la méthode arithmétique soit plus rapide il faut complètement épurer le code
#   voir le fichier `enigme-3-02-benchmark.py`
#
# conclusion : il faudra choisir la version de l'algo (chaîne de caractères ou arithmétique) selon le langage, la situation, la lisibilité du code et facilité à le maintenir

