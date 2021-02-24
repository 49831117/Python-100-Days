Statement
Given two positive integers n and m, create a two-dimensional array of size n×m and populate it with the characters "."and "*" in a chequered pattern. The top left corner should have the character "." .

Example input
6 8

Example output
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/two_dimensional_lists_arrays/    

You may also try step-by-step theory chunks:
https://snakify.org/lessons/two_dimensional_lists_arrays/steps/1/



m, n = map(int, input().split())

a = [['.']*m for i in range(n)]

for i in range(n):
  for j in range(m):
    if (i+j)%2 != 0:
      a[i][j] = '*'
for row in a:
  print (*row)


  Model Solution

  n, m = [int(s) for s in input().split()]
a = [['.' if (i + j) % 2 == 0 else '*']
     for i in range(n)
     for j in range(m)]
for line in a:
  print(*line)