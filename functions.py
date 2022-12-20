from collections.abc import Callable
import my_library
from my_library import randint_list

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

def calculer(calcul1: Callable, calcul2: Callable, a: float, b: float, c: float) -> float:
    result = calcul1(a, b)
    result = calcul2(result, c)

    return result

result = calculer(addition, addition, 123, 42, 3.14)
print(result)

# le code "import my_library" oblige à préciser le nom de la librairie devant le nom de la fonction
my_list = my_library.randint_list(0, 100)
print(my_list)

# le code "from my_library import randint_list" permet de ne pas préciser le nom de la librairie devant le nom de la fonction
my_list = randint_list(0, 10, 300)
print(my_list)

result = my_library.my_average(my_list)
print(result)

my_list = [42, True, 'abc', 123]
result = my_library.my_average2(my_list)
print(result)
