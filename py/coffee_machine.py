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

report = {
    "water":300,
    "milk":200,
    "coffee":100,
}

def insert_coins():
    Q = int ( input ( "How many quarters? " ) )
    D = int ( input ( "How many dimes? " ) )
    N = int ( input ( "How many nickels? " ) )
    P = int ( input ( "How many pennies? " ) )
    dollars = 0.25*Q + 0.1*D + 0.05*N + 0.01*P
    return dollars


turn_on = True
money = 0
'''
1. Make 3 flavor
- Espresso $ 1.50
 - 50 ml Water
 - 18 g Coffee
- Latte $ 2.50
 - 200 ml Water
 - 24 g Coffee
 - 150 ml Milk
- Cappuccino $ 3.00
 - 250 ml Water
 - 24 g Coffee
 - 100 ml Milk

2. Coin Operated
- Penny = 1 cent
- Nickel = 5 cents
- Dime = 10 cents
- Quarter = 25 cents
'''

while turn_on:
    # TODO 1: print what_would_you_want
    what_would_you_want = input("What would you like? (espresso/latte/cappuccino): ")

    if what_would_you_want == "report":
        print(f"Water: {report[0]}ml\nMilk: {report[1]}g\nCoffee: {report[2]}g\nMoney: ${money}") 
    else:
        insert_coins()
        if what_would_you_want == "Espresso":
        elif what_would_you_want == "Latte":
        elif what_would_you_want == "Cappuccino":
            



# TODO 2: what_would_you_want = "report" / "espresso" / "latte" / "cappuccino"
# TODO 3: check resources sufficient or not
    # TODO 3-1: report 中任一項 < 0 則拒絕製作，並印出拒絕的原因
    # TODO 3-2: report 製作完後要材料減少、金額要增加
# TODO 4: process coins & check transaction successfull or not
    # TODO 4-1: 錢夠→要製作，錢不夠→不製作並印出拒絕原因
# TODO 5：make coffee