Statement
Chess knight can move to a square that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally. The complete move therefore looks like the letter L. Given two different squares of the chessboard, determine whether a knight can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a knight can go from the first square to the second one in a single move or NO otherwise.

https://i.imgur.com/lzDMi1m.png

Example input
2
4
3
2

Example output
YES

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/if_then_else_conditions/ 

You may also try step-by-step theory chunks:
https://snakify.org/lessons/if_then_else_conditions/steps/1/  



x1 = int (input ())
y1 = int (input ())
x2 = int (input ())
y2 = int (input ())

diff_x = abs (x1 - x2)
diff_y = abs (y1 - y2)

if diff_x != 0:
  m = float (diff_y / diff_x)

if diff_x == 0:
  print ("NO")
elif m == 0.5 or m == 2:
  print ("YES")
else:
  print ("NO")



Model Solution

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
  print('YES')
else:
  print('NO')