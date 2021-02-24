'''
Statement
Given a list of non-zero integers, find and print the first adjacent pair of elements that have the same sign. If there is no such pair, print 0.

Example input #1
-1 2 3 -1 -2

Example output #1
2 3

Example input #2
1 -3 4 -2 1

Example output #2
0

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/lists/ 

You may also try step-by-step theory chunks:
https://snakify.org/lessons/lists/steps/1/

'''

n = list(input().split(" "))
length = len(n)
k = 0
for i in range(length-1):
    if int(n[i])*int(n[i+1])>0:
        k = i
if int(n[0])*int(n[1])>0:
  print(n[0], n[1])
else:
  for i in range(1, length-1):
    if int(n[i])*int(n[i+1])>0:
        k = i
        break
  if k != 0:
    print(n[k], n[k+1])
  else:
    print(0)



# Model Solution

# a = [int(s) for s in input().split()]
# for i in range(1, len(a)):
#   if a[i - 1] * a[i] > 0:
#     print(a[i - 1], a[i])
#     break
# else:
#   print(0)