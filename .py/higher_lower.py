
"""
剩迴圈、美化
"""



logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import os
def clear():
    os.system('cls')
import random
from game_data import data

def compare(a, b):
    '''return who has more follower_count'''
    if a["follower_count"] < b["follower_count"]:
        return "b"
    elif a["follower_count"] > b["follower_count"]:
        return "a"

def check_point(count):
    if count != 0:
        print(f"You're right! Your current score is {count}.\n")

continue_game = True
count = 0
a, b = random.sample(data, 2)

a = dict(a)
b = dict(b)


while continue_game:
    clear()
    print(logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    right = compare(a, b)
    print("偷看答案：", right)
    print("\n")
    check_point(count)
    ans = input("Who has the more follower? (A/B) ").lower()
    if right != ans:
        clear()
        print(logo)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        print("\n\n")
        print(f"Sorry, you're answer ({ans.upper()}) is wrong! Your final score is {count}.\n")
        continue_game = False
    a = b
    b = dict(random.choice(data))
    while a == b:
        b = dict(random.choice(data))
    count += 1 
    
 