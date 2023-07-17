"""Options selection file"""
from src.screens.options import menu
from src.prize_draw.raffle import raffle_numbers
from src.screens.result_screen import screen_results

def lottery_game() -> None:
    """
    Executes functions that allow the user to change
    the number of numbers and the range of numbers to be drawn
    """
    menu_choice = ""
    number_of_numbers = 0
    result = set()

    while not menu_choice:
        menu_choice = menu(
            menu_msg="Olá seja bem vindo(a) a loteria",
            menu_items=["Jogar","Selecionar quantidade de números, o padrão é 10"]
        )

    if menu_choice == 1:
        result = raffle_numbers()
    elif menu_choice == 2:
        number_of_numbers = int(input("Insira a quantidade de números: "))
        result = raffle_numbers(number_of_numbers)

    screen_results(result)
