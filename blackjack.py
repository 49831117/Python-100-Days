
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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# 玩家抽一張牌，並紀錄手牌及總和
def mylist(list):
    j = random.randint(1, 13)
    if j == 0 and 11 in list:
        list.append(1)
    elif (sum(list) + int(cards[j-1])) > 21 and (11 in list):
        list.replace(11, 1)
        list.append(cards[j-1])
    else:
        list.append(cards[j-1])
    return list

# 當玩家 stand 輪到莊家抽牌，過程中若莊家手牌總和 < 17 就得抽下一張牌，直到滿足條件為止，並紀錄莊家手牌及總和。
def computerlist(c_list):
    if sum(c_list) == 21:
        print("==== Black Jack! ====\n")
        checkwinner2(list, c_list)
    elif sum(c_list) < 17: # 莊家必須 hit
        j = random.randint(1, 13)
        if j == 0 and 11 in c_list:
            c_list.append(1)
        elif (sum(c_list) + int(cards[j-1])) > 21 and (11 in list):
            c_list.replace(11, 1)
            c_list.append(cards[j-1])
        elif (sum(c_list) + int(cards[j-1])) > 21 and (11 not in list):
            c_list.append(1)
        else:
            c_list.append(cards[j-1])
        computerlist(c_list)
    else: # 莊家 >= 17 必須 stand
        return c_list
    

# check bust
def checkbust(list):
    if sum(list) > 21:
        print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}, your score: {sum(list)}\nBust! You loss.\n")
        return
    elif sum(list) == 21:
        hit_or_stand(list)
    else:
        print(f"Your cards: {list}, current score: {sum(list)}")
        hit_or_stand(list)


# check who win the game
def checkwinner(list, c_list):
    if sum(list) < 22:
        if sum(list) > sum(c_list) or sum(c_list) > 21:
            print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}, your score: {sum(list)}\nCongratulations! You win!\n")
        elif sum(list) < sum(c_list):
            print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}, your score: {sum(list)}\nSorry! You loss!\n")
        elif sum(list) == sum(c_list):
            print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}, your score: {sum(list)}\nDraw!\n")
        return
    elif sum(list) > 21:
        checkbust(list)

def checkwinner2(list, c_list):
    if sum(c_list) < 21:
        print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}, your score: {sum(list)}\nCongratulations! You win!\n")
    elif sum(c_list) == 21:
        print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}, your score: {sum(list)}\nDraw!\n")
        return
    elif sum(list) > 21:
        checkbust(list)


# hit or stand
def hit_or_stand(list):
    hit = True
    sum1 = sum(list)
    sum2 = sum(c_list)
    while hit:
        if sum1 > 21 or sum2 > 21:
            checkwinner2(list, c_list)
            checkbust(list)
            break
        elif sum1 < 21:
            h_or_s = input("Type 'y' to get another card, type 'n' to pass. (Y/N) ").lower()
            print("")
            if h_or_s == "y":
                mylist(list) # 玩家再抽一張牌
                checkbust(list) # 檢查玩家是否 > 21
                hit = False
            elif h_or_s == "n": # 玩家 stand
                computerlist(c_list)
                checkwinner(list, c_list) 
                hit = False               
        elif sum1 == 21:
            print("==== Black Jack! ====\n")
            computerlist(c_list)
            checkwinner2(list, c_list)
            hit = False
        else:
            checkwinner(list, c_list)
            hit = False
        

list = []
c_list = []


playornot = input("Do you want to play a game of Blackjack? (Y/N) ").lower()

if playornot == "y":
    clear()
    print(logo)

    mylist(list)
    mylist(list)

    j = random.randint(1, 13)
    c_list.append(cards[j-1])
    k = random.randint(1, 13)
    c_list.append(cards[k-1])
    print(f"\nYour cards: {list}, current score: {sum(list)}")
    if sum(c_list) == 21:
        print("\n==== Black Jack! ====\n")
        print(f"Computer's cards: {c_list}, and computer's score: {sum(c_list)}\nYour cards: {list}.\nSorry! You loss!\n")
    else:
        print(f"Computer's first card: {c_list[0]}\n")
        hit_or_stand(list)