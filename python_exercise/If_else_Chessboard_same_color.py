Statement
Given two squares of a chessboard. If they are painted in the same color, print YES, otherwise print NO.

The program receives four integers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square.

https://i.imgur.com/iLmObtC.png

Example input
1
1
2
6

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

color1 = x1 + y1
color2 = x2 + y2

if color1%2 == 0 and color2%2 == 0: # 皆黑色
  print ("YES")
elif color1%2 == 1 and color2%2 ==1: # 皆白色
  print ("YES")
else:
  print ("NO")



  Model Solution

  x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
  print('YES')
else:
  print('NO')