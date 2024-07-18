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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Returns the report of resources in the machine"""
    for i in resources:
        print("%s: %d" % (i, resources[i]))
    print(f"Money: ${profit}")


def check_resources(order_ingredients):
    """Return True if order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from inputted coins"""
    print("Please insert coins.")
    total = int(input("How many quarters? ($0.25):  ")) * 0.25
    total += int(input("How many dimes? ($0.10): ")) * 0.10
    total += int(input("How many nickels? ($0.05): ")) * 0.05
    total += int(input("How many pennies? ($0.01): ")) * 0.01
    return total


def transaction_success(total, cost):
    if total >= cost:
        change = round(total - cost, 2)
        print(f"Your change is ${change}.")
        global profit
        profit += cost
        return True
    else:
        print("Not enough funds, money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


off = False

while not off:
    choice = input("What would you like? (espresso $1.5/latte $2.5/cappuccino $3.0): ")
    if choice == 'off':
        off = True
    elif choice == 'report':
        report()
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





