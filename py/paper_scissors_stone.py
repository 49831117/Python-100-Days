import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

guest = int(input ("What do you choose?\nType 1 for paper, 2 for scissors, 3 for rock.\n"))
if guest == 1:
  print ("You: paper\n", paper)
elif guest == 2:
  print ("You: scissors\n", scissors)
elif guest == 3:
  print ("You: rock\n", rock)
else:
  print ("You enter the wrong digit.")

computer = int (random.randint(1, 3))
if computer == 1:
  print ("computer: paper\n", paper)
elif computer == 2:
  print ("computer: scissors\n", scissors)
elif computer == 3:
  print ("computer: rock\n", rock)

# if guest == computer:
#   print ("Draw.")
# elif guest == 1:
#   if computer == 2:
#     print ("You lose.")
#   else:
#     print ("You win.")
# elif guest == 2:
#   if computer == 1:
#     print ("You win.")
#   else:
#     print ("You lose.")
# elif guest == 3:
#   if computer == 1:
#     print ("You lose.")
#   else:
#     print ("You win.")

a = guest
b = computer

if a == b:
    print ("Draw.")
elif a < b and (-1)**(a-b) < 0:
    print ("You lose.")
elif a == 3 and b ==1:
    print ("You lose.")
else:
    print ("You win.")

# # 反思:
# import numpy
# list_i = [輸, 贏, 平手] , for i = 1, 2, 3
# random 輸、贏、平手
# 再對照印出 array 的可行性？

# 解法： https://repl.it/@appbrewery/rock-paper-scissors-end#main.py
# NOTE：game_images = [rock, paper, scissors] 的想法很讚
