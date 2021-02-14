logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# 因原寫法定義兩個類似步驟的函數，故嘗試合併。
def caeser(direction_input, text_input, shift_amount):
    end_text = ""
    if direction_input == "decode":
        shift_amount = int(shift_amount)
        shift_amount *= -1
    for alph in text:
        if alph in alphabet:
            position = alphabet.index(alph)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += alph

    print(f"{direction_input} \"{text_input}\" in {shift_amount} digits result：\n {end_text}")


continue_or_not = True

while continue_or_not is True:
    # 選擇加密或解密
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    # 欲加密 / 解密的文字，並轉成小寫
    text = input("Type your message:\n ").lower() 
    # 平移字元數量
    shift = int(input("Type the shift number:\n "))
    # mod 26
    shift = shift % 26

    caeser(direction_input=direction, text_input=text, shift_amount=shift)

    # 是否要繼續執行程式?
    want_continue = input("Type 'yes' if you want to decode or encode again. Otherwise type 'no'.\n ").lower()
    if want_continue == "no":
        continue_or_not = False
        print("Goodbye.")
    elif want_continue == "yes":
        continue_or_not = True
    # Quetion: 如果輸入 yes or no 以外的字?





# def encrypt(text_input, shift_amount):
#     for alph in text:
#         new_index = alphabet.index(alph) + int(shift)
#         print(alphabet[new_index], end = "")
    
# def decrypt(text_input, shift_amount):
#     for alph in text:
#         new_index = alphabet.index(alph) - int(shift)
#         print(alphabet[new_index], end = "")

# if direction == "encode":
#     print(f"{direction} {text} {shift} digits result：")
#     encrypt(text)
# elif direction == "decode":
#     print(f"{direction} {text} {shift} digits result：")
#     decrypt(text)
# else:
#     print("Input error.")