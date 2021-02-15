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

"""
# 另解：############################################ 覺得很棒!!!
# key point:
# 1. 將運算子存成字典，再用字典呼叫對應的函數。
# 2. 將完整運算邏輯定義成函數。
# 3. 最後只需要呼叫函數即可。
# 4. 注意：自己呼叫自己的函數容易造成 infinite loop 要小心使用。

import os
def clear():
    os.system('cls')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# 1. 
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


# 2.
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol) # 印出字典的所有 key（運算符號）

  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol] # 抓取對應運算子
    answer = calculation_function(num1, num2) # 根據對應運算子做運算

    print(f"{num1} {operation_symbol} {num2} = {answer}") # 印出運算結果

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear() # 清空終端機
      calculator() # 重新呼叫完整運算邏輯

# 3.
calculator()
"""