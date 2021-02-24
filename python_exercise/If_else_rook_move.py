'''
Statement
Chess rook moves horizontally or vertically. Given two different squares of the chessboard, determine whether a rook can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a rook can go from the first square to the second one in a single move or NO otherwise.

https://i.imgur.com/fBevTRT.png

Example input
4
4
5
5

Example output
NO

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/if_then_else_conditions/

You may also try step-by-step theory chunks:
https://snakify.org/lessons/if_then_else_conditions/steps/1/
'''

a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())

if a == c or b == d:
  print ("YES")
else:
  print ("NO")


Model Solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
  print('YES')
else:
  print('NO')