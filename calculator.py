logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os
def clear():
    os.system('cls')

continue_cal = True

def add(num1, num2):
    return num1 + num2
def diff(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

print(logo)
num1 = float(input("What\'s the first number? "))
op = input("+\n-\n*\n/\nPick an operation: ")
num2 = float(input("What\'s the next number? "))

while continue_cal:
    if op == "+":
        print(f"{num1} {op} {num2} = {add(num1, num2)}")
        num1 = add(num1, num2)
    elif op == "-":
        print(f"{num1} {op} {num2} = {diff(num1, num2)}")
        num1 = diff(num1, num2)
    elif op == "*":
        print(f"{num1} {op} {num2} = {mul(num1, num2)}")
        num1 = mul(num1, num2)
    elif op == "/":
        print(f"{num1} {op} {num2} = {div(num1, num2)}")
        num1 = div(num1, num2)
    check_con = input(f"\nType \"Q\" to end the calculator.\nType \"Y\" to continue calculating with {num1}.\nType \"N\" to start a new calculation.\n ").lower()
    if check_con == "y":
        op = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What\'s the next number? "))
    elif check_con == "n":
        clear()
        print(logo)
        num1 = float(input("What\'s the first number? "))
        op = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What\'s the next number? "))
    elif  check_con == "q":
        continue_cal = False
