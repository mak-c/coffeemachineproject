MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

money = 0

# TODO 1. Print a report of all the coffee machine resources
# TODO 2. Check resources sufficient to make coffee
# TODO 3. Turn off the coffee machine by typing 'off'
# TODO 4. Prompt user 'What would you like?'
# TODO 5. Process coins
# TODO 6. Check transaction successful
# TODO 7. Make coffee (deduct resources)



def report():
    for i in resources:
        print("%s: %d" % (i, resources[i]))
    print(f"Money: ${money}")


def check_resources(coffee_input):
    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee = resources["coffee"]
    no_of_ingredients = len(coffee_input)
    if no_of_ingredients == 2:
        #it's an espresso, so compare water and coffee only
        water = coffee_input[0]
        coffee = coffee_input[1]
        if water > resource_water:
            print("Sorry there is not enough water.")
            return
        elif coffee > resource_coffee:
            print("Sorry there is not enough coffee.")
            return
    else:
        #the coffee has all ingredients to compare with available resources
        water = coffee_input[0]
        milk = coffee_input[1]
        coffee = coffee_input[2]
        if water > resource_water:
            print("Sorry there is not enough water.")
            return
        elif milk > resource_milk:
            print("Sorry there is not enough milk.")
            return
        elif coffee > resource_coffee:
            print("Sorry there is not enough coffee.")
            return
    return True


def process_coins():
    quarters = int(input("How many quarters? ($0.25):  "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickels = int(input("How many nickels? ($0.05): "))
    pennies = int(input("How many pennies? ($0.01): "))
    total = ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    return total


def transaction_success(total, cost):
    if cost > total:
        print("Not enough funds, money refunded.")
        return False
    else:
        global money
        change = total - cost
        money += cost
        print(f"Your change is ${round(change, 2)}.")
        return True


off = False

while not off:
    user_input = input("What would you like? (espresso $1.5/latte $2.5/cappuccino $3.0): ")
    if user_input == 'report':
        report()
    elif user_input == 'off':
        off = True
    elif user_input == 'espresso':
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]
        ingredients = [water, coffee]
        if check_resources(ingredients) and transaction_success(process_coins(), cost):
            resources["water"] -= water
            resources["coffee"] -= coffee
            print("Here is your espresso, enjoy!")
        else:
            print("contact your coffee machine technician")

    elif user_input == 'latte':
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        cost = MENU["latte"]["cost"]
        ingredients = [water, milk, coffee]
        if check_resources(ingredients) and transaction_success(process_coins(), cost):
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            print("Here is your latte, enjoy!")
        else:
            print("contact your coffee machine technician")

    elif user_input == 'cappuccino':
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = MENU["cappuccino"]["cost"]
        ingredients = [water, milk, coffee]
        if check_resources(ingredients) and transaction_success(process_coins(), cost):
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            print("Here is your cappuccino, enjoy!")
        else:
            print("contact your coffee machine technician")

    else:
        print("Invalid input, please try again.")






