Statement
Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.

The program receives two integers from 1 to 8 specifying the column and row number of the square.

https://i.imgur.com/z5rz8pa.png

Example input #1
1
1

Example output #1
YES

Example input #2
1
2

Example output #2
NO

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/if_then_else_conditions/  

You may also try step-by-step theory chunks:
https://snakify.org/lessons/if_then_else_conditions/steps/1/


x = int (input ())
y = int (input ())

if x%2 == 0 and y%2 == 0:
  print ("YES") # 黑色
elif x%2 == 1 and y%2 == 1:
  print ("YES") # 黑色
else:
  print ("NO")


  Model Solution

x1 = int(input())
y1 = int(input())

if (x1 + y1) % 2 == 0:
  print('YES')
else:
  print('NO')
