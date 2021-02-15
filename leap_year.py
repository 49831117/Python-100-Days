
year = int(input("Which year do you want to check?\n "))

if year%400 == 0:
    print(f"{year} is leap year")
elif year%100 == 0:
    print(f"{year} is NOT leap year")
elif year%4 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is NOT leap year")


# 另解
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  
