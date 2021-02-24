Statement
It is possible to place 8 queens on an 8×8 chessboard so that no two queens threaten each other. Thus, it requires that no two queens share the same row, column, or diagonal.  

Given a placement of 8 queens on the chessboard. If there is a pair of queens that violates this rule, print YES, otherwise print NO. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chessboard with rows and columns numbered from 1 to 8.

https://i.imgur.com/Nf8NcwU.png

Example input
1 5
2 3
3 1
4 7
5 2
6 8
7 6
8 4
(shown on the picture)

Example output
NO

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/lists/ 

You may also try step-by-step theory chunks:
https://snakify.org/lessons/lists/steps/1/



# 檢查同行與同列
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
x5, y5 = map(int, input().split())
x6, y6 = map(int, input().split())
x7, y7 = map(int, input().split())
x8, y8 = map(int, input().split())

set_x = {x1, x2, x3, x4, x5, x6, x7, x8}
set_y = {y1, y2, y3, y4, y5, y6, y7, y8}

# 檢查對角線
a1, b1 = x1-y1, x1+y1
a2, b2 = x2-y2, x2+y2
a3, b3 = x3-y3, x3+y3
a4, b4 = x4-y4, x4+y4
a5, b5 = x5-y5, x5+y5
a6, b6 = x6-y6, x6+y6
a7, b7 = x7-y7, x7+y7
a8, b8 = x8-y8, x8+y8

set_a = {a1, a2, a3, a4, a5, a6, a7, a8}
set_b = {b1, b2, b3, b4, b5, b6, b7, b8}

if len(set_x)<8 or len(set_y)<8:
  print("YES")
elif len(set_a)<8 or len(set_b)<8:
  print("YES")
else:
  print("NO")



Model Solution

x = []
y = []
for i in range(8):
  a = [int(s) for s in input().split()]
  x.append(a[0])
  y.append(a[1])
answer = 'NO'
for i in range(8):
  for j in range(i + 1, 8):
    if ((x[i] == x[j]) or
        (y[i] == y[j]) or
        (abs(x[i] - x[j]) == abs(y[i] - y[j]))):
      answer = 'YES'
print(answer)
