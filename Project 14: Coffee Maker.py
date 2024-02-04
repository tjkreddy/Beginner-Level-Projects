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


def resources_check():
    recipe = (MENU[order])
    ingredients = recipe["ingredients"]
    for item in ingredients:
        if ingredients[item] <= resources[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False


def coins_processing():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(inserted_money):
    recipe = (MENU[order])
    if inserted_money >= recipe["cost"]:
        extra_amount = round((inserted_money - recipe["cost"]), 2)
        global profit
        profit += recipe["cost"]
        print(f"Here is {extra_amount} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def making_coffee():
    recipe = (MENU[order])
    ingredients = recipe["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order} ☕️. Enjoy!")


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        enough_ingredients = resources_check()
        if enough_ingredients:
            total_money = coins_processing()
            if transaction(total_money):
                making_coffee()
