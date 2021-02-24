Statement
Given a sequence of distinct non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.

Example input
1
7
9
0

Example output
7

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/while_loop/   

You may also try step-by-step theory chunks:
https://snakify.org/lessons/while_loop/steps/1/




n = int(input())
list = []

while n != 0:
  list += [n]
  n = int( input())

a = list.sort()
print( list[-2] )


Model Solution

maximum = int(input())
second_maximum = int(input())
if second_maximum > maximum:
  second_maximum, maximum = maximum, second_maximum
a = -1
while a != 0:
  a = int(input())
  if a > maximum:
    second_maximum, maximum = maximum, a
  elif a > second_maximum:
    second_maximum = a
print(second_maximum)