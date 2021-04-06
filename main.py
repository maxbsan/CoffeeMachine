import functions

turned_on = True
while turned_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "report":
        functions.show_report()
    elif selection == "off":
        turned_on = False
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        functions.check_resources(selection)
        if (type(functions.check_resources(selection))) == bool and functions.check_resources(selection):
            functions.check_money(selection)
        else:
            print(f"Sorry, {functions.check_resources(selection)}")
    else:
        print("That's not a valid selection. Please try again.")
