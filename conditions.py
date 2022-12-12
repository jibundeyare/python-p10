import random

if True:
    print("La condition est vraie")
    print("Ce code est exécuté")

if False:
    print("La condition est fausse")
    print("Ce code n'est pas exécuté")

conditions_vente = False

if conditions_vente:
    print("L'utilisateur a accepté les conditions de vente")
else:
    print("L'utilisateur n'a pas accepté les conditions de vente")

if not conditions_vente:
    print("L'utilisateur n'a pas accepté les conditions de vente")
else:
    print("L'utilisateur a accepté les conditions de vente")

emails = random.randint(0, 3)
print(emails)

# elif c'est la même chose else if

if emails == 1:
    print("Vous avez un nouveau mail")
elif emails > 1:
    print(f"Vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")

windows_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))

print(f'{windows_closed = }')
print(f'{electricity_off = }')

if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité est coupée")
elif not windows_closed and electricity_off:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité est coupée")
elif windows_closed and not electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité n'est pas coupée")
else:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité n'est pas coupée")
