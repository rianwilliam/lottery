"""Graphic interface"""
from typing import List
from src.validations.validate_menu_choice import validate_option

def menu(menu_msg: str, menu_items: List[str] = []) -> int:
    """
    Print the user menu
    """
    print(menu_msg)
    for index, item in enumerate(menu_items):
        print(f"[{index+1}] - {item}")
    choice = input("Insira a opção desejada: ")
    if not validate_option(choice, menu_items):
        return 0
    return int(choice)
