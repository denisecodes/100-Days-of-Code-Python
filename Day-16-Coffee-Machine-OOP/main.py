from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

make_drink = True
while make_drink:
    # Prompt user to choose a drink
    options = menu.get_items()
    choice = input(f"What would you like? {options} : ").lower()
    if choice == 'off':
        make_drink = False
#Print report
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #Check resources is sufficient and if payment is sufficient
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            #Make coffee and deduct resources
            coffee_maker.make_coffee(drink)




