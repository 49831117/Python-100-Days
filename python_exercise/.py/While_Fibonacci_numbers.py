'''
Statement
Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Given a positive integer n, print the nth Fibonacci number.

Example input
6

Example output
8

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/while_loop/     

You may also try step-by-step theory chunks:
https://snakify.org/lessons/while_loop/steps/1/

'''

n = int (input ())

a = 1
b = 1
i = 1

while i < n:
  c = a + b
  a = b
  b = c
  i += 1
print (a)
  

# Model Solution

# prev, next = 1, 1
# n = int(input())
# for i in range(n - 2):
#   prev, next = next, prev + next
# print(next)