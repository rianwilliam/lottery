""""""
import random
from typing import Set

def get_range_numbers(number_of_numbers: int) -> int:
    """"""
    numbers_range = ""
    while not numbers_range.isdigit() or \
    number_of_numbers > int(numbers_range):
        numbers_range = input("Insira o intervalo de números, de 0 a: ")
    return numbers_range

def raffle_numbers(number_of_numbers: int = 10) -> Set[int]:
    numbers_range = get_range_numbers(number_of_numbers)
    result = set()

    while len(result) != number_of_numbers:
        result.add(
            random.randint(0,int(numbers_range))
        )
    return result
