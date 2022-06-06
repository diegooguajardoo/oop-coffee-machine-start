from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
on = True

menu = Menu()
money = MoneyMachine()
machine = CoffeeMaker()

while on:
    choice = input("What would you like: (espresso/cappuccino/latte/)")
    if choice == "off":
        quit()
    elif choice == "report":
        print(machine.report())
    elif choice == "espresso":
        item = MenuItem(name="espresso")
        print(item)
    on = False

