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

# 起始值
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

report = {
    "water":300,
    "milk":200,
    "coffee":100,
}


def insert_coins():
    '''return total amount from coin insert.'''
    Q = int ( input ( "How many quarters? " ) )
    D = int ( input ( "How many dimes? " ) )
    N = int ( input ( "How many nickels? " ) )
    P = int ( input ( "How many pennies? " ) )
    dollars = 0.25*Q + 0.1*D + 0.05*N + 0.01*P
    return dollars


def resources_sufficient_or_not(drink):
    '''return True when order can be made.Otherwise, return False'''
    for item in drink:
        if drink[item] > report[item]:
            print(f'Sorry there is not sufficent {item}.')
            return False
    return True


# def if_transacton_sucessed(moner_received, drink_cost):
    


turn_on = True
profit = 0


while turn_on:
    change = 0
    what_would_you_want = input("What would you like? (espresso/latte/cappuccino)\nOr type 'off' to turn off this machine: ").lower()
    if what_would_you_want == 'off':
        turn_on = False
    elif what_would_you_want == "report":
        print(f"Water: {report['water']}ml\nMilk: {report['milk']}g\nCoffee: {report['coffee']}g\nMoney: ${profit}") 
    else:
        drink = MENU[what_would_you_want]
        if resources_sufficient_or_not(drink['ingredients']):
            money_received = insert_coins()
            if money_received < drink['cost']:
                print('Sorry that\'s not enough money. Money refunded.')
            else:
                profit += drink['cost']
                change = round(money_received - drink['cost'], 2)
                print(f'Here\'s ${change} in change.')
                for item in drink['ingredients']:
                    report[item] -= drink['ingredients'][item]
            
                



# TODO 1: print what_would_you_want
# TODO 2: what_would_you_want = "report" / "espresso" / "latte" / "cappuccino"
# TODO 3: check resources sufficient or not
    # TODO 3-1: report 中任一項 < 0 則拒絕製作，並印出拒絕的原因
    # TODO 3-2: report 製作完後要材料減少、金額要增加
# TODO 4: process coins & check transaction successfull or not
    # TODO 4-1: 錢夠→要製作，錢不夠→不製作並印出拒絕原因
# TODO 5：make coffee