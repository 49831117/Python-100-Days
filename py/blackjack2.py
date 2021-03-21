
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import os

def clear():
    os.system('cls')

def deal_card(): # 抽牌
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list):
    """Take a list of cards and return the score calculated from the cards."""
    if len(list) == 2 and sum(list) == 21:
        return 0 # Blackjack
    if sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    return sum(list)

def compare(user_score, computer_score):
    """compare scores between user and computer"""
    if computer_score == 0:
        return "\nBlackJack.\nSorry, you loss.\n"
    elif computer_score == user_score:
        return "\nDraw.\n"
    elif user_score == 0:
        return "\nBlackJack.\nCongratulations! You win.\n"
    elif user_score > 21:
        return "\nBOOOOOOM!\nSorry, you lose.\n"
    elif computer_score > 21:
        return "\nBOOOOOOM!\nCongratulations! You win.\n"
    elif user_score > computer_score:
        return "\nCongratulations! You win.\n"
    else:
        return "\nSorry, you loss.\n"
    

play_or_not = input("Do you want to play a game of Blackjack? (Y/N) ").lower()

while play_or_not == "y":
    # while not game_over:
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2): # 抽兩次牌並加入手牌
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_over:
        clear()
        print(logo)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass.\n ").lower() # 問玩家是否要加牌
            if user_should_deal == "y":
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hands: {user_cards}\nYour final score: {user_score}\nComputer's final hand: {computer_cards}\nComputer's final score: {computer_score}\n")
    print(compare(user_score, computer_score))

    play_or_not = input("Do you want to play a game of BlackJack? (Y/N) ").lower()
