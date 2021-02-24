'''
Statement
Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:

On the main diagonal put 0.
On the diagonals adjacent to the main put 1.
On the next adjacent diagonals put 2, and so forth.

Example input
5


Example output
0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/two_dimensional_lists_arrays/  

You may also try step-by-step theory chunks:
https://snakify.org/lessons/two_dimensional_lists_arrays/steps/1/

'''

n = int( input())
a = [[0]*n for i in range(n)] # 生成 n*n 的零矩陣

for i in range(n):
  for j in range(n):
    a[i][j] = abs(i - j)
for row in a:
  print(*row)



# Model solution

# n = int(input())
# a = [[0] * n for i in range(n)]
# for i in range(n):
#   for j in range(n):
#     a[i][j] = abs(i - j)
# for line in a:
#   print(*line)