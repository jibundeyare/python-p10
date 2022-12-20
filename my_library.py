import random

def randint_list(lower_value: int, higher_value: int, count: int=10) -> list:
    numbers = []

    for i in range(0, count):
        number = random.randint(lower_value, higher_value)
        numbers.append(number)

    return numbers

# écrire une fonction qui accepte en paramètre une liste et qui renvoie la moyenne des nombres de la liste
def my_average(numbers: list) -> float:
    my_sum = 0

    for number in numbers:
        my_sum += number

    result = my_sum / len(numbers)

    return result

def my_average2(numbers: list) -> float:
    my_sum = 0
    count = 0

    for number in numbers:
        if type(number) is int or type(number) is float:
            my_sum += number
            count += 1

    result = my_sum / count

    return result
