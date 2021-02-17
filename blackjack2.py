
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


# 隨機抽取一張牌
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# 計算手牌總分
def calculate_score(cards):
    '''抽牌與計算手牌總分'''
    # 玩家與電腦手牌
    user_cards = []
    computer_cards = []
    
    # 抽兩張牌加入手牌
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        # list += new_card 必須要在 new_card 也是 list 的前提下才能使用
        # 但此處 new_card 為一元素，故使用 .append()
    
    calculate_score(user_cards)

    # 若手上只有兩張牌 Ace + 10（J/Q/k），則 Blackjack（score = 0）
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # 若手上有 Ace 但 score > 21，則 Ace 則以 1 計。
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)


    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    



