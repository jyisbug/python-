from coffee import MENU, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    """判断原材料是否足够"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            is_enough = False
        return is_enough


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def process_coins():
    """从硬币计算总数"""
    print("Please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.10
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}")


machine_continue = True
while machine_continue:
    choice = input("What would you like?(espresso/latte/cappuccino):").lower()
    if choice == 'off':
        machine_continue = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk{resources['milk']}: 50ml")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


