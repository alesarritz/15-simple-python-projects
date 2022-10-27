from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

answer = input(f"What would you like? ({menu.get_items()})?: ")
while answer != "off":
    if answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(answer)
        if type(menu_item) is MenuItem and coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost) is True:
                coffee_maker.make_coffee(menu_item)

    answer = input(f"What would you like? ({menu.get_items()})?: ")

