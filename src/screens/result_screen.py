""""""
from typing import Set

def screen_results(results: Set[int]) -> None:
    """"""
    for number in list(results):
        print(f"|{number}|", end=" ")
    print("")

