# HangMan
import hangmanartandwords
import random
### from replit import clear  ### 這要怎麼放進 VS Code？
import os
def clear():
    os.system('cls')

print (hangmanartandwords.logo)

chosen_word = random.choice(hangmanartandwords.word_list)
#print(f'Pssst, the solution is {chosen_word}.') #偷看答案，測試用

word_lenth = len( chosen_word )

display = [ [] for _ in range(word_lenth)]
for k in range (word_lenth):
    display[k] = "_"
# 此時 display = ['_', '_', '_', '_', '_', '_']
print ("Target:", "_ " * word_lenth ) # 只是為了好讀而已 # 此時印出 Target: _ _ _ ... _


die = 0
wrong_guess = []
letter_guessed = []

while "_" in display:
    guess = input("Guess a letter: ").lower()
    t = 0 # 記數用 #####
    
    if "_" in display:
        if guess not in chosen_word:
            if guess not in wrong_guess:
                wrong_guess += guess
                if die < 5:
                    die += 1
                    print ( hangmanartandwords.stages[die])
                    print (f"{guess} is NOT in the target word. You lose a life. Q_Q")
                    print ("Wrong Time:", die)
                else:
                    die += 1
                    print ( hangmanartandwords.stages[die])
                    print ("Wrong Time:", die)
                    print (f"You lose! The answer is '{chosen_word}'.")
                    break
                # target = " ".join(display)
                # print ("Target:", target)
            elif guess in wrong_guess:
                print ( hangmanartandwords.stages[die])
                print ("Wrong Time:", die)
                print (f"{guess} is false, you already guessed it. ~\"~ ")
            target = " ".join(display)
            print ("Target:", target)
        elif guess in chosen_word:            
            for letter in chosen_word:
                if t < word_lenth :
                    if letter == guess:
                        display[t] = guess
                    t += 1
            target = " ".join(display) # 不改變 list 結構，另外生成 string
            print ( hangmanartandwords.stages[die])
            print ("Target:", target) # 印出猜測後更新的字串            
            if guess in letter_guessed:
                print (f"You guessed {guess} already. Try other letter.")
            elif guess not in letter_guessed:
                letter_guessed += guess
if "_" not in display:
    print("You win!") # 告知已猜完


