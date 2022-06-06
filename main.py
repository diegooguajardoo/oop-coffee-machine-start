from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
on = True

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while on:
    options = menu.get_items()
    choice = input(f"What would you like: ({options}): ")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)

