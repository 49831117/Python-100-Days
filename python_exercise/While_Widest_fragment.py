Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Determine the length of the widest fragment where all the elements are equal to each other.

Example input
1
7
7
9
1
0

Example output
2

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/while_loop/    

You may also try step-by-step theory chunks:
https://snakify.org/lessons/while_loop/steps/1/



# 將輸入值存入 list
n = int(input())
list = []
while n != 0:
    list += [n]
    n = int( input())

# 預設值
count = 1
list2 = [1]
length = len(list)
# 檢查前後項是否相符，若無則1，若有則計數。
for i in range(length-1):
  if list[i] == list[i+1] and i < length-1:
    count += 1
    list2 += [ count ]
  elif list[i] != list[i+1] and i < length-1:
    count = 1
    list2 += [ count ]


# 印出檢查結果
print(max(list2))
    

# 參考答案
# next = int(input())
# length = 1
# max_length = 1
# while next != 0:
#   prev, next = next, int(input())
#   if prev == next:
#     length += 1
#   else:
#     length = 1
#   max_length = max(length, max_length)
# print(max_length)







# max_count = 0
# count = 1
# length = len(list)
# k = 0

# for x in range(length-1):
#     count = 1
#     for k in range(length - 1):
#         if list[k] == list[k+1]:
#             count += 1
#             k += 1
#         if max_count < count:
#             max_count = count
# print ( max_count )