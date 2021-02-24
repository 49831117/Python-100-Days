'''
Statement
Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. Multiply every element by c and print the result.

Example input
3 4
11 12 13 14
21 22 23 24
31 32 33 34
2

Example output
22 24 26 28
42 44 46 48
62 64 66 68

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/two_dimensional_lists_arrays/  

You may also try step-by-step theory chunks:
https://snakify.org/lessons/two_dimensional_lists_arrays/steps/1/


'''

# 行數、列數
row, col = [int(i) for i in input().split()]
# 生成矩陣
a = [[int(j) for j in input().split()] for i in range(row)]
# 乘數
mul = int(input())

for i in range(row):
  for j in range(col):
    a[i][j] *= mul

for row in a:
  print(*row)





# Model Solution

# m, n = [int(s) for s in input().split()]
# a = [[int(j) for j in input().split()] for i in range(m)]
# c = int(input())
# for i in range(m):
#   for j in range(n):
#     a[i][j] *= c
# for line in a:
#   print(*line)