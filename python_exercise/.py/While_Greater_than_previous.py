'''
Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of elements of the sequence that are greater than their neighbors above.  

Example input
1
2
3
4
5
0

Example output
4

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/while_loop/   

You may also try step-by-step theory chunks:
https://snakify.org/lessons/while_loop/steps/1/

'''


n = int( input())
list = []
count = 0

while n != 0:
  list += [n]
  length = len(list)
  if list[length-2]<list[length-1]:
    count += 1
  n = int( input())
print(count)
    
  


# Model Solution

# prev = next = int(input())
# counter = 0
# while next != 0:
#   if prev < next:
#     counter += 1
#   prev, next = next, int(input())
# print(counter)