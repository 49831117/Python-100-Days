print ("Welcome to the calculator!")
name1 = str( input ("What\'s your name?\n")).lower()
name2 = str ( input ("What\'s their name?\n")).lower()
combine_name = name1 + name2
t = int (combine_name.count("t"))
r = int (combine_name.count("r"))
u = int (combine_name.count("u"))
e = int (combine_name.count("e"))
total_true = str (t + r + u + e)
l = int (combine_name.count("l"))
o = int (combine_name.count("o"))
v = int (combine_name.count("v"))
e = int (combine_name.count("e"))
total_love = str (l + o + v + e)
score = int (total_true + total_love)
if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like code and mentos.")
elif score >= 40 and score <= 50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score is {score}.")

# 也可以改成用 Day 4 的 random 模組