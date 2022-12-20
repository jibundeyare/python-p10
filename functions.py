def addition(a: float, b: float) -> float:
    """Cette fonction permet d'additionner deux nombres

    a float le premier nombre à additioner
    b float le deuxième nombre à additioner
    return float le résultat de l'addition
    """
    result = a + b

    return result

result = addition(123, 42)
print(result)

my_number1 = 123
my_number2 = 42
result = addition(my_number1, my_number2)
print(result)

def calculer(calcul1: callable, calcul2: callable, a: float, b: float, c: float) -> float:
    result = calcul1(a, b)
    result = calcul2(result, c)

    return result

result = calculer(addition, addition, 123, 42, 3.14)
print(result)
