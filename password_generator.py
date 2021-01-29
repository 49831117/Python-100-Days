import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n")) 
num_numbers = int(input(f"How many numbers would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like in your password?\n"))


# 暫存數：數字、符號、字母
x = 0
y = 0
z = 0

for num in numbers:
    random_number = random.sample(numbers, num_numbers)
    x += 1
for sym in symbols:
    random_symbol = random.sample(symbols, num_symbols)
    y += 1
for let in letters:
    random_letter = random.sample(letters, num_letters)

random_password = random_letter + random_number + random_symbol
print ("隨機選出的字元：" + "".join(random_password ))
random.shuffle( random_password )
str_password = "".join(random_password)
print ("將上述字元亂數排列後：" + str_password )
    