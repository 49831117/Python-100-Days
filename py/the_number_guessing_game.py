logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
'''

import random

guess_list = []
answer_num = random.choice(range(100)) + 1
print(logo)
# print(f"====== {answer_num} =====") # 偷看答案
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def compare(guess_num, attempts):
    global answer_num
    if guess_num != answer_num and attempts > 0:
        if guess_num < answer_num:
            print("Too low.")
            end_game = False
        elif guess_num > answer_num:
            print("Too high.")
            end_game = False
        print("Guess again.")
        return end_game
    elif guess_num == answer_num and attempts > 0:
        print(f"You got it! The answer was {answer_num}.")
        end_game = True
        return end_game
    elif attempts <1:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {answer_num}.")
        end_game = True
        return end_game

if easy_or_hard == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    end_game = False
    while not end_game:
        guess_num = int(input("Make a guess: "))
        attempts -= 1
        end_game = compare(guess_num, attempts)
        if not end_game:
            print(f"You have {attempts} attempts remaining to guess the number.")
elif easy_or_hard == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    end_game = False
    while not end_game:
        guess_num = int(input("Make a guess: "))
        attempts -= 1
        end_game = compare(guess_num, attempts)
        if not end_game:
            print(f"You have {attempts} attempts remaining to guess the number.")

'''
# 參考作法

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns): #Function to check user's guess against actual answer.
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty(): #Make function to set difficulty.
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!") 
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")  #Choosing a random number between 1 and 100.

  turns = set_difficulty()
  guess = 0
  while guess != answer: #Repeat the guessing functionality if they get it wrong.
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))#Repeat the guessing functionality if they get it wrong.
    turns = check_answer(guess, answer, turns) #Track the number of turns and reduce by 1 if they get it wrong.
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()

'''