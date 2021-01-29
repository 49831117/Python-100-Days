# FizzBuZZ
# 3 的倍數：Fizz／5 的倍數：Buzz／15 的倍數：FizzBuzz
for n in range(1, 101):
    if n % 15 == 0:
        n = "FizzBuzz"
        print (n)         # print("FizzBuzz")
    elif n % 5 == 0:
        n = "Buzz"
        print (n)         # print ("Buzz")
    elif n % 3 == 0:
        n = "Fizz"
        print (n)         # print ("Fizz")
    else:
        print (n)