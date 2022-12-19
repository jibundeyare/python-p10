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

fruits = ['abricot', 'baie', 'cerise']

# boucle de type for each == pour chaque
for i, foo in enumerate(fruits):
    print(f'{i + 1}: {foo}')
