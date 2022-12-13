fruits = ['ananas', 'banane', 'cerise']
print(fruits)

# accès en lecture au 0ème élément de la liste
print(fruits[0])

my_fruit = fruits[0]
print(my_fruit)

# accès en écriture au 0ème élément de la liste
fruits[0] = 'abricot'
print(fruits)
print(fruits[0])

my_count = len(fruits)

index = 0
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

# ajouter un élément
fruits = ['ananas', 'banane', 'cerise', 'mangue']
fruits.append('datte')
print(fruits)

# supprimer un élément sans le récupérer
del fruits[0]
print(fruits)

fruits.remove(0)
print(fruits)

# supprime et renvoie le dernier élément
last_element = fruits.pop()
print(fruits)
print(last_element)

# supprime et renvoie le premier élément
# pop(0) est équivalent à shift()
first_element = fruits.pop(0)
print(fruits)
print(first_element)

# insérer un élément
fruits.insert(1, 'kiwi')
print(fruits)
