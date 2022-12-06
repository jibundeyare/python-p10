# l'opérateur d'affectation = permet d'injecter une valeur dans une variable

# integer, nombre entier

my_number1 = 123
my_number2 = -42
my_number6 = 0

print(my_number1)
print(my_number2)
print(my_number6)
print(type(my_number6))

# float, nombre à virgule flottante

my_number3 = 3.14
my_number4 = -2.71
# 0.0 ou 0. ou .0
my_number5 = .0
print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number5))

# bool, booléen

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# None, valeur nulle
# null, nil

my_none = None
print(my_none)
print(type(my_none))

# string, chaîne de caractères
# double quote ou simple quote, c'est pareil

my_text1 = "Ceci est une chaîne de caractères"
my_text2 = 'Ceci est aussi une chaîne de caractères'

print(my_text1)
print(my_text2)

# \ caractère d'échappement
# \n saut de ligne

my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = "John \"Foo\" Doe"
print(my_text3)
print(my_text4)
print(my_text5)
print(type(my_text1))

my_text6 = """abc
def
ghi"""
print(my_text6)
my_text7 = '''abc
def
ghi'''
print(my_text6)
print(my_text7)
print(type(my_text6))

foo = "lorem ipsum"
# affectation de valeur à parti d'une variable
bar = foo
print(bar)

a = 123
b = 42
# permutation de la valeur des variables
a, b = b, a
print(a, b)

a = 123
b = 42

# à vous de jouer

# variante qui ne marche qu'avec des nombres
c = a + b
a = c - a
b = c - b
print(a, b)

# transtypage
foo = "123"
# str vers int
foo = int(foo)
print(type(foo))

foo = "123"
# str vers float
foo = float(foo)
print(type(foo))

foo = 3.14
# float vers int, permet de supprimer tout ce qui se touve derrière la virgule
foo = int(foo)
print(foo)

foo = 3.14
# float vers str
foo = str(foo)
print(type(foo))

# # 
# foo = 2.71
# # récupérer la partie entière (c-à-d 2)
# a = 
# # récupérer la partie après les virgule (c-à-d 0.71)
# b = 
# print(a)
# print(b)

# transtypage == type casting == conversion d'un type de données

# 0 donne False et tous les autres nombres donnent True 
my_number7 = 0
# conversion explicite en booléen
print(bool(my_number7))

# conversion implicite en booléen
if my_number7:
    print("L'utilisateur a mis autre chose que zéro")
else:
    print("L'utilisateur a mis zéro")

my_text8 = ''
# conversion explicite en booléen
print(bool(my_text8))

# conversion implicite en booléen
if my_text8:
    print("L'utilisateur a écrit quelque chose")
else:
    print("L'utilisateur n'a rien écrit")

# listes
fruits = ['ananas', 'banane', 'cerise']

# opérateur d'inclusion
result = 'ananas' in fruits
print(result)
result = 'fraise' in fruits
print(result)

# conversion explicite en booléen
result = bool(fruits)
print(result)

# conversion implicite en booléen
if fruits:
    print("La liste contient des éléments")
else:
    print("La liste ne contient aucun élément")

# conversion explicite en booléen
# mais attention None ne peut être converti en int ou float
print(bool(None))
