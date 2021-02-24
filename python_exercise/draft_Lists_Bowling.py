Statement
In bowling, the player starts with 10 pins in a row at the far end of a lane. The goal is to knock all the pins down. For this assignment, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled.

The balls are numbered from 1 to N for this situation. The subsequent number pairs, one for each K represent the first and last (inclusive) positions of the pins that were knocked down with each roll. Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down.

Example input
10 3
8 10
2 5
3 6


# 15 4
# 1 1
# 1 4
# 6 8
# 7 9


Example output
I.....I...

# ....I....IIIIII

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/lists/ 

You may also try step-by-step theory chunks:
https://snakify.org/lessons/lists/steps/1/



n, m = input().split(" ")

list = ["I" for k in range(int(n))]
# print("".join(list))

for i in range(int(n)):
  a, b = map(int(r) for r in input().split())
  a = int(a)
  b = int(b)
  for j in range(a, b):
    list[j] = ['.']

str = "".joint(list)  
print(str)







# 如果改問：輸入的為倒下的保齡球，做法如下：
# s = set()
# for i in range(int(m)):
#   for element in map(int, input().split()):
#     s.add(element)

# for k in range(int(n)):
#   if k in s:
#     print(".", end = "")
#   else:
#     print("I", end = "")
