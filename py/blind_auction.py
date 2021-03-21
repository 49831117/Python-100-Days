logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# 輸入完一筆資訊後，清除畫面並繼續輸入，以示公平。
# Review：https://en.wikipedia.org/wiki/Hangman_(game)
import os
def clear():
    os.system('cls')

print(logo)

print("Welcome to the secret auction program.")

blind_bid_list = {}

go_on = True

while go_on:

    name = input("What\'s your name?\n ")
    dollars = int(input("What\'s your bid?\n $"))

    blind_bid_list[name] = dollars

    check_go_on = input("Are there any other bidders? (yes/no) \n ").lower()
    
    if check_go_on == "yes":
        clear()
    elif check_go_on == "no":
        maximun = max([v for v in blind_bid_list.values()])
        name_of_bidder = []
        for k in blind_bid_list:
            if blind_bid_list[k] == maximun:
                name_of_bidder += [k]
        name_of_bidder = "".join(name_of_bidder)
        print(f"The winner is {name_of_bidder} with a bid of ${maximun}.")
        go_on = False



# # 參考答案
# 定義新的函數，用以紀錄最高得主及最高投標金額。

# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
#         '''
# import os
# def clear():
#     os.system('cls')

# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # eg. bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
  

