# roller coaster ticket （版本一）

# height = float ( input("What\'s your height in cm?\n"))

# if height >120:
#     age = int (input("what\'s your age?\n"))
#     photo = str(input("Want photos? (Y/N)\n"))
#     if age < 12:
#         if photo == "Y":
#             print ("The total bill is $8.")
#         else:
#             print ("The total bill is $5.")
#     elif age <18:
#         if photo == "Y":
#             print ("The total bill is $10.")
#         else:
#             print ("The total bill is $7.")
#     else:
#         if photo == "Y":
#             print ("The total bill is $15.")
#         else:
#             print ("The total bill is $12.")
# else:
#     print("Sorry, you can\'t ride.")


########################################################

#roller coaster （版本二）

height = float ( input ("What\'s your height in cm?\n"))
age = int ( input ("What\'s your age?\n"))
bill = 0

if height > 120:
    photo = str ( input ("Want photos? $3 per photo. (Y/N)\n"))
    if age < 12:
        bill += 5
        print ("Child ticket is $5.")
        if photo == "Y":
            bill += 3
            print (f"The total bill is ${bill}.")
        else:
            print (f"The total bill is ${bill}.")
    elif age <18:
        bill += 7
        print ("Teenage ticket is $7.")
        if photo == "Y":
            bill += 3
            print (f"The total bill is ${bill}.")
        else:
            print (f"The total bill is ${bill}.")
    else:
        bill += 12
        print ("Adault ticket is $12.")
        if photo == "Y":
            bill += 3
            print (f"The total bill is ${bill}.")
        else:
            print (f"The total bill is ${bill}.")
else:
    print ("Sorry, you can\'t ride.")

