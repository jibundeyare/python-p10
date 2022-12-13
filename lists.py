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
