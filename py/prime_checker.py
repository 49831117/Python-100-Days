# way1 by myself
import math

def prime_checker(number):
    check_ceil = math.sqrt(number)       # 開根號
    check_ceil = math.floor(check_ceil)  # 無條件捨去，取整數
    divide_list = []
    stop = check_ceil + 1
    for x in range(2, stop, 1):
        t = 2
        while t < stop:
            #print (f"Checking {x}...")
            if number % t == 0:
                if t not in divide_list:
                    divide_list += [t]
            t += 1
    if divide_list == []:
        print(f"{number} is a prime number.")
    else:
        #divide_list.remove(1)   # 質數不含1，把 1 移除   # 後來改變列表方式，故註記掉
        p = ", ".join(str(v) for v in divide_list)
        print (f"{number} is NOT a prime number.\nPrime factor: {p}")
    
number = int (input("Which number do you want to check if it\'s a prime number or not? "))
prime_checker(number)


# way2 參考作法

# import math

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print ("It\'s a prime number.")
#     else:
#         print ("It\'s not a prime number.")
# num = int ( input ("Which number do you want to check is prime or not: "))
# prime_checker ( num )