import random

names_string = input("Give me everybody\'s names, separated by a comma and a space.\n")
names = names_string.split(", ")
import random
# people_num = len ( names )
# random_num = random.randint(0, people_num -1 ) #要減一
# print (f"{names[random_num].upper()} needs to pay the check!")  # f-string + .upper() 的用法！
print ( f"{random.choice(names).upper()} needs to pay the check.")