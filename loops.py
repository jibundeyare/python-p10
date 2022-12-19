# while == tant que
while False:
  
    print('ce message ne sera pas affiché')

# @warning boucle infinie
# while True:
#     print('ce message sera affiché en boucle')

counter = 10

while counter:
    print(f"{counter = }")
    counter -= 1
    # même chose
    # counter = counter - 1

print()

counter = 0

# le nombre boucle == valeur limite - la première valeur du compteur
while counter < 10:
    print(f"{counter = }")
    counter += 3
    # même chose
    # counter = counter + 3

# boucle de type for == pour
for counter in range(0, 10):
    print(f'{counter = }')

# le 3ème paramètre de range() permet de spécifier l'incrément
# exemple avec un incrément de 2 (au lieu de 1) 
for counter in range(0, 10, 2):
    print(f'{counter = }')

# compte à rebours
for counter in range(10, 0, -1):
    print(f'{counter = }')

fruits = ['abricot', 'baie', 'cerise']

# boucle de type for each == pour chaque
for i, fruit in enumerate(fruits):
    print(f'{i + 1}: {fruit}')

# reversed() renvoie un itérateur économe en mémoire
print(reversed(fruits))
# [::1] renvoie une liste dont la taille est égale à la liste originale (peut ne pas être économe en mémoire)
print(fruits[::-1])

for fruit in reversed(fruits):
    print(fruit)

for fruit in fruits[::-1]:
    print(fruit)


my_list = [123, 2, 42, 3.14, 2, 56, 2]
my_number = 2
counter = 0

for item in my_list:
    if item == my_number:
        counter += 1
        # print(item)

print(f'{counter = }')

my_list = [123, 2, 42, 3.14, 2, 56, 2]
accumulateur = 0

for item in my_list:
    accumulateur += item

print(f'{accumulateur = }')
