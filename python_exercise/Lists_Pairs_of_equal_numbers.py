Statement
Given a list of numbers, count a number of pairs of equal elements. Any two elements that are equal to each other should be counted exactly once.

Example input #1
1 2 3 2 3

Example output #1
2

Example input #2
1 1 1 1 1

Example output #2
10

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/lists/ 

You may also try step-by-step theory chunks:
https://snakify.org/lessons/lists/steps/1/



s = [int(i) for i in input().split()]
length = len(s)

i = 0
j = 1
count = 0

for i in range(length):
  for j in range(length):
    if i < j and s[i] == s[j]:
      count += 1
    j += 1
  i += 1
print( count )



Model Solution

a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
  for j in range(i + 1, len(a)):
    if a[i] == a[j]:
      counter += 1
print(counter)