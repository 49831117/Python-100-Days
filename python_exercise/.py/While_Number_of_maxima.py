'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Find how many elements of this sequence are equal to its largest element.

Example input #1
1
7
9
0

Example output #1
1

Example input #2
1
3
3
1
0

Example output #2
2

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/while_loop/   

You may also try step-by-step theory chunks:
https://snakify.org/lessons/while_loop/steps/1/

'''



n = int( input())
list = []

while n != 0:
  list += [n]
  n = int( input())

max = max( list )
print(list.count(max))


# Model Solution

# maximum = int(input())
# counter = 1
# a = -1
# while a != 0:
#   a = int(input())
#   if a > maximum:
#     maximum, counter = a, 1
#   elif a == maximum:
#     counter += 1
# print(counter)
