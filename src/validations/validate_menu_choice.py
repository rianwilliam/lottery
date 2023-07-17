"""Validates user-entered values"""
from typing import List

def validate_option(choice: int, menu_items: List[str] = []) -> bool:
    """
    Validates the values entered by the user, if they are digits and
    if they correspond to any menu option

    * Args:
        \t - choice (int):
    """
    if not choice.isdigit():
        return False
    elif int(choice) < 0 or int(choice) > len(menu_items):
        return False
    return True

def validate_numbers_range(numbers_range: str) -> bool:
    """"""
    if not numbers_range.isdigit():
        return False
    return True
