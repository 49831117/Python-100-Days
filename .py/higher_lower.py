
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


a, b = random.sample(data, 2)

print("偷看答案", compare(a, b))
count = 0

a_name = a["name"]
a_follower_count = a["follower_count"]
a_description = a["description"]
a_country = a["country"]

b_name = b["name"]
b_follower_count = b["follower_count"]
b_description = b["description"]
b_country = b["country"]


print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
print(f"Compare B: {b_name}, a {b_description}, from {b_country}.")

ans = input("Who has the more follower? (A/B)").lower()
if ans == compare(a, b):
    count += 1
    print(f"You're right! Current score: {count}.")
else:
    print(f"You're wrong! Current score: {count}.")

a = [b]
b = random.sample(data, 1)

a_name = a[0]["name"]
a_follower_count = a[0]["follower_count"]
a_description = a[0]["description"]
a_country = a[0]["country"]

b_name = b[0]["name"]
b_follower_count = b[0]["follower_count"]
b_description = b[0]["description"]
b_country = b[0]["country"]


print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
print(f"Compare B: {b_name}, a {b_description}, from {b_country}.")