MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "penny": 0.01,
    "dime": 0.10,
    "nickel": 0.05,
    "quarter": 0.25,
}


def check_resources(drink_name):
    """Check if enough ingredients to make drink, return True if enough, return False if not enough ingredients"""
    for ingredient in drink_name:
        global resources
        if drink_name[ingredient] <= resources[ingredient]:
            return True
        else:
            print(f"Sorry there is not enough {ingredient}")
            return False

# TODO: Process coins - quarters, dimes, nickles, pennies
def process_coins():
    """Ask user how much quarters, dimes, nickel and pennies they will put in, calculate the total amount of money"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    total = quarters * coins["quarter"]
    dimes = int(input("How many dimes?: "))
    total += dimes * coins["dime"]
    nickels = int(input("How many nickels?: "))
    total += nickels * coins["nickel"]
    pennies = int(input("How many pennies?: "))
    total += pennies * coins["penny"]
    return total

# TODO: Make coffee and deduct resources
def make_coffee(user_money, drink, drink_name):
    """Make coffee for user and calculate change and deduct ingredients used from resources dictionary"""
    global MENU
    global money
    drink_cost = MENU[drink]["cost"]
    change = user_money - drink_cost
    # Print change with up to 2 decimal places
    print(f"Here is ${change:.2f} in change.")
    print(f"Here is your {drink} ☕. Enjoy!")
    for ingredient in drink_name:
        global resources
        resources[ingredient] -= drink_name[ingredient]
    money += drink_cost

money = 0
make_drink = True
# For checking resources and money from first time:
#print(f"Resources: {resources}")
#print(f"Money: ${money}")
# Ask user what drink they want and this prompt should come again once a drink has been dispensed
while make_drink:
    drink = input("“What would you like? (espresso/latte/cappuccino): ").lower()
# Turn off coffee machine for coffee machine maintainers, when user enters "off"
    if drink == "off":
        make_drink = False
# TODO: Print report of all coffee resources
# Print report if user inputs "report"
    elif drink == "report":
        water = resources["water"]
        print(f"Water: {water}ml")
        milk = resources["milk"]
        print(f"Mik: {milk}ml")
        coffee = resources["coffee"]
        print(f"Coffee: {coffee}ml")
        print(f"Money: ${money}")
# TODO: Check resources sufficient
    else:
        drink_required = MENU[drink]["ingredients"]
        if check_resources(drink_required):
            payment = process_coins()
            drink_cost = MENU[drink]["cost"]
    # TODO: Check transaction successful, If true = coffee and change (if needed_, if false = refund
            if payment < drink_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                make_coffee(payment, drink, drink_required)






