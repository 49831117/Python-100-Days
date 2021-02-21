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
