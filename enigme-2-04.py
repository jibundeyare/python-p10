# Énigme 2-04
#
# 04. Un guichetier pas très sérieux
# Un homme va à la banque pour réclamer le montant en espèce d'un chèque non barré.
# En remettant l'argent, le guichetier lui donne par erreur les euros à la place des centimes et les centimes à la place des euros.
# L'homme empoche l'argent sans vérifier, puis il achète un journal à un euro et trente centimes avant de rejoindre sa maison.
# Il remarque alors qu'il a exactement deux fois plus d'argent que le montant du chèque.
# Quel était le montant du chèque non barré ? 

from timeit import default_timer as timer

# start benchmark
start = timer()

# votre code ici
for euro in range(100, 10000):
    for centime in range(1, 100):
        montant = euro + centime
        montant /= 100

        equation = centime * 98 - (199 / 100) * euro - 130
        # print(equation)

        if equation == 0:
            print(montant)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

