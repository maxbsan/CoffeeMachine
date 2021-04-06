from data import menu, resources, money


def show_report():
    """Prints a report of the contents of the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(money['total'], 2)}")


def check_resources(coffee):
    """Checks the recipe and the resources in the machine to determine if the coffee can be prepared"""
    total_water = resources['water']
    total_milk = resources['milk']
    total_coffee = resources['coffee']
    enough_wa = True
    enough_mi = True
    enough_co = True

    wa = menu[coffee]["ingredients"]["water"]
    co = menu[coffee]["ingredients"]["coffee"]
    mi = 0
    if coffee == "latte" or coffee == "cappuccino":
        mi = menu[coffee]["ingredients"]["milk"]

    if total_water < wa:
        enough_wa = False
    if total_milk < mi:
        enough_mi = False
    if total_coffee < co:
        enough_co = False

    if enough_co and enough_mi and enough_wa:
        return True
    elif not enough_wa:
        return "not enough water"
    elif not enough_mi:
        return "not enough milk"
    elif not enough_co:
        return "not enough coffee"


def make_coffee(coffee):
    """Prepares and returns the selected coffee. At the end it subtracts the utilized resources."""
    print(f'Here is your {coffee}! ☕️ Enjoy.')
    decrease_resources(coffee)


def decrease_resources(choice):
    resources["water"] -= menu[choice]["ingredients"]["water"]
    resources["coffee"] -= menu[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        resources["milk"] -= menu[choice]["ingredients"]["milk"]


def check_money(choice):
    """Asks for payment and checks if it's enough or short"""
    total_cost = menu[choice]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))

    total_input = (quarters * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)

    if total_input > total_cost:
        money["total"] += total_input
        change = total_input - total_cost

        if money['total'] > change:
            print(f"Here is ${round(change, 2)} in change")
            money["total"] -= change
            make_coffee(choice)
        else:
            money["total"] -= total_input
            print("Sorry not enough change. Operation cancelled")

    elif total_input == total_cost:
        money["total"] += total_input
        make_coffee(choice)
    else:
        print("Not enough money. Operation cancelled")
