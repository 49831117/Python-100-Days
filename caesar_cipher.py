alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 選擇加密或解密
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# 欲加密 / 解密的文字，並轉成小寫
text = input("Type your message:\n").lower() 
# 平移字元數量
shift = input("Type the shift number:\n")

# 因原寫法定義兩個類似步驟的函數，故嘗試合併。
def caeser(direction_input, text_input, shift_amount):
    print(f"{direction_input} \"{text_input}\" {shift_amount} digits result：")
    if direction_input == "decode":
        shift_amount = int(shift_amount)
        shift_amount *= -1
    for alph in text:
        new_index = alphabet.index(alph) + int(shift_amount)
        print(alphabet[new_index], end = "")

caeser(direction_input=direction, text_input=text, shift_amount=shift)


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